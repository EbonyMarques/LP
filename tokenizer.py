import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def tokenizer(reviews):
    tokens = nltk.tokenize.word_tokenize(' '.join(reviews))
    return FreqDist(tokens)

def filter_words(words):
    #return list(map(lambda i: list(filter(lambda j: j[0] not in stopwords.words('english'),i)), words))
    return list(filter(lambda i: i[0] not in stopwords.words('english'), words))

def remove_numbers(words):
    return list(filter(lambda i: i[0].isdigit() is False, words))
