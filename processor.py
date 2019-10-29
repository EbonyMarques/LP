from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

def processor(text):
    try:
        lemmatizer = WordNetLemmatizer()
        result = list(map(lambda i: re.sub("[^A-Za-z0]+", " ", i), [text]))
        result = list(map(lambda i: word_tokenize(i), result))
        result = list(map(lambda i: list(filter(lambda j: j not in stopwords.words("english"), i)), result))
        result = list(map(lambda i: list(map(lambda j: lemmatizer.lemmatize(j), i)), result))
        result = ' '.join(result[0])
        return result
    except:
        print("Atenção! Este texto não pôde ser processado: " + text + ".") #esse bloco try/except será retirado na versão final