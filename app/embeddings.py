from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")  # loading the model once


def generate_embeddings(chunks):
    texts = [chunk["text"] for chunk in chunks]  # Extract texts from chunks
    embeddings = model.encode(texts, show_progress_bar=True)  # Generate embeddings
    for i, chunk in enumerate(chunks):  # Add embeddings to corresponding chunks
        chunk["embedding"] = embeddings[i]  # Add embedding to chunk
    return chunks
