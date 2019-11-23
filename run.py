from extractor import Extractor
from vectorizer import CountVectorizer, TFIDFVectorizer
from classifier import NaiveBayes, SVM
from util import plot_graphic, reviews_function, ThreadWithReturnValue, words_separation, set_reviews_to_wordcloud, predict_texts
from threading import Thread

extractor = Extractor()
reviews = extractor.reviews
recommendations = extractor.recommendations


vectorizer1 = CountVectorizer(reviews, recommendations)
vectorizer2 = CountVectorizer(reviews, recommendations, (1, 4))
vectorizer3 = TFIDFVectorizer(reviews, recommendations)
vectorizer4 = TFIDFVectorizer(reviews, recommendations, (1, 4))
classifier1 = NaiveBayes(vectorizer1, "data/naive_bayes_classifier_5000_1_1.pickle")
classifier2 = NaiveBayes(vectorizer2, "data/naive_bayes_classifier_5000_1_4.pickle")
classifier3 = SVM(vectorizer3, "data/svm_classifier_5000_1_1.pickle")
classifier4 = SVM(vectorizer4, "data/svm_classifier_5000_1_4.pickle")
result1 = classifier1.scorer()
result2 = classifier2.scorer()
result3 = classifier3.scorer()
result4 = classifier4.scorer()

#((accuracy, precision, fmeasure))
accuracy =[result3[0],result1[0],result4[0],result2[0]]
nomesClassifier = ["SVM(1,1)", "Naive(1,1)", "SVM(1,4)","Naive(1,4)"]
precision = [result3[1],result1[1],result4[1],result2[1]]
fmeasure = [result3[2],result1[2],result4[2],result2[2]]


thread1 = Thread(target=plot_graphic, args=["Accuracy", nomesClassifier, accuracy, "Algorithm", "Accuracy percentage", "graphs/accuracy.png"])
thread2 = Thread(target=plot_graphic, args=["Precision", nomesClassifier, precision, "Algorithm", "Precision percentage", "graphs/precision.png"])
#thread3 = Thread(target=plot_graphic, args=["Fmeasure", nomesClassifier, fmeasure, "Algorithm", "Fmeasure percentage", "graphs/fmeasure.png"])
thread1.start()
thread2.start()
#thread3.start()
thread1.join()
thread2.join()
#thread3.join()




namePP, valuesPP, namePN, valuesPN = words_separation(reviews)
nameN, valuesN, resultN = reviews_function(reviews[5000:])
nameP, valuesP, resultP = reviews_function(reviews[:4999])


'''#thread1 = Thread(target=plot_graphic, args=["Negative reviews' most frequent words (just in negative reviews)", namePN, valuesPN, "Word", "Occurrence", "graphs/frequent_words_just_negative_reviews.png"])
thread2 = Thread(target=plot_graphic, args=["Positive reviews' most frequent words (just in positive reviews)", namePP, valuesPP, "Word", "Occurrence", "graphs/frequent_words_just_positive_reviews.png"])
#thread3 = Thread(target=plot_graphic, args=["Negative reviews' most frequent words", nameN, valuesN, "Word", "Occurrence", "graphs/frequent_words_negative_reviews.png"])
thread4 = Thread(target=plot_graphic, args=["Positive reviews' most frequent words", nameP, valuesP, "Word", "Occurrence", "graphs/frequent_words_positive_reviews.png"])
#thread1.start()
thread2.start()
#thread3.start()
thread4.start()
#thread1.join()
thread2.join()
#thread3.join()
thread4.join()'''

"""
#plot_graphic("Precision", ["SVM(1,1)", "Naive(1,1)", "SVM(1,4)", "Naive(1,4)"], [classifier3.getPrecission(),classifier1.getPrecission(), classifier4.getPrecission(), classifier2.getPrecission()], "Algorithm", "Precision percentage")
# """

#set_reviews_to_wordcloud([reviews, reviews[:4999], reviews[:5000]])

predict_texts(True, classifier4)
