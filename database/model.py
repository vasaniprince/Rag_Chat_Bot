import psycopg2
from psycopg2 import OperationalError
from datetime import datetime
import time
from config import Config


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect()
    
    def connect(self, max_retries=3):
        retry_count = 0
        while retry_count < max_retries:
            try:
                self.connection = psycopg2.connect(
                    host=Config.POSTGRES_HOST,
                    port=Config.POSTGRES_PORT,
                    user=Config.POSTGRES_USER,
                    password=Config.POSTGRES_PASSWORD,
                    database=Config.POSTGRES_DB
                )
                self.cursor = self.connection.cursor()
                break
            except OperationalError as e:
                retry_count += 1
                if retry_count == max_retries:
                    raise Exception(f"Failed to connect to database after {max_retries} attempts: {str(e)}")
                time.sleep(1)  # Wait 1 second before retrying
    
    def add_message(self, role, content):
        try:
            if not self.connection:
                self.connect()
            
            query = """
            INSERT INTO chat_history (role, content)
            VALUES (%s, %s)
            """
            self.cursor.execute(query, (role, content))
            self.connection.commit()
        except OperationalError as e:
            print(f"Error adding message: {e}")
            raise
    
    def get_history(self):
        try:
            if not self.connection:
                self.connect()
                
            query = "SELECT * FROM chat_history ORDER BY timestamp ASC"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except OperationalError as e:
            print(f"Error getting history: {e}")
            raise
    
    def __del__(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Exception as e:
            print(f"Error closing database connections: {e}")
