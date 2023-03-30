def chunkify(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]