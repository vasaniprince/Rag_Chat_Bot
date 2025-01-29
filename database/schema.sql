"""
CREATE DATABASE IF NOT EXISTS ragchatbot;
USE ragchatbot;

CREATE TABLE IF NOT EXISTS chat_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    role ENUM('user', 'system') NOT NULL,
    content TEXT NOT NULL
);
"""