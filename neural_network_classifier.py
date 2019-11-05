from classifier import Classifier
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

class MLP(Classifier):
    def __init__(self, vectorizer):
        self.vectorizer = vectorizer
        self.file_path = "mlp_classifier_5000.pickle"
        self.name = "NeuralNetwork/MLP"

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
        classifier = MLPClassifier(solver = "lbfgs", alpha = 1e-5, hidden_layer_sizes = (70, ), random_state = 1, verbose = True)
        classifier.fit(reviews_train, recommendations_train)
        self.model = classifier