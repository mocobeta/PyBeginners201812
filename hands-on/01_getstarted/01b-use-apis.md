# Janome API を使う

## ドキュメント/リファレンス/プログラム例

- https://mocobeta.github.io/janome/
- http://mocobeta.github.io/janome/api/
- https://github.com/mocobeta/janome/tree/master/examples

## Hello Janome!

好みのインタプリタから実行してください。

```
In [1]: from janome.tokenizer import Tokenizer
In [2]: t = Tokenizer()
In [3]: for token in t.tokenize('今日も１日がんばるぞい'):
   ...:     print(token)
```

**ハンズオン課題 1-1** 

'今日も１日がんばるぞい' を形態素解析して，表層形のみを取り出してください。

ヒント: API リファレンスを参照するか，または `Token` クラスのプロパティは `dir` でも確認できます。

```
In [12]: token = t.tokenize('今日')[0]
In [13]: dir(token)
```

なお，`wakati=True` オプションをつけた場合と同じ結果になるはずです。

```
In [8]: for token in t.tokenize('今日も１日がんばるぞい', wakati=True):
   ...:     print(token)
```

※ (＋α) MeCab が使える方は，MeCab + mecab-python3 で書き換えてみてください。

**ハンズオン課題 1-2** 

'今日も１日がんばった' を形態素解析して，基本形のみを取り出してください。

※ (＋α) MeCab が使える方は，MeCab + mecab-python3 で書き換えてみてください。

## ユーザー定義辞書

**ハンズオン課題 1-3**

ユーザー定義辞書を使って，"美ら海図画コンクール" が正しく形態素解析されるようにしてください。

※ (＋α) MeCab が使える方は，MeCab + mecab-python3 で書き換えてみてください。
