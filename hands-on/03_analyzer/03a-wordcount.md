# Word Count

**ハンズオン課題 3-1**

引数で指定されたファイルを読み，出現回数の多い上位20単語と，その出現回数を出力するプログラム `wordcount.py` を作成してください。

ヒント: http://mocobeta.github.io/janome/api/janome.html#janome.tokenfilter.TokenCountFilter

(例)

```
$ python wordcount.py ../data/kazeno_matasaburo_utf8.txt
。	1071
た	895
て	803
の	802
、	782
...
```

※ (＋α) MeCab が使える方は，MeCab + mecab-python3 で書き換えてみてください。

**ハンズオン課題 3-2**

`wordcount.py` を修正して，２番めの引数が指定されたら，その品詞に絞り，かつ基本形の出現回数の多い上位20単語と，その出現回数を出力するようにしてください。

(例)

```
$ python wordcount.py ../data/kazeno_matasaburo_utf8.txt 名詞
みんな	167
三郎	134
の	134
よう	114
一郎	91
...
```

```
$ python wordcount.py ../data/kazeno_matasaburo_utf8.txt 動詞
する	217
いる	217
言う	145
来る	107
なる	96
...
```

※ (＋α) MeCab が使える方は，MeCab + mecab-python3 で書き換えてみてください。
