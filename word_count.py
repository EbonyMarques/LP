#!/usr/bin/env python

from wordcloud import WordCloud
from PIL import Image
import numpy as np

def cloud(vectorize):
    mask = np.array(Image.open("mask.png"))
    # mask = None
    print('Generate a word cloud image')
    wordcloud = WordCloud(width=1543, height=1560, mask=mask, background_color = 'white').generate_from_frequencies(vectorize)
    wordcloud.to_file("steam.png")
