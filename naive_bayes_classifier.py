from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import precision_score
from pickle import dump, load

class NaiveBayes():
    def __init__(self, vectorizer):
        self.vectorizer = vectorizer
        self.reviews_test = None
        self.recommendations_test = None
        self.model = None

        try:
            print("Trying load classifier...")
            self.classifier_loader()

        except:
            print("Load failed. Training...")
            self.classifier_creator()
            self.classifier_saver()

    def classifier_saver(self):
        with open("naive_bayes_classifier.pickle", "wb") as file:
            dump([self.reviews_test, self.recommendations_test, self.model], file)
            print("Classifier saved.\n")
        
    def classifier_loader(self):
        with open("naive_bayes_classifier.pickle", "rb") as file:
            self.reviews_test, self.recommendations_test, self.model = load(file)
            print("Classifier loaded.\n")
        
    def text_predictor(self, text):
        processed_text = self.vectorizer.text_vectorizer(text)
        return self.model.predict(processed_text)

    def classifier_creator(self):
        processed_reviews = self.vectorizer.fited_reviews
        recommendations = self.vectorizer.recommendations
        reviews_train, self.reviews_test, recommendations_train, self.recommendations_test = train_test_split(processed_reviews, recommendations, test_size=0.2, random_state=0)
        classifier = BernoulliNB()
        classifier.fit(reviews_train, recommendations_train)
        self.model = classifier

    def accuracy_printer(self):
        predictor = self.model.predict(self.reviews_test)
        print("Testing NaiveBayes/BernoulliNB classifier...")
        print("Accuracy: %.2f" % accuracy_score(self.recommendations_test, predictor))
        print("Precision: %.2f" % precision_score(self.recommendations_test, predictor, average="macro"))
        print("F-measure: %.2f\n" % f1_score(self.recommendations_test, predictor, average="macro"))