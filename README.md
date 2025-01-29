# RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that uses a vector database for semantic search and stores chat history in a local PostgreSQL database. The chatbot is served via a Flask API.

## Features

- Text corpus preprocessing and chunking
- Vector database for semantic search using FAISS
- Sentence embeddings using Hugging Face's sentence-transformers
- Chat history storage in PostgreSQL
- Flask API endpoints for chat and history retrieval

## Prerequisites

- Python 3.8+
- PostgreSQL
- Git

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd RAG_Chat_Bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following configurations:

## Database Setup

1. Create the PostgreSQL database:

2. Create the chat history table:
```sql
CREATE TABLE chat_history (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role VARCHAR(10) NOT NULL,
    content TEXT NOT NULL
);
```


## Usage

1. Start the Flask server:
```bash
python run.py
```

2. The API will be available at `http://localhost:5000`

### API Endpoints

1. **Chat Endpoint**
   - URL: `/chat`
   - Method: `POST`
   - Request Body:
     ```json
     {
         "query": "Your question here"
     }
     ```
   - Response:
     ```json
     {
         "answer": "Generated answer",
         "relevant_chunks": ["chunk1", "chunk2"]  // Optional
     }
     ```

2. **History Endpoint**
   - URL: `/history`
   - Method: `GET`
   - Response:
     ```json
     {
         "history": [
             {
                 "id": 1,
                 "timestamp": "2024-01-29T10:00:00",
                 "role": "user",
                 "content": "Question"
             },
             {
                 "id": 2,
                 "timestamp": "2024-01-29T10:00:01",
                 "role": "system",
                 "content": "Answer"
             }
         ]
     }
     ```

## Testing

Run the test suite:
```bash
python test.py
```

This will:
- Split the documents into chunks
- Generate embeddings
- Store them in the vector database

## License

This project is licensed under the MIT License - see the LICENSE file for details.