from nltk import FreqDist, word_tokenize
from statsmodels.stats import weightstats
import csv

first_word_counts, second_word_counts = [], []
first_word, second_word = "nice", "good"
quantity, recommendationType = 1365, "Recommended"

def first_word_appender(row):
    global first_word_counts
    
    if len(first_word_counts) < quantity:
        if row[5] == recommendationType and first_word in word_tokenize(row[6]):
            first_word_counts.append(word_counts(row[6], [first_word]))
            
def second_word_appender(row):
    global second_word_counts
    
    if len(second_word_counts) < quantity:
        if row[5] == recommendationType and second_word in word_tokenize(row[6]):
            second_word_counts.append(word_counts(row[6], [second_word]))

def word_counts(text, words):
    counts = FreqDist(word_tokenize(text))

    return list(map(lambda x: counts[x] or 0, words))[0]

with open("steam_reviews.csv", encoding = "utf-8") as file:
    reader = csv.reader(file, delimiter = ";")
    reader = list(reader)
    reader.pop(0)

    list(map(lambda row: first_word_appender(row[0].split(",")), reader))
    list(map(lambda row: second_word_appender(row[0].split(",")), reader))

ztest, pval = weightstats.ztest(first_word_counts, second_word_counts)
"""
a, b = 0, 0

for i in first_word_counts:
    a += i

for i in second_word_counts:
    b += i

print("H0: a/4350 = b/4350")
print("H1: a/4350 != b/4350\n")

print("a/4350 = " + str(a/1365))
print("b/4350 = " + str(b/1365) + "\n")
"""
if pval < 0.05:
    print("H0 is not rejected")

else:
    print("H0 is rejected")
