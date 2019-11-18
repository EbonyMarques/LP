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

def reviews_positive(reviews):
    freq_distP = tokenizer(reviews[0:4999])
    wordsP = freq_distP.most_common(20)
    resultP = remove_numbers(filter_words(wordsP))
    nameP = list(map(lambda x: x[0], resultP))
    valuesP = list(map(lambda x: x[1], resultP))
    return ((nameP, valuesP, resultP))

def reviews_negative(reviews):
    freq_distN = tokenizer(reviews[5000:])
    wordsN = freq_distN.most_common(20)
    resultN = remove_numbers(filter_words(wordsN))
    nameN = list(map(lambda x: x[0], resultN))
    valuesN = list(map(lambda x: x[1], resultN))
    return ((nameN, valuesN, resultN))

def words_separation(reviews):
    nameP, valuesP, resultP = reviews_positive(reviews)
    nameN, valuesN, resultN = reviews_negative(reviews)
    palavrasPos = list(filter(lambda i: i[0] in list(filter(lambda j: j not in nameN,nameP)), resultP))
    namePP = list(map(lambda x: x[0], palavrasPos))
    valuesPP = list(map(lambda x: x[1], palavrasPos))
    palavrasNeg = list(filter(lambda i: i[0] in list(filter(lambda j: j not in nameP,nameN)), resultN))
    namePN = list(map(lambda x: x[0], palavrasNeg))
    valuesPN = list(map(lambda x: x[1], palavrasNeg))
    return ((namePP, valuesPP, namePN, valuesPN))