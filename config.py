from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT = int(os.getenv('POSTGRES_PORT'))
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    CHUNK_SIZE = 300
    CHUNK_OVERLAP = 50
    TOP_K_RESULTS = 3
    VECTOR_DB_PATH = "./vector_db"