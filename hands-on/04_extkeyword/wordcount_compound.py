# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
import sys

def wc(file):
    with open(file, encoding='utf8') as f:
        token_filters = [CompoundNounFilter(), POSKeepFilter('名詞,複合'), TokenCountFilter(sorted=True)]
        a = Analyzer(tokenizer=Tokenizer(), token_filters=token_filters)
        text = f.read()
        return list(a.analyze(text))

if __name__ == '__main__':
    file = sys.argv[1]
    counts = wc(file)
    for k, v in counts:
        print('%s\t%d' % (k, v))