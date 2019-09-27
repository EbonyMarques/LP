from nltk import FreqDist, word_tokenize
from statsmodels.stats import weightstats
from numpy import average
import csv

reviews, first_word_counts, second_word_counts = [], [], []
first_word, second_word, n, recommendation = "nice", "good", 4350, "Recommended"

def appender(row, recommendation, amount):
    global reviews

    if len(reviews) < amount:
        if recommendation == "":
            reviews.append(row)

        elif recommendation == row[5]:
            reviews.append(row)

def first_word_counter(text, word):
    global first_word_counts

    first_word_counts.append(word_counts(text, [word]))
            
def second_word_counter(text, word):
    global second_word_counts

    second_word_counts.append(word_counts(text, [word]))

def word_counts(text, words):
    token = word_tokenize(text)
    counts = FreqDist(token)

    result = list(map(lambda x: counts[x] or 0, words))

    return result[0]

with open("steam_reviews.csv", encoding = "utf-8") as file:
    reader = csv.reader(file, delimiter = ";")
    reader = list(reader)
    reader.pop(0)

    list(map(lambda row: appender(row[0].split(","), recommendation, n), reader))

    for i in reviews:
        first_word_counter(i[6], first_word)
        second_word_counter(i[6], second_word)

ztest, pval = weightstats.ztest(first_word_counts, second_word_counts)

a, b = average(first_word_counts), average(second_word_counts)

print("a = sum of all occurrences of %s in %s reviews" %(first_word, n))
print("b = sum of all occurrences of %s in %s reviews\n" %(second_word, n))

print("Recommendation type: %s" %(recommendation))

print("\nH0: a/%s != b/%s"%(n, n))
print("H1: a/%s = b/%s\n"%(n, n))

print("a/%s = %f" %(n, a))
print("b/%s = %f" %(n, b))

if pval < 0.05:
    print("\nH0 is not rejected")

else:
    print("\nH0 is rejected")
