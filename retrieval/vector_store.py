import chromadb
from chromadb.config import Settings
import numpy as np
from config import Config

class VectorStore:
    def __init__(self):
        self.client = chromadb.Client(Settings(
            persist_directory=Config.VECTOR_DB_PATH
        ))
        # Try to get existing collection, create if doesn't exist
        try:
            self.collection = self.client.get_collection("documents")
        except:
            self.collection = self.client.create_collection("documents")
    
    def add_documents(self, texts, embeddings):
        """Add documents and their embeddings to the vector store."""
        # Convert texts to list if it's not already
        if isinstance(texts, str):
            texts = [texts]
        if len(texts) == 0:
            return
            
        # Generate IDs
        ids = [f"doc_{i}" for i in range(len(texts))]
        
        # Add to collection
        try:
            self.collection.add(
                embeddings=embeddings.tolist() if isinstance(embeddings, np.ndarray) else embeddings,
                documents=texts,
                ids=ids
            )
        except Exception as e:
            print(f"Error adding documents: {str(e)}")
            raise
    
    def search(self, query_embedding, top_k=Config.TOP_K_RESULTS):
        """Search for most similar documents."""
        try:
            # Check if collection is empty
            if self.collection.count() == 0:
                return []
                
            results = self.collection.query(
                query_embeddings=query_embedding.tolist() if isinstance(query_embedding, np.ndarray) else query_embedding,
                n_results=min(top_k, self.collection.count())
            )
            return results['documents'][0] if results['documents'] else []
        except Exception as e:
            print(f"Error during search: {str(e)}")
            return []