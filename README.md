# Mini Search Engine with TF-IDF Ranking

## 📌 Project Overview

This project implements a mini search engine from scratch using classical information retrieval techniques.  
It indexes a collection of text documents and returns ranked search results based on query relevance.

The goal of this project is to demonstrate a clear understanding of core search engine concepts rather than building a large-scale production system.

---

## 🏗️ Architecture

Documents
↓
Text Preprocessing
↓
Inverted Index
↓
TF-IDF Vectorization
↓
Cosine Similarity
↓
Ranked Search Results

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
