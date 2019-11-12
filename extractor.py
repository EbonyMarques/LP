import nltk
from nltk.probability import FreqDist
from processor import processor
from pickle import dump, load
from csv import reader


class Extractor():
    def __init__(self):
        self.reviews = []
        self.recommendations = []
        self.freqDist = None

        try:
            print("Trying load data...")
            self.data_loader()

        except:
            print("Load failed. Extracting...")
            self.extractor()
            self.data_saver()

    def data_saver(self):
        with open("processed_data_5000.pickle", "wb") as file:
            dump([self.reviews, self.recommendations], file)
            print("Data saved.\n")

    def data_loader(self):
        with open("processed_data_5000.pickle", "rb") as file:
            self.reviews, self.recommendations = load(file)
            self.tokenizer(self.reviews)
            print("Data loaded.\n")

    def review_appender(self, text):
        self.reviews.append(text)

    def recommendation_appender(self, value):
        self.recommendations.append(value)

    def data_processor(self, loaded_data):
        processed_data = list(map(lambda i: processor(i[1].lower()), loaded_data))
        self.tokenizer(processed_data)
        list(map(lambda i: self.review_appender(i), processed_data))
        list(map(lambda i: self.recommendation_appender(i[0]), loaded_data))

    def data_extractor(self, file_name):
        with open(file_name) as file:
            loaded_data = reader(file, delimiter = ";")
            return list(loaded_data)

    def extractor(self):
        #positive_data = self.data_extractor("positive_reviews.csv")
        positive_data = self.data_extractor("positive_random_reviews_part_2000.csv")
        #negative_data = self.data_extractor("negative_reviews.csv")
        negative_data = self.data_extractor("negative_random_reviews_part_2000.csv")
        self.data_processor(positive_data)
        self.data_processor(negative_data)

    def tokenizer(self, reviews):
        tokens = nltk.tokenize.word_tokenize(' '.join(reviews))
        self.freqDist = FreqDist(tokens)