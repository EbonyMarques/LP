from nltk import FreqDist, word_tokenize
import csv

words = ["excellent", "terrible", "trash"]
counts_total = [0, 0, 0]

def word_counts(text, words):
    global counts_total
    
    token = word_tokenize(text)
    counts = FreqDist(token)

    result = list(map(lambda x: counts[x] or 0, words))

    counts_total[0] += result[0]
    counts_total[1] += result[1]
    counts_total[2] += result[2]

with open("steam_reviews.csv", encoding = "utf-8") as file:
    reader = csv.reader(file, delimiter = ";")

    reader = list(reader)
    reader.pop(0)

    list(map(lambda row: word_counts(row[0].split(",")[6], words), reader))

    print("Ocorrências de '%s': %i\nOcorrências de '%s': %i\nOcorrências de '%s': %i" %(words[0], counts_total[0], words[1], counts_total[1], words[2], counts_total[2]))
