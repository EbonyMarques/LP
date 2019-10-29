from processor import processor
from csv import reader

class Extractor():
    def __init__(self):
        self.reviews = []
        self.recommendations = []
        self.extractor()

    def review_appender(self, text):
        self.reviews.append(text)

    def recommendation_appender(self, value):
        self.recommendations.append(value)

    def data_processor(self, loaded_data):
            processed_data = list(map(lambda i: processor(i[1]), loaded_data))
            list(map(lambda i: self.review_appender(i), processed_data))
            list(map(lambda i: self.recommendation_appender(i[0]), loaded_data))

    def data_loader(self, file_name):
        with open(file_name) as file:
            loaded_data = reader(file, delimiter = ";")
            return list(loaded_data)

    def extractor(self):
        #positive_data = self.data_loader("positive_reviews.csv")
        positive_data = self.data_loader("positive_random_reviews_part_2000.csv")
        #negative_data = self.data_loader("negative_reviews.csv")
        negative_data = self.data_loader("negative_random_reviews_part_2000.csv")
        self.data_processor(positive_data)
        self.data_processor(negative_data)