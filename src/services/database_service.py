"""
Database service for storing conversation history
"""
import sqlite3
import datetime
from typing import List, Tuple, Optional
import os

class DatabaseService:
    def __init__(self, db_path: str = "conversation_history.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database and create tables"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # 대화 내역 테이블 생성
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    username TEXT NOT NULL,
                    guild_id TEXT,
                    guild_name TEXT,
                    command TEXT NOT NULL,
                    user_input TEXT NOT NULL,
                    bot_response TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    tokens_used INTEGER DEFAULT 0
                )
            ''')
            
            # 사용자 통계 테이블 생성
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_stats (
                    user_id TEXT PRIMARY KEY,
                    username TEXT NOT NULL,
                    total_commands INTEGER DEFAULT 0,
                    total_tokens INTEGER DEFAULT 0,
                    last_activity DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
    
    def save_conversation(self, user_id: str, username: str, guild_id: str, 
                         guild_name: str, command: str, user_input: str, 
                         bot_response: str, tokens_used: int = 0):
        """Save a conversation to the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # 대화 내역 저장
            cursor.execute('''
                INSERT INTO conversations 
                (user_id, username, guild_id, guild_name, command, user_input, bot_response, tokens_used)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, username, guild_id, guild_name, command, user_input, bot_response, tokens_used))
            
            # 사용자 통계 업데이트
            cursor.execute('''
                INSERT OR REPLACE INTO user_stats 
                (user_id, username, total_commands, total_tokens, last_activity)
                VALUES (?, ?, 
                    COALESCE((SELECT total_commands FROM user_stats WHERE user_id = ?), 0) + 1,
                    COALESCE((SELECT total_tokens FROM user_stats WHERE user_id = ?), 0) + ?,
                    CURRENT_TIMESTAMP)
            ''', (user_id, username, user_id, user_id, tokens_used))
            
            conn.commit()
    
    def get_user_history(self, user_id: str, limit: int = 10) -> List[Tuple]:
        """Get conversation history for a specific user"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT command, user_input, bot_response, timestamp, tokens_used
                FROM conversations 
                WHERE user_id = ?
                ORDER BY timestamp DESC
                LIMIT ?
            ''', (user_id, limit))
            return cursor.fetchall()
    
    def get_user_stats(self, user_id: str) -> Optional[Tuple]:
        """Get statistics for a specific user"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT username, total_commands, total_tokens, last_activity
                FROM user_stats 
                WHERE user_id = ?
            ''', (user_id,))
            return cursor.fetchone()
    
    def get_server_stats(self, guild_id: str) -> List[Tuple]:
        """Get top users for a specific server"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT username, COUNT(*) as command_count, SUM(tokens_used) as total_tokens
                FROM conversations 
                WHERE guild_id = ?
                GROUP BY user_id, username
                ORDER BY command_count DESC
                LIMIT 10
            ''', (guild_id,))
            return cursor.fetchall()
    
    def search_conversations(self, user_id: str, keyword: str, limit: int = 5) -> List[Tuple]:
        """Search conversations by keyword"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT command, user_input, bot_response, timestamp
                FROM conversations 
                WHERE user_id = ? AND (user_input LIKE ? OR bot_response LIKE ?)
                ORDER BY timestamp DESC
                LIMIT ?
            ''', (user_id, f'%{keyword}%', f'%{keyword}%', limit))
            return cursor.fetchall()
    
    def clear_user_history(self, user_id: str):
        """Clear conversation history for a specific user"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM conversations WHERE user_id = ?', (user_id,))
            cursor.execute('DELETE FROM user_stats WHERE user_id = ?', (user_id,))
            conn.commit()
    
    def get_database_stats(self) -> dict:
        """Get overall database statistics"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # 총 대화 수
            cursor.execute('SELECT COUNT(*) FROM conversations')
            total_conversations = cursor.fetchone()[0]
            
            # 총 사용자 수
            cursor.execute('SELECT COUNT(*) FROM user_stats')
            total_users = cursor.fetchone()[0]
            
            # 총 토큰 사용량
            cursor.execute('SELECT SUM(tokens_used) FROM conversations')
            total_tokens = cursor.fetchone()[0] or 0
            
            # 가장 인기있는 명령어
            cursor.execute('''
                SELECT command, COUNT(*) as usage_count
                FROM conversations 
                GROUP BY command
                ORDER BY usage_count DESC
                LIMIT 5
            ''')
            popular_commands = cursor.fetchall()
            
            return {
                'total_conversations': total_conversations,
                'total_users': total_users,
                'total_tokens': total_tokens,
                'popular_commands': popular_commands
            } 