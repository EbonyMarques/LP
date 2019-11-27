import numpy as np
from time import time
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from util import tokenizer

def set_reviews_to_wordcloud(datasets):
    generate_csv_freqdist(False)
    list(map(lambda dataset: generate_cloud(tokenizer(dataset)), datasets))

def generate_cloud(freq_dist):
    mask = np.array(Image.open("graphics/word_cloud/masks/mask-%s.png" % 'd'))
    gradient = np.array(Image.open("graphics/word_cloud/colors/gradient.jpg"))
    contour = 0
    print("Generating a word cloud image\n")
    wordcloud = WordCloud(width=1543, height=1560, mask=mask, background_color="white", contour_width=contour).generate_from_frequencies(freq_dist)
    wordcloud.recolor(color_func=ImageColorGenerator(gradient))
    wordcloud.to_file("graphics/word_cloud/steam%s.png" % str(int(time())))

def generate_csv_freqdist(generate, index=0, datasets=[]):
    if generate:
        from operator import itemgetter
        fileNames = ['all', 'positives', 'negatives']
        arq = open('%s.csv' % fileNames[index], 'w')
        fq = tokenizer(datasets[index])
        arq.writelines(list(map(lambda tuple: tuple[0]+';'+ str(tuple[1]) + '\n', sorted(fq.items(), key=itemgetter(1), reverse=True))))
        arq.close()

