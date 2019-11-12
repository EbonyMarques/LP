import nltk
from nltk.probability import FreqDist

def tokenizer(reviews):
    tokens = nltk.tokenize.word_tokenize(' '.join(reviews))
    return FreqDist(tokens)