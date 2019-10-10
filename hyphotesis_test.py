from nltk import FreqDist, word_tokenize
from statsmodels.stats import weightstats
from numpy import average
import csv

first_word_counts, second_word_counts = [], []
first_word, second_word = "excellent", "trash"
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

first_average, second_average = average(first_word_counts), average(second_word_counts)

print("first = sum of all occurrences of %s in %s reviews" %(first_word, quantity))
print("second = sum of all occurrences of %s in %s reviews\n" %(second_word, quantity))

print("Type: %s" %(recommendationType))

print("\nH0: first/%s = second/%s"%(quantity, quantity))
print("H1: first/%s != second/%s\n"%(quantity, quantity))

print("first/%s = %f" %(quantity, first_average))
print("second/%s = %f" %(quantity, second_average))

if pval < 0.05:
    print("\nH0 is not rejected")

else:
    print("\nH0 is rejected")
