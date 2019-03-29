from PIL import Image
from os import path
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import os
import random

# Color taken from the 1floridaadrc website
CONTOUR_COLOR = "#814397"

def main():
    mask = np.array(Image.open("brain-mask.png"))
    text = open("keywords.txt").read()
    text.replace(";", " ")

    wc = WordCloud(max_words=1000, mask=mask, margin=2, random_state=1, background_color="white",
                   contour_color=CONTOUR_COLOR, contour_width=3, width=1920, height=1515)
    wc.generate(text)
    wc.to_file('wordcloud.png')
    plt.title("ADRC Publication Wordcloud")
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
