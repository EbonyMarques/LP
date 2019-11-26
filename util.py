from nltk import tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
#from wordcloud import WordCloud, ImageColorGenerator
from time import time
#from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from threading import Thread

def tokenizer(reviews):
    tokens = tokenize.word_tokenize(' '.join(reviews))
    return FreqDist(tokens)

def filter_words(words):
    #return list(map(lambda i: list(filter(lambda j: j[0] not in stopwords.words('english'),i)), words))
    return list(filter(lambda i: i[0] not in stopwords.words('english'), words))

def remove_numbers(words):
    return list(filter(lambda i: i[0].isdigit() is False, words))

def reviews_function(reviews):
    freq_dist = tokenizer(reviews)
    words = freq_dist.most_common(20)
    result = remove_numbers(filter_words(words))
    name = list(map(lambda x: x[0], result))
    values = list(map(lambda x: x[1], result))
    return ((name, values, result))

def words(name1,name2, result):
    palavras = list(filter(lambda i: i[0] in list(filter(lambda j: j not in name1,name2)), result))
    name = list(map(lambda x: x[0], palavras))
    values = list(map(lambda x: x[1], palavras))
    return ((name, values))

def words_separation(reviews):
    nameP, valuesP, resultP = reviews_function(reviews[0:4999])
    nameN, valuesN, resultN = reviews_function(reviews[5000:])
    nameWP, valuesWP  = words(nameN,nameP,resultP)
    nameWN, valuesWN  = words(nameP,nameN,resultN)
    return ((nameWP, valuesWP, nameWN, valuesWN))

def set_reviews_to_wordcloud(args):
    list(map(lambda dataset: generate_cloud(tokenizer(dataset)), args))
"""
def generate_cloud(freq_dist):
    mask = np.array(Image.open("word_cloud/masks/mask-%s.png" % 'e'))
    gradient = np.array(Image.open("word_cloud/colors/gradient.jpg"))
    contour = 0
    print("Generating a word cloud image\n")
    wordcloud = WordCloud(width=1543, height=1560, mask=mask, background_color="white", contour_width=contour).generate_from_frequencies(freq_dist)
    wordcloud.recolor(color_func=ImageColorGenerator(gradient))
    wordcloud.to_file("word_cloud/steam%s.png" % str(int(time())))
"""
def plot_graphic(title, names, values, x_title, y_title, path):
    plt.figure(figsize=(15, 6))
    #plt.subplot(131)
    plt.bar(names, values)
    plt.suptitle(title)
    plt.xlabel(x_title, fontsize=15)
    plt.ylabel(y_title, fontsize=13)
    #plt.yticks([0.905, 0.910, 0.915, 0.920, 0.925, 0.930, 0.935, 0.940, 0.945, 0.950])
    plt.ylim(bottom=0.9)  # this line
    #plt.show()
    plt.savefig(path)
    #, 'Precisão SVM', 'Precisão Naive', 'F-measure SVM', 'F-measure Naive'

def processor(text):
    stopwords_list = stopwords.words("english")
    words_to_remove = ["don't", "not", "is", "it's", "but"]
    list(map(lambda i: stopwords_list.remove(i), words_to_remove))

    try:
        result = text.replace("'", "")
        result = re.sub("\W", " ", str(result))
        result = re.sub("\s+[a-zA-Z]\s+", " ", result)
        result = list(map(lambda i: re.sub("[^A-Za-z]+", " ", i), [result]))
        #result = re.sub("\s+", " ", result, flags=re.I)
        #result = re.sub("^b\s+", "", result)
        result = list(map(lambda i: word_tokenize(i), result))
        result = list(map(lambda i: list(filter(lambda j: j not in stopwords_list, i)), result))
        lemmatizer = WordNetLemmatizer()
        result = list(map(lambda i: list(map(lambda j: lemmatizer.lemmatize(j), i)), result))
        result = " ".join(result[0])
        return result

    except:
        print("Atenção! Este texto não pôde ser processado: " + text + ".") #esse bloco try/except será retirado na versão final

def predict_texts(initialize, classifier=None):
    stop = not initialize
    while(stop is False):
        text = str(input("Entre com algum texto para verificar ou 'sair' para encerrar.\n\n>>> "))

        if text.strip().lower() == "sair":
            stop = True

        else:
            message = "\nEsse texto é considerado"
            predicted = classifier.text_predictor(text)
            message += (" positivo.\n") if int(predicted[0]) > 0 else (" negativo.\n")
            print(message)

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        #print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return