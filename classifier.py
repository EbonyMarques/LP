from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
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
        self.predictor = None

    def predictor_definer(self):
        self.predictor = self.model.predict(self.reviews_test)

    def text_predictor(self, text):
        processed_text = self.vectorizer.text_vectorizer(text)
        return self.model.predict(processed_text)  

    def scorer(self):
        accuracy = accuracy_score(self.recommendations_test, self.predictor)
        precision = precision_score(self.recommendations_test, self.predictor, average="macro")
        fmeasure = f1_score(self.recommendations_test, self.predictor, average="macro")
        return ((accuracy, precision, fmeasure))

    def classifier_saver(self):
        with open(self.file_path, "wb") as file:
            dump([self.reviews_test, self.recommendations_test, self.model], file)
            print("Classifier saved.\n")

    def classifier_loader(self):
        with open(self.file_path, "rb") as file:
            self.reviews_test, self.recommendations_test, self.model = load(file)
            self.predictor_definer()
            print("Classifier loaded.\n")

class NaiveBayes(Classifier):
    def __init__(self, vectorizer, file_path):
        self.vectorizer = vectorizer
        self.file_path = file_path
        self.name = "NaiveBayes/MultinomialNB"
        
        try:
            print("Trying load classifier...")
            self.classifier_loader()

        except:
            print("Load failed. Training...")
            self.classifier_creator()
            self.classifier_saver()

    def classifier_creator(self):
        processed_reviews = self.vectorizer.fited_reviews
        recommendations = self.vectorizer.recommendations
        reviews_train, self.reviews_test, recommendations_train, self.recommendations_test = train_test_split(processed_reviews, recommendations, test_size=0.2, random_state=0)
        classifier = MultinomialNB()
        classifier.fit(reviews_train, recommendations_train)
        self.model = classifier

class SVM(Classifier):
    def __init__(self, vectorizer, file_path):
        self.vectorizer = vectorizer
        self.classifier = svm.SVC()
        self.file_path = file_path
        self.name = "SVM/GridSearchCV"

        try:
            print("Trying load classifier...")
            self.classifier_loader()

        except:
            print("Load failed. Training...")
            self.classifier_creator()
            self.predictor_definer()
            self.classifier_saver()

    def classifier_creator(self):
        processed_reviews = self.vectorizer.fited_reviews
        recommendations = self.vectorizer.recommendations
        hyper = {"C": [1.0, 2.0, 3.0],
                 "kernel": ["linear", "rbf", "sigmoid", "poly"],
                 "degree": [2, 3, 4],
                 "gamma": ["scale"]}
        reviews_train, self.reviews_test, recommendations_train, self.recommendations_test = train_test_split(processed_reviews, recommendations, test_size=0.2, random_state=0)
        classifier = GridSearchCV(self.classifier, hyper, cv = 5, n_jobs = 1, iid = False)
        classifier.fit(reviews_train, recommendations_train)
        self.model = classifier
