from extractor import Extractor
from tokenizer import tokenizer, filter_words,remove_numbers, reviews_positive, reviews_negative, words_separation
from count_vectorizer import CountVectorizer
from tfidf_vectorizer import TFIDFVectorizer
from naive_bayes_classifier import NaiveBayes
from svm_classifier import SVM
#from plot_graphic import plot_graphic
#from word_count import cloud

extractor = Extractor()
reviews = extractor.reviews
recommendations = extractor.recommendations

vectorizer1 = CountVectorizer(reviews, recommendations)
vectorizer2 = CountVectorizer(reviews, recommendations, (1, 4))
vectorizer3 = TFIDFVectorizer(reviews, recommendations)
vectorizer4 = TFIDFVectorizer(reviews, recommendations, (1, 4))

classifier1 = NaiveBayes(vectorizer1, "naive_bayes_classifier_5000_1_1.pickle")
classifier2 = NaiveBayes(vectorizer2, "naive_bayes_classifier_5000_1_4.pickle")
classifier3 = SVM(vectorizer3,"svm_classifier_5000_1_1.pickle")
classifier4 = SVM(vectorizer4, "svm_classifier_5000_1_4.pickle")

print("Naive 1-1")
classifier1.accuracy_printer()
print("Naive 1-4")
classifier2.accuracy_printer()
print("SVM 1-1")
classifier3.accuracy_printer()
print("SVM 1-4")
classifier4.accuracy_printer()

#freq_dist = tokenizer(reviews)
#nameN, valuesN, resultN = reviews_negative(reviews)
#namePP, valuesPP, namePN, valuesPN = words_separation(reviews)

#plot_graphic("Negative words", namePN, valuesPN)
#plot_graphic("Positive words", namePP, valuesPP)
#plot_graphic("Negative reviews' words", nameN, valuesN)
#plot_graphic("F-measure", ["SVM(1,1)", "Naive(1,1)", "SVM(1,4)", "Naive(1,4)"], [classifier3.getFmeasure(),classifier1.getFmeasure(), classifier4.getFmeasure(), classifier2.getFmeasure()])
#cloud(extractor.freq_dist)

"""

stop = False

while(stop is not True):
    text = str(input("Entre com algum texto para verificar ou 'sair' para encerrar.\n\n>>> "))

    if text.strip().lower() == "sair":
        stop = True
    else:
        message = "\nEsse texto é considerado"
        predicted = classifier.text_predictor(text.lower())
        message += (" positivo.\n") if int(predicted[0]) > 0 else (" negativo.\n")
        
        print(message)"""
