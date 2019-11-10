from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import precision_score
from pickle import dump, load

class Classifier():
    def __init__(self):
        self.vectorizer = None
        self.reviews_test = None
        self.recommendations_test = None
        self.classifier = None
        self.model = None
        self.file_path = None
        self.name = None
    
    def classifier_saver(self):
        with open(self.file_path, "wb") as file:
            dump([self.reviews_test, self.recommendations_test, self.model], file)
            print("Classifier saved.\n")

    def classifier_loader(self):
        with open(self.file_path, "rb") as file:
            self.reviews_test, self.recommendations_test, self.model = load(file)
            print("Classifier loaded.\n")

    def text_predictor(self, text):
        processed_text = self.vectorizer.text_vectorizer(text)
        return self.model.predict(processed_text)

    def accuracy_printer(self):
        predictor = self.model.predict(self.reviews_test)
        print("Testing", self.name, "classifier...")
        print("Accuracy: %.4f" % accuracy_score(self.recommendations_test, predictor))
        print("Precision: %.4f" % precision_score(self.recommendations_test, predictor, average="macro"))
        print("F-measure: %.4f\n" % f1_score(self.recommendations_test, predictor, average="macro"))

    def getAccuracy(self):
        predictor = self.model.predict(self.reviews_test)
        return accuracy_score(self.recommendations_test, predictor)

    def getPrecission(self):
        predictor = self.model.predict(self.reviews_test)
        return precision_score(self.recommendations_test, predictor, average="macro")

    def getFmeasure(self):
        predictor = self.model.predict(self.reviews_test)
        return f1_score(self.recommendations_test, predictor, average="macro")
