from collections import defaultdict
from preprocess import preprocess

def build_inverted_index(documents):
    """
    documents:dict {doc_id: text}
    returns: inverted index{word: set(doc_ids)}
    """
    inverted_index = defaultdict(set)

    for doc_id, text in documents.items():
        tokens = preprocess(text)
        for token in tokens:
            inverted_index[token].add(doc_id)
    
    return inverted_index