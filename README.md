
---

## 🔑 Key Concepts Implemented

- Text preprocessing and tokenization
- Inverted index for efficient keyword lookup
- Term Frequency–Inverse Document Frequency (TF-IDF)
- Vector Space Model representation
- Cosine similarity for document ranking

---

## ⚙️ How It Works

1. Raw text documents are cleaned and tokenized.
2. An inverted index maps terms to the documents they appear in.
3. TF-IDF weights are computed for each document.
4. User queries are converted into TF-IDF vectors.
5. Cosine similarity is used to measure relevance between the query and each document.
6. Documents are ranked and returned based on similarity scores.

---

## ▶️ How to Run

```bash
python main.py
