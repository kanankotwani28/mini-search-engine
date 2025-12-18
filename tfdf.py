import math
from collections import Counter

def compute_tfidf(documents, inverted_index):
    """
    Computes TF-IDF vectors for all documents.

    Returns:
        tfidf_vectors: dict[doc_id -> dict[word -> tfidf_score]]
    """
    total_docs = len(documents)
    tfidf_vectors = {}

    # Precompute IDF for each word
    idf = {}
    for word, docs in inverted_index.items():
        idf[word] = math.log(total_docs / len(docs))

    # Compute TF-IDF for each document
    for doc_id, text in documents.items():
        words = text.lower().split()
        word_counts = Counter(words)
        total_words = len(words)

        tfidf_vectors[doc_id] = {}

        for word, count in word_counts.items():
            if word in idf:
                tf = count / total_words
                tfidf_vectors[doc_id][word] = tf * idf[word]

    return tfidf_vectors
