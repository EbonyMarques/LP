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

def reviews_function(reviews):
    freq_dist = tokenizer(reviews)
    words = freq_dist.most_common(20)
    result = remove_numbers(filter_words(words))
    name = list(map(lambda x: x[0], result))
    values = list(map(lambda x: x[1], result))
    return ((name, values, result))

def words(name1,name2, result):
    palavras = list(filter(lambda i: i[0] in list(filter(lambda j: j not in name1,name2)), result))
    name = list(map(lambda x: x[0], palavras))
    values = list(map(lambda x: x[1], palavras))
    return ((name, values))

def words_separation(reviews):
    nameP, valuesP, resultP = reviews_function(reviews[0:4999])
    nameN, valuesN, resultN = reviews_function(reviews[5000:])
    nameWP, valuesWP  = words(nameN,nameP,resultP)
    nameWN, valuesWN  = words(nameP,nameN,resultN)
    return ((nameWP, valuesWP, nameWN, valuesWN))
