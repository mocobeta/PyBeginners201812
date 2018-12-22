# BoW, TFIDF with gensim

## 準備

gensim をインストールしてください。

```
(venv) 04_extkeyword$ pip install gensim
```

## gensim ことはじめ

**ハンズオン課題 4-2**

好きなインタプリタを立ち上げて，以下実行してください。`## write your code ##` という箇所は，自分で埋めてください。

### テキストの読み込みと分割

`joel_gtd.txt` を読み込み，改行コード `\n` で split して `docs` 変数に格納する。

```
In [1]: with open('joel_gtd.txt') as f:
   ...:     data = f.read()
   ...:
In [2]: docs = data.split('\n')
In [3]: docs
Out[3]:
['下っ端でも何かを成し遂げる方法',
...
```

### トークナイズ

`docs` の各行を形態素解析して，単語のリストのリストに変換して `texts` 変数に格納する。

```
In [7]: from janome.tokenizer import Tokenizer
In [8]: t = Tokenizer()
In [11]: texts = ## write your code ##
In [15]: texts[0]
Out[15]: ['下っ端', 'で', 'も', '何', 'か', 'を', '成し遂げる', '方法']
```

### Dictionary 作成

`texts` から，gensim の Dictionary を構築して `dictionary` 変数に格納する。

チュートリアル: https://radimrehurek.com/gensim/tut1.html

```
In [17]: from gensim import corpora, models
In [18]: dictionary = corpora.Dictionary(texts)
In [22]: dictionary.token2id
Out[21]:
{'か': 0,
 'で': 1,
 'も': 2,
 'を': 3,
 '下っ端': 4,
 '何': 5,
 ...
```

### BoW 化と Corpus 作成

構築した `dictionary` を使って，`texts` を文書ベクトル (Bag of Words) に変換し，MmCorpus としてシリアライズする。

```
In [22]: corpus = ## write your code ##
In [23]: corpora.MmCorpus.serialize('joel_gtd.mm', corpus)
```

### 文書ベクトル (BoW) から，出現回数の多い単語を調べる

MmCorpus を読み出し(デシリアライズ)，`corpus` 変数に格納する。テキストファイル 9 行目（「たとえば、あなたのチームの〜」）に出現する上位10単語とその出現回数を表示する。

- ヒント1: 9行目の文書ベクトルは， `corpus[8]` で取り出せる。
- ヒント2: 単語IDから単語（文字列）への変換は， `dictionary.get(id)` メソッドが使える。 

```
In [35]: corpus = corpora.MmCorpus('joel_gtd.mm')
## write your code ##
[('を', 16.0),
 ('。', 12.0),
 ('バグ', 11.0),
 ('の', 10.0),
 ('、', 7.0),
 ('て', 7.0),
 ('に', 7.0),
 ('が', 6.0),
 ('あなた', 5.0),
 ('は', 5.0)]
```

### TFIDF モデル作成と適用

TfidfModel を作成して `tfidf` 変数に格納し，モデルを `corpus` に適用する。テキストファイル 9 行目に現れる単語の中で，tfidf 値の大きい上位10単語とその値を表示する。

ひとつ前の結果と比べてみましょう。

チュートリアル: https://radimrehurek.com/gensim/tut2.html

```
In [40]: tfidf = ## write your code ##
In [41]: corpus_tfidf = ## write your code ##
## write your code ##
[('バグ', 0.46777662910929185),
 ('彼ら', 0.2126257405042236),
 ('くれ', 0.18636800359271097),
 ('トラッキング', 0.18636800359271097),
 ('入力', 0.18636800359271097),
 ('データベース', 0.16196688680871282),
 ('始める', 0.14717296406592642),
 ('メール', 0.12424533572847397),
 ('使い', 0.12424533572847397),
 ('自身', 0.10797792453914187)]
```