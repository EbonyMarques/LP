from extractor import Extractor
from count_vectorizer import CountVectorizer
from tfidf_vectorizer import TFIDFVectorizer
from naive_bayes_classifier import NaiveBayes
from svm_classifier import SVM

extractor = Extractor()
reviews = extractor.reviews
recommendations = extractor.recommendations

vectorizer1 = CountVectorizer(reviews, recommendations)
vectorizer2 = CountVectorizer(reviews, recommendations, (1, 4))
vectorizer3 = TFIDFVectorizer(reviews, recommendations)
vectorizer4 = TFIDFVectorizer(reviews, recommendations, (1, 4))

classifier1 = NaiveBayes(vectorizer1)
classifier2 = NaiveBayes(vectorizer2)
classifier3 = SVM(vectorizer3)
classifier4 = SVM(vectorizer4)

#classifier.accuracy_printer()
"""
stop = False

while(stop != True):
    text = str(input("Entre com algum texto para verificar ou 'sair' para encerrar.\n\n>>> "))

    if text.strip().lower() == "sair":
        stop = True
    else:
        message = "\nEsse texto é considerado"
        predicted = classifier.text_predictor(text.lower())
        message += (" positivo.\n") if int(predicted[0]) > 0 else (" negativo.\n")
        
        print(message)"""