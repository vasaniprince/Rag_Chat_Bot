CREATE TABLE IF NOT EXISTS chat_history (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role VARCHAR(10) CHECK (role IN ('user', 'system')) NOT NULL,
    content TEXT NOT NULL
);