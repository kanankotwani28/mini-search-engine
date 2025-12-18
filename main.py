from index import build_inverted_index
from index import build_inverted_index
from tfdf import compute_tfidf

index, documents = build_inverted_index("documents")

print("Inverted Index:")
for word, docs in index.items():
    print(word, "->", docs)

index, documents = build_inverted_index("documents")
tfidf_vectors,idf = compute_tfidf(documents, index)

print("TF-IDF Vectors:\n")
for doc, vector in tfidf_vectors.items():
    print(doc)
    for word, score in vector.items():
        print(f"  {word}: {score:.4f}")
    print()

from index import build_inverted_index
from tfdf import compute_tfidf
from search import search

# Build index and vectors
inverted_index, documents = build_inverted_index("documents")
tfidf_vectors, idf = compute_tfidf(documents, inverted_index)

# Search
query = input("Enter search query: ")
results = search(query, tfidf_vectors, idf)

print("\nSearch Results:")
for doc, score in results:
    if score > 0:
        print(f"{doc} -> score: {score:.4f}")
