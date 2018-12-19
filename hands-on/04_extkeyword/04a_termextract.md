# termextract (専門用語抽出)

## 準備

[ここ](http://gensen.dl.itc.u-tokyo.ac.jp/pytermextract/) から termextract をダウンロードして，インストールしてください。

```
(venv) 04_extkeyword$ wget http://gensen.dl.itc.u-tokyo.ac.jp/soft/pytermextract-0_01.zip
(venv) 04_extkeyword$ unzip pytermextract-0_01.zip
(venv) 04_extkeyword$ cd pytermextract-0_01/
(venv) pytermextract-0_01$ python setup.py install
(venv) pytermextract-0_01$ pip freeze
...
termextract==0.12b0
```

## 用語抽出

**ハンズオン課題 4-1**

1. 好きなニュース記事か，Wikipedia の記事（なるべく長めの文章が望ましい）の本文部分のみをコピーして保存してください。(Instapaper などを使うと楽です。)

2. 保存したテキストから，[CompoundNounFilter](http://mocobeta.github.io/janome/api/janome.html#janome.tokenfilter.CompoundNounFilter) を使って複合名詞(名詞の連続)を抽出し，出現回数をカウントして多い順に並べてください。

    - 参考: http://eneprog.blogspot.com/2018/07/janome-analayzerpython.html

3. [termextract ドキュメント](http://gensen.dl.itc.u-tokyo.ac.jp/pytermextract/) の「３．サンプルスクリプトを使用する」 に従って，保存したテキストから，termextract を使って用語抽出してください。

4. 2 と 3 の結果を比べてみましょう。

**ホームワーク**

さらに興味があれば，termextract の元になった論文を読んで，スコア算出方法や計算式を確認してみましょう。

出現頻度と連接頻度に基づく専門用語抽出

中川 裕志, 湯本 紘彰, 森 辰則

[ここ](https://www.jstage.jst.go.jp/article/jnlp1994/10/1/10_1_27/_article/-char/ja) から PDF がダウンロードできます。