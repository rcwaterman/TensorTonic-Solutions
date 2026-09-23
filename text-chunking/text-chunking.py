def text_chunking(tokens: list, chunk_size: int, overlap: int) -> list:
    """
    Returns fixed-size token chunks with the requested overlap.
    """
    # Write code here
    result = [tokens[0:chunk_size]] if len(tokens) else []
    for i in range(chunk_size, len(tokens), chunk_size-overlap):
        result.append(tokens[i-overlap:i+chunk_size-overlap])
        
    return result