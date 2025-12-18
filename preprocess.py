# to convert this into tokens we use preprocess text
import string
STOPWORDS = {
    "is","a","of","and","are","with"
}

def preprocess(text):
    """
    Converts raw text into a list of clean tokens
    """
    text = text.lower()
    text = text.translate(str.maketrans("", "",string.punctuation))
    words = text.split()
    token = [word for word in words if word not in STOPWORDS]
    return token