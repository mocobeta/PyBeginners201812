#!/bin/bash

from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import sys

def split_text(src, out):
    """
    src で渡されたファイルを読み，単語分割して out に書き出します。
    """
    t = Tokenizer()
    with open(src, encoding='utf8') as f1:
        with open(out, mode='w', encoding='utf8') as f2:
            for line in f1:
                tokens = t.tokenize(line, wakati=True)
                f2.write('%s\n' % ' '.join(tokens))


def show_wordcloud(file):
    with open(file) as f:
        text = f.read()
        wordcloud = WordCloud(font_path='ipagp.ttf',background_color='white',width=1024,height=674).generate(text)
        image = wordcloud.to_image()
        image.show()

if __name__ == '__main__':
    src = sys.argv[1]
    out = 'words.txt'
    split_text(src, out)
    show_wordcloud(out)