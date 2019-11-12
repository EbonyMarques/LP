from classifier import Classifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import svm

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
