from extractor import Extractor
from vectorizer import CountVectorizer, TFIDFVectorizer
from classifier import NaiveBayes, SVM
from util import reviews_function, ThreadWithReturnValue, words_separation, predict_texts
from graphic_util import plot_graphic
from threading import Thread
from time import *

extractor = Extractor()
reviews = extractor.reviews
recommendations = extractor.recommendations

vectorizer1 = TFIDFVectorizer(reviews, recommendations)
vectorizer2 = TFIDFVectorizer(reviews, recommendations, (1, 4))
vectorizer3 = TFIDFVectorizer(reviews, recommendations)
vectorizer4 = TFIDFVectorizer(reviews, recommendations, (1, 4))

times = []

time1 = [float(time())]
classifier3 = SVM(vectorizer3, "data/svm_classifier_5000_1_1.pickle")
time1.append(float(time()))
times.append(time1[1]-time1[0])

time2 = [float(time())]
classifier1 = NaiveBayes(vectorizer1, "data/naive_bayes_classifier_5000_1_1.pickle")
time2.append(float(time()))
times.append(time2[1]-time2[0])

time3 = [float(time())]
classifier4 = SVM(vectorizer4, "data/svm_classifier_5000_1_4.pickle")
time3.append(float(time()))
times.append(time3[1]-time3[0])

time4 = [float(time())]
classifier2 = NaiveBayes(vectorizer2, "data/naive_bayes_classifier_5000_1_4.pickle")
time4.append(float(time()))
times.append(time4[1]-time4[0])

print(times)

classifiers_names = ["SVM (1,1)", "Naive (1,1)", "SVM (1,4)","Naive (1,4)"]

thread13 = Thread(target=plot_graphic, args=["Train times", classifiers_names, times, "Algorithm (ngram_range)", "Seconds", "graphics/times.png"])
thread13.start()
thread13.join()

"""
result1 = classifier1.scorer()
result2 = classifier2.scorer()
result3 = classifier3.scorer()
result4 = classifier4.scorer()


accuracy = [result3[0], result1[0], result4[0], result2[0]]
precision = [result3[1], result1[1], result4[1], result2[1]]
fmeasure = [result3[2], result1[2], result4[2], result2[2]]
"""
"""
namePP, valuesPP, namePN, valuesPN = words_separation(reviews)
nameN, valuesN, resultN = reviews_function(reviews[5000:])
nameP, valuesP, resultP = reviews_function(reviews[:4999])
nameT, valuesT, resultT = reviews_function(reviews)
"""

#thread1 = Thread(target=plot_graphic, args=["Accuracy", classifiers_names, accuracy, "Algorithm (ngram_range)", "Percentage", "graphics/accuracy.png"])
#thread2 = Thread(target=plot_graphic, args=["Precision", classifiers_names, precision, "Algorithm (ngram_range)", "Percentage", "graphics/precision.png"])
#thread3 = Thread(target=plot_graphic, args=["F-measure", classifiers_names, fmeasure, "Algorithm (ngram_range)", "Percentage", "graphics/fmeasure.png"])
#thread4 = Thread(target=plot_graphic, args=["Negative reviews' most frequent words (just in negative reviews)", namePN, valuesPN, "Word", "Occurrence", "graphics/frequent_words_just_negative_reviews.png"])
#thread5 = Thread(target=plot_graphic, args=["Positive reviews' most frequent words (just in positive reviews)", namePP, valuesPP, "Word", "Occurrence", "graphics/frequent_words_just_positive_reviews.png"])
#thread6 = Thread(target=plot_graphic, args=["Negative reviews' most frequent words", nameN, valuesN, "Word", "Occurrence", "graphics/frequent_words_negative_reviews.png"])
#thread7 = Thread(target=plot_graphic, args=["Positive reviews' most frequent words", nameP, valuesP, "Word", "Occurrence", "graphics/frequent_words_positive_reviews.png"])
#thread8 = Thread(target=plot_graphic, args=["Most frequent words in positive and negative reviews", nameT, valuesT, "Word", "Occurrence", "graphics/frequent_words_positive_and_negative_reviews.png"])
"""
thread9 = Thread(target=plot_graphic, args=["Most frequent positive words in positive reviews", ["fun", "play", "like", "friend", "great", "good", "love", "recommend", "best"], [2590, 2491, 1585, 1514, 1383, 1377, 754, 711, 685], "Word", "Occurrence", "graphics/frequent_positive_words_positive_reviews.png"])
thread10 = Thread(target=plot_graphic, args=["Most frequent negative words in positive reviews", ["issue", "bug", "problem", "bad", "toxic", "hate", "negative", "disconnect", "difficult"], [749, 378, 361, 320, 240, 133, 116, 107, 107], "Word", "Occurrence", "graphics/frequent_negative_words_positive_reviews.png"])
thread11 = Thread(target=plot_graphic, args=["Most frequent negative words in negative reviews", ["hacker", "banned", "community", "ban", "bad", "issue", "cheater", "problem", "bug"], [773, 744, 660, 513, 433, 401, 319, 318, 305], "Word", "Occurrence", "graphics/frequent_negative_words_negative_reviews.png"])
thread12 = Thread(target=plot_graphic, args=["Most frequent positive words in negative reviews", ["fun", "good", "great", "fix", "friend", "support", "recommend", "well", "better"], [1137, 900, 648, 550, 505, 470, 446, 329, 312], "Word", "Occurrence", "graphics/frequent_positive_words_negative_reviews.png"])
"""
#thread1.start()
#thread1.join()
#thread2.start()
#thread2.join()
#thread3.start()
#thread3.join()
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
"""
thread9.start()
thread9.join()
thread10.start()
thread10.join()
thread11.start()
thread11.join()
thread12.start()
thread12.join()
"""
# set_reviews_to_wordcloud([reviews, reviews[:4999], reviews[5000:]])
#predict_texts(True, classifier4)