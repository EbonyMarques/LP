from sklearn.feature_extraction.text import TfidfVectorizer
from vectorizer import Vectorizer
from processor import processor

class TFIDFVectorizer(Vectorizer):
    def __init__(self, reviews, recommendations, ngram_range = (1, 1)):
        self.vectorizer = TfidfVectorizer(ngram_range=ngram_range)
        self.reviews = reviews
        self.recommendations = recommendations
        self.vectorize()