from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from threading import Thread
import csv

def train(vectorizer, reviews, recommendations):
    return BernoulliNB().fit(vectorizer.fit_transform(reviews), recommendations)

def analyser(text):
    global classificator, vectorizer
    
    predicted = classificator.predict(vectorizer.transform([text]))
    return predicted

def listCreator(source, index):
    global reviews, recommendations
    
    if index == 1:
        reviews = list(map(lambda item: item[index], source))
    else:
        recommendations = list(map(lambda item: item[index], source))

with open("reviews.csv", encoding="utf-8") as file:
    data = csv.reader(file, delimiter=";")
    data = list(data)

reviews, recommendations = [], []
vectorizer = CountVectorizer()

t1, t2 = Thread(target=listCreator,args=[data, 0]), Thread(target=listCreator,args=[data, 1])
t1.start(); t2.start()
t1.join(); t2.join()

classificator = train(vectorizer, reviews, recommendations)

stop = False

while(stop == False):
    operation = str(input("Entre com algum texto para verificar ou 'sair' para encerrar.\n\n>>> "))

    if operation.strip().lower() == "sair":
        stop = True
    else:
        message = "\nEsse texto é considerado"
        predicted = analyser(operation)
        message += (" positivo.\n") if int(predicted[0]) > 0 else (" negativo.\n")
        print(message)
