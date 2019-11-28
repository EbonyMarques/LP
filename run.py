from extractor import Extractor
from vectorizer import CountVectorizer, TFIDFVectorizer
from classifier import NaiveBayes, SVM
from util import reviews_function, ThreadWithReturnValue, words_separation, predict_texts
from graphic_util import plot_graphic
from threading import Thread

extractor = Extractor()
reviews = extractor.reviews
recommendations = extractor.recommendations

vectorizer1 = TFIDFVectorizer(reviews, recommendations)
vectorizer2 = TFIDFVectorizer(reviews, recommendations, (1, 4))
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

classifiers_names = ["SVM (1,1)", "Naive (1,1)", "SVM (1,4)","Naive (1,4)"]
accuracy =[result3[0], result1[0], result4[0], result2[0]]
precision = [result3[1], result1[1], result4[1], result2[1]]
fmeasure = [result3[2], result1[2], result4[2], result2[2]]

"""
namePP, valuesPP, namePN, valuesPN = words_separation(reviews)
nameN, valuesN, resultN = reviews_function(reviews[5000:])
nameP, valuesP, resultP = reviews_function(reviews[:4999])
nameT, valuesT, resultT = reviews_function(reviews)
"""

#thread1 = Thread(target=plot_graphic, args=["Accuracy", classifiers_names, accuracy, "Algorithm (ngram_range)", "Percentage", "graphics/accuracy.png"])
#thread2 = Thread(target=plot_graphic, args=["Precision", classifiers_names, precision, "Algorithm (ngram_range)", "Percentage", "graphics/precision.png"])
thread3 = Thread(target=plot_graphic, args=["F-measure", classifiers_names, fmeasure, "Algorithm (ngram_range)", "Percentage", "graphics/fmeasure.png"])
#thread4 = Thread(target=plot_graphic, args=["Negative reviews' most frequent words (just in negative reviews)", namePN, valuesPN, "Word", "Occurrence", "graphics/frequent_words_just_negative_reviews.png"])
#thread5 = Thread(target=plot_graphic, args=["Positive reviews' most frequent words (just in positive reviews)", namePP, valuesPP, "Word", "Occurrence", "graphics/frequent_words_just_positive_reviews.png"])
#thread6 = Thread(target=plot_graphic, args=["Negative reviews' most frequent words", nameN, valuesN, "Word", "Occurrence", "graphics/frequent_words_negative_reviews.png"])
#thread7 = Thread(target=plot_graphic, args=["Positive reviews' most frequent words", nameP, valuesP, "Word", "Occurrence", "graphics/frequent_words_positive_reviews.png"])
#thread8 = Thread(target=plot_graphic, args=["Most frequent words in positive and negative reviews", nameT, valuesT, "Word", "Occurrence", "graphics/frequent_words_positive_and_negative_reviews.png"])

#thread1.start()
#thread1.join()
#thread2.start()
#thread2.join()
thread3.start()
thread3.join()
#thread4.start()
#thread4.join()
#thread5.start()
#thread5.join()
#thread6.start()
#thread6.join()
#thread7.start()
#thread7.join()
#thread8.start()
#thread8.join()

# set_reviews_to_wordcloud([reviews, reviews[:4999], reviews[5000:]])
predict_texts(True, classifier4)