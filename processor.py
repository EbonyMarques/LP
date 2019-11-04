from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

def processor(text):
    stopwords_list = stopwords.words("english")
    words_to_remove = ["don't", "not", "is", "it's", "but"]
    list(map(lambda i: stopwords_list.remove(i), words_to_remove))
    
    try:
        result = text.replace("'", "")
        result = re.sub("\W", " ", str(result))
        result = re.sub("\s+[a-zA-Z]\s+", " ", result)
        result = list(map(lambda i: re.sub("[^A-Za-z0]+", " ", i), [result]))
        #result = re.sub("\s+", " ", result, flags=re.I)
        #result = re.sub("^b\s+", "", result)
        result = list(map(lambda i: word_tokenize(i), result))
        #print(result)
        result = list(map(lambda i: list(filter(lambda j: j not in stopwords_list, i)), result))
        #print(result)
        lemmatizer = WordNetLemmatizer()
        result = list(map(lambda i: list(map(lambda j: lemmatizer.lemmatize(j), i)), result))
        #print(result)
        result = " ".join(result[0])
        return result
        
    except:
        print("Atenção! Este texto não pôde ser processado: " + text + ".") #esse bloco try/except será retirado na versão final