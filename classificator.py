from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
import csv

def train(records, vectorizer):
    reviews = [i[1] for i in records]
    recommendation = [int(i[0]) for i in records]
    reviews = vectorizer.fit_transform(reviews)
    return BernoulliNB().fit(reviews, recommendation)

def analyser(text):
    global classificator, vectorizer
    return classificator.predict(vectorizer.transform([text]))

with open("reviews.csv", encoding="utf-8") as file:
    reviews = csv.reader(file, delimiter=";")
    reviews = list(reviews)

vectorizer = CountVectorizer(binary = "true")
classificator = train(reviews, vectorizer)

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
