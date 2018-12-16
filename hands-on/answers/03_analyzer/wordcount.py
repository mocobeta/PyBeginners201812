# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
import sys

MAX_WORDS = 20

def wc(file, pos=''):
    with open(file, encoding='utf8') as f:
        if not pos:
            token_filters = [TokenCountFilter(sorted=True)]
        else:
            token_filters = [POSKeepFilter(pos), TokenCountFilter(sorted=True,att='base_form')]
        a = Analyzer(tokenizer=Tokenizer(), token_filters=token_filters)
        text = f.read()
        return list(a.analyze(text))[:MAX_WORDS]

if __name__ == '__main__':
    file = sys.argv[1]
    pos = sys.argv[2] if len(sys.argv) > 2 else ''
    counts = wc(file, pos)
    for k, v in counts:
        print('%s\t%d' % (k, v))