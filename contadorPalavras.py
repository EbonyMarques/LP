from nltk import FreqDist, word_tokenize
import csv

greats, bads, nices = 0, 0, 0
words = {}

def word_counts(text, words):
    global greats, bads, nices
    
    token = word_tokenize(text)
    counts = FreqDist(token)

    test = list(map(lambda x: counts[x] or 0, words))

    greats += test[0]
    bads += test[1]
    nices += test[2]

with open("steam_reviews.csv", encoding = "utf-8") as file:
    reader = csv.reader(file, delimiter = ";")

    reader = list(reader)
    reader.pop(0)

    list(map(lambda row: word_counts(row[0].split(",")[6], ["great", "bad", "nice"]), reader))

    print("Ocorrências da palavra 'great': %i\nOcorrências da palavra 'bad': %i\nOcorrências da palavra 'nice': %i" %(greats, bads, nices))
