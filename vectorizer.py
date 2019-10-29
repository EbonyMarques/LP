from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

class Vectorizer():
    def __init__(self, reviews, recommendations):
        self.vectorizer = CountVectorizer()
        #self.vectorizer = TfidfVectorizer()
        self.reviews = reviews
        self.recommendations = recommendations
    
    def vectorize(self):
        return self.vectorizer.fit_transform(self.reviews)

    def text_vectorizer(self, text):
        return self.vectorizer.transform([text])