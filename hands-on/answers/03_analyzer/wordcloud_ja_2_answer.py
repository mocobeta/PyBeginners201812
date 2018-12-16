# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
from wordcloud import WordCloud
import sys


def create_analyzer(udic_file, udic_type):
    tokenizer = Tokenizer(udic_file, udic_type=udic_type, udic_enc='utf8') if udic_file else Tokenizer()
    char_filters = [RegexReplaceCharFilter('《.*?》', '')]
    token_filters = [POSKeepFilter(['名詞','形容詞','形容動詞','感動詞']), POSStopFilter(['名詞,非自立','名詞,代名詞']), ExtractAttributeFilter('base_form')]
    return Analyzer(char_filters, tokenizer, token_filters)

def split_text(src, out, udic_file='', udic_type='simpledic'):
    """
    src で渡されたファイルを読み，単語分割して out に書き出します。
    """
    a = create_analyzer(udic_file, udic_type)
    with open(src, encoding='utf8') as f1:
        with open(out, mode='w', encoding='utf8') as f2:
            for line in f1:
                tokens = list(a.analyze(line))
                f2.write('%s\n' % ' '.join(tokens))


def show_wordcloud(file):
    with open(file) as f:
        text = f.read()
        wordcloud = WordCloud(font_path='ipagp.ttf',background_color='white',width=1024,height=674).generate(text)
        image = wordcloud.to_image()
        image.show()

if __name__ == '__main__':
    src = sys.argv[1]
    udic_file = sys.argv[2] if len(sys.argv) > 2 else ''
    udic_type = sys.argv[3] if len(sys.argv) > 3 else 'simpledic'
    out = 'words.txt'
    split_text(src, out, udic_file, udic_type)
    show_wordcloud(out)