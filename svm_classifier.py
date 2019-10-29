from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import svm
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import precision_score

class SVM():
    def __init__(self, vectorizer):
        self.classifier = svm.SVC()
        self.reviews_test = None
        self.recommendations_test = None
        self.vectorizer = vectorizer
        self.model = None
        self.classifier_creator()
    
    def text_predictor(self, text):
        processed_text = self.vectorizer.text_vectorizer(text)
        return self.model.predict(processed_text)

    def classifier_creator(self):
        processed_reviews = self.vectorizer.vectorize()
        recommendations = self.vectorizer.recommendations
        hyper = {"C": [1.0, 2.0, 3.0],
                 "kernel": ["linear", "rbf", "sigmoid", "poly"],
                 "degree": [2, 3, 4],
                 "gamma": ["scale"]}
        reviews_train, self.reviews_test, recommendations_train, self.recommendations_test = train_test_split(processed_reviews, recommendations, test_size=0.2, random_state=0)
        classifier = GridSearchCV(self.classifier, hyper, cv = 5, n_jobs = 1, iid = False)
        classifier.fit(reviews_train, recommendations_train)
        self.model = classifier

    def accuracy_printer(self):
        predictor = self.model.predict(self.reviews_test)

        # SCORE
        print("Testing SVM/GridSearchCV classifier...")
        print("Accuracy: %.2f" % accuracy_score(self.recommendations_test, predictor))
        print("Precision: %.2f" % precision_score(self.recommendations_test, predictor, average="macro"))
        print("F-measure: %.2f" % f1_score(self.recommendations_test, predictor, average="macro"))

        # CONFUSION MATRIX
        # print("\nConfusion matrix")
        # print(confusion_matrix(labels_test, predictor, labels=[0, 1]))
