from flask import Flask, request, jsonify
from database.model import Database
from retrieval.embeddings import EmbeddingModel
from retrieval.vector_store import VectorStore
from utils.text_processing import clean_text, chunk_text
import json

app = Flask(__name__)

# Initialize components
db = Database()
embedding_model = EmbeddingModel()
vector_store = VectorStore()

@app.route('/add_knowledge', methods=['POST'])
def add_knowledge():
    """
    Add text to the knowledge base directly from user input.
    """
    try:
        data = request.json
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
            
        text = data['text']
        
        # Process the text
        cleaned_text = clean_text(text)
        chunks = chunk_text(cleaned_text)
        
        # Generate embeddings and store
        embeddings = embedding_model.embed_batch(chunks)
        vector_store.add_documents(chunks, embeddings)
        
        return jsonify({
            'message': 'Knowledge added successfully',
            'chunks_processed': len(chunks)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """Process a chat query using the RAG system."""
    try:
        data = request.json
        if not data or 'query' not in data:
            return jsonify({'error': 'No query provided'}), 400
        
        query = data['query']
        user_context = data.get('context', '')  # Optional context from user
        
        # Clean and process the query
        cleaned_query = clean_text(query)
        query_embedding = embedding_model.embed_text(cleaned_query)
        
        # Retrieve relevant documents
        relevant_docs = vector_store.search(query_embedding)
        
        if not relevant_docs:
            response = "I couldn't find any relevant information to answer your question."
        else:
            # Combine context from knowledge base and user input
            context = " ".join(relevant_docs)
            if user_context:
                context = f"{user_context}\n{context}"
            response = f"Based on the available information: {context}"
        
        # Store conversation in database
        db.add_message('user', query)
        db.add_message('system', response)
        
        return jsonify({
            'answer': response,
            'retrieved_chunks': relevant_docs
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_chat_history', methods=['GET'])
def get_chat_history():
    """Get chat history for the current session."""
    try:
        history = db.get_history()
        return jsonify({
            'history': history,
            'message': 'Chat history retrieved successfully'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/clear_chat', methods=['POST'])
def clear_chat():
    """Clear the chat history."""
    try:
        db.clear_history()
        return jsonify({'message': 'Chat history cleared successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)