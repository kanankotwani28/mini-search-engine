from collections import defaultdict
from preprocess import preprocess
import os

def build_inverted_index(documents_path: str):
    """
    Builds an inverted index from text documents.

    Returns:
        inverted_index: dict[word -> set(doc_ids)]
        documents: dict[doc_id -> original text]
    """
    inverted_index = defaultdict(set)
    documents = {}

    for filename in os.listdir(documents_path):
        if not filename.endswith(".txt"):
            continue

        doc_id = filename
        file_path = os.path.join(documents_path, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        documents[doc_id] = text

        tokens = preprocess(text)

        for token in tokens:
            inverted_index[token].add(doc_id)

    return inverted_index, documents
