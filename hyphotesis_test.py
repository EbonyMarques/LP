from nltk import FreqDist, word_tokenize
from statsmodels.stats import weightstats as stests
import rpy2
import csv

def appender_nices(row, word, n):
    global nices
    
    if len(nices) < n:
        if word in word_tokenize(row[6]) and row[5] == "Recommended":
            nices.append(row)

def appender_goods(row, word, n):
    global goods
    
    if len(goods) < n:
        if word in word_tokenize(row[6]) and row[5] == "Recommended":
            goods.append(row)

def counter(recommendation):
    global count
    
    if recommendation == "Not Recommended":
        count += 1

def word_counts(text, words):
    token = word_tokenize(text)
    counts = FreqDist(token)

    result = list(map(lambda x: counts[x] or 0, words))

    return result[0]

nices, goods, nices_counts, goods_counts = [], [], [], []
counts = 0

with open("steam_reviews.csv", encoding = "utf-8") as file:
    reader = csv.reader(file, delimiter = ";")
    reader = list(reader)
    reader.pop(0)

    list(map(lambda row: appender_nices(row[0].split(","), "nice", 1365), reader))
    list(map(lambda row: appender_goods(row[0].split(","), "good", 1365), reader))

for review in nices:
    nices_counts.append(word_counts(review[6], ["nice"]))

for review in goods:
    goods_counts.append(word_counts(review[6], ["good"]))

ztest, pval = stests.ztest(nices_counts, goods_counts)

a, b = 0, 0

for i in nices_counts:
    a += i

for i in goods_counts:
    b += i

print("H0: a/1365 = b/1365")
print("H1: a/1365 != b/1365")

if pval == 0.05:
    print("H0 is not rejected")

else:
    print("H0 is rejected")
