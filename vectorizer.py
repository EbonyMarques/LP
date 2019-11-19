from sklearn.feature_extraction.text import CountVectorizer as cv
from sklearn.feature_extraction.text import TfidfVectorizer as tv
from util import processor

class Vectorizer():
    def __init__(self):
        self.vectorizer = None
        self.reviews = None
        self.recommendations = None
        self.fited_reviews = None

    def text_vectorizer(self, text):
        return self.vectorizer.transform([text.lower().replace("'", "")])
    
    def vectorize(self):
        self.fited_reviews = self.vectorizer.fit_transform(self.reviews)

class CountVectorizer(Vectorizer):
    def __init__(self, reviews, recommendations, ngram_range = (1, 1)):
        self.vectorizer = cv(ngram_range=ngram_range)
        self.reviews = reviews
        self.recommendations = recommendations
        self.vectorize()

class TFIDFVectorizer(Vectorizer):
    def __init__(self, reviews, recommendations, ngram_range = (1, 1)):
        self.vectorizer = tv(ngram_range=ngram_range)
        self.reviews = reviews
        self.recommendations = recommendations
        self.vectorize()