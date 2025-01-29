from config import Config

def chunk_text(text, chunk_size=Config.CHUNK_SIZE, overlap=Config.CHUNK_OVERLAP):
    """Split text into overlapping chunks."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def clean_text(text):
    """Clean and normalize text."""
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Basic normalization
    text = text.lower().strip()
    return text