from extractor import Extractor
from vectorizer import Vectorizer
#from naive_bayes_classifier import NaiveBayes
from svm_classifier import SVM

extractor = Extractor()
reviews = extractor.reviews
recommendations = extractor.recommendations
vectorizer = Vectorizer(reviews, recommendations)
#classifier = NaiveBayes(vectorizer)
classifier = SVM(vectorizer)
classifier.accuracy_printer()

stop = False

while(stop != True):
    text = str(input("Entre com algum texto para verificar ou 'sair' para encerrar.\n\n>>> "))

    if text.strip().lower() == "sair":
        stop = True
    else:
        message = "\nEsse texto é considerado"
        predicted = classifier.text_predictor(text.lower())
        message += (" positivo.\n") if int(predicted[0]) > 0 else (" negativo.\n")
        
        print(message)