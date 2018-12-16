#!/bin/bash

from wordcloud import WordCloud
import sys

def show_wordcloud(file):
    with open(file, encoding='utf8') as f:
        text = f.read()
        wordcloud = WordCloud(font_path='ipagp.ttf',background_color='white',width=1024,height=674).generate(text)
        image = wordcloud.to_image()
        image.show()

if __name__ == '__main__':
    file = sys.argv[1]
    show_wordcloud(file)
