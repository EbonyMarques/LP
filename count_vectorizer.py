from sklearn.feature_extraction.text import CountVectorizer as CountVec
from vectorizer import Vectorizer
from processor import processor

class CountVectorizer(Vectorizer):
    def __init__(self, reviews, recommendations, ngram_range = (1, 1)):
        self.vectorizer = CountVec(ngram_range=ngram_range)
        self.reviews = reviews
        self.recommendations = recommendations
        self.vectorize()