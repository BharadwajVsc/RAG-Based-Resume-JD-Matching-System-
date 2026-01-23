import faiss
import numpy as np
import json
import os

# print("FAISS version:", faiss.__version__)


def build_faiss_index(
    chunks, index_path="data/faiss.index", meta_path="data/metadata.json"
):
    """Builds a FAISS index from text chunks and saves it to disk.

    Args:
        chunks (list): A list of dictionaries, each containing 'text' and 'embedding'.
        index_path (str): The file path to save the FAISS index.
        meta_path (str): The file path to save the metadata.

    Returns:
        faiss.Index: The built FAISS index.
    """

    os.makedirs("data", exist_ok=True)  # Ensure the data directory exists

    embeddings = np.array(
        [chunk["embedding"] for chunk in chunks], dtype="float32"
    )  # Convert embeddings to numpy array
    dimension = embeddings.shape[1]  # Get the dimension of embeddings
    index = faiss.IndexFlatL2(dimension)  # Create a FAISS index
    index.add(x=embeddings)  # type: ignore # Add embeddings to the index

    faiss.write_index(index, index_path)  # Save the index to disk

    metadata = [
        {"chunk_id": chunk["chunk_id"], "text": chunk["text"]} for chunk in chunks
    ]  # Prepare metadata

    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)  # Save metadata to disk

    return index
