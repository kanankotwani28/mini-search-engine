import math
from collections import Counter

def cosine_similarity(vec1, vec2):
    """
    Computes cosine similarity between two vectors.
    Vectors are dictionaries: word -> weight
    """
    dot_product = 0.0

    for word in vec1:
        if word in vec2:
            dot_product += vec1[word] * vec2[word]

    magnitude1 = math.sqrt(sum(weight ** 2 for weight in vec1.values()))
    magnitude2 = math.sqrt(sum(weight ** 2 for weight in vec2.values()))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)

def build_query_vector(query, idf):
    """
    Converts a query string into a TF-IDF vector.
    """
    words = query.lower().split()
    word_counts = Counter(words)
    total_words = len(words)

    query_vector = {}

    for word, count in word_counts.items():
        if word in idf:
            tf = count / total_words
            query_vector[word] = tf * idf[word]

    return query_vector

def search(query, tfidf_vectors, idf):
    """
    Returns documents ranked by relevance to the query.
    """
    query_vector = build_query_vector(query, idf)
    scores = {}

    for doc_id, doc_vector in tfidf_vectors.items():
        score = cosine_similarity(query_vector, doc_vector)
        scores[doc_id] = score

    # Sort by score (highest first)
    ranked_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked_results
