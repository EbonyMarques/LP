from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.feature_extraction.text import TfidfVectorizer

class Vectorizer():
    def __init__(self, reviews, recommendations):
        self.vectorizer = CountVectorizer()
        #self.vectorizer = TfidfVectorizer()
        self.reviews = reviews
        self.recommendations = recommendations
        self.fited_reviews = None
        self.vectorize()
    
    def vectorize(self):
        self.fited_reviews = self.vectorizer.fit_transform(self.reviews)

    def text_vectorizer(self, text):
        return self.vectorizer.transform([text])