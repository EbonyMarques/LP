#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from processor import processor

class Vectorizer():
    def __init__(self):
        #self.vectorizer = CountVectorizer(ngram_range=(1, 4))
        #self.vectorizer = TfidfVectorizer(ngram_range)
        self.vectorizer = None
        self.reviews = None
        self.recommendations = None
        self.fited_reviews = None
        #self.vectorize()
        #print(self.vectorizer.vocabulary_)
    
    def vectorize(self):
        self.fited_reviews = self.vectorizer.fit_transform(self.reviews)

    def text_vectorizer(self, text):
        return self.vectorizer.transform([text.lower().replace("'", "")])