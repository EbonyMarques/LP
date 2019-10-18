from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from langdetect import detect
import csv

reviews, quantity, recommendation = [], 1000, "Recommended"

def appender(row):
    global reviews
    
    if len(reviews) < quantity:
        if row[5] == recommendation:
            if len(str(row[6])) > 250 and len(str(row[6])) < 500:
                if int(row[3]) > 100:
                    try:
                        if detect(str(row[6])) == "en":
                            if recommendation == "Recommended":
                                reviews.append([1, str(row[6])])
                            else:
                                reviews.append([0, str(row[6])])
                    except:
                        pass

with open("steam_reviews.csv", encoding = "utf-8") as file:
    reader = csv.reader(file, delimiter = ";")
    reader = list(reader)
    reader.pop(0)

    list(map(lambda row: appender(row[0].split(",")), reader))

    for i in reviews:
        print(i[1])
        input()
