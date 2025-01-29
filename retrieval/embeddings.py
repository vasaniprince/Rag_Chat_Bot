from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingModel:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
    
    def embed_text(self, text):
        """Generate embeddings for a piece of text."""
        return self.model.encode(text)
    
    def embed_batch(self, texts):
        """Generate embeddings for multiple texts."""
        return self.model.encode(texts)