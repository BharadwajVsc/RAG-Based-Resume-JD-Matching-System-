def chunking(text: str, chunk_size: int = 600, overlap: int = 100) -> list:
    """Splits text into overlapping chunks.

    Args:
        text (str): The input text to be chunked.
        chunk_size (int): The size of each chunk.
        overlap (int): The number of overlapping characters between chunks.

    Returns:
        list: A list of text chunks.
    """

    if not text:
        return []
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        if chunk.strip():
            chunks.append(chunk.strip())
        start = end - overlap
        if start < 0:
            start = 0
    return chunks
