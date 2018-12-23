# Getting Started

## 準備

1. Janome 0.3.7 をインストール

```
(venv) hands-on$ pip install janome
(venv) hands-on$ janome --version
janome 0.3.7
```

2. Graphviz をインストール

For Mac

```
# MacPort
$ sudo port install graphviz

# Homebrew
$ brew install graphviz

# インストールされたか確認
$ type dot
dot is /usr/local/bin/dot
```

For Windows

[ここ](https://graphviz.gitlab.io/_pages/Download/Download_windows.html) からダウンロードして bin フォルダにパスを通す。

```
# インストールされたか確認
>where dot
C:\Program Files (x86)\Graphviz2.38\bin\dot.exe
```

## Janome CLI

**Windows で文字化けする場合， `-e sjis` オプションをつけてください。**

対話的に使う:

```
(venv) hands-on$ janome
すもももももももものうち
すもも	名詞,一般,*,*,*,*,すもも,スモモ,スモモ
も	助詞,係助詞,*,*,*,*,も,モ,モ
もも	名詞,一般,*,*,*,*,もも,モモ,モモ
も	助詞,係助詞,*,*,*,*,も,モ,モ
もも	名詞,一般,*,*,*,*,もも,モモ,モモ
の	助詞,連体化,*,*,*,*,の,ノ,ノ
うち	名詞,非自立,副詞可能,*,*,*,うち,ウチ,ウチ
```

ワンライナー:

```
(venv) hands-on$ echo "自然言語処理ことはじめ" | janome
自然	名詞,形容動詞語幹,*,*,*,*,自然,シゼン,シゼン
言語	名詞,一般,*,*,*,*,言語,ゲンゴ,ゲンゴ
処理	名詞,サ変接続,*,*,*,*,処理,ショリ,ショリ
こと	名詞,非自立,一般,*,*,*,こと,コト,コト
はじめ	名詞,副詞可能,*,*,*,*,はじめ,ハジメ,ハジメ
```

ラティスグラフを描画:

```
(venv) hands-on$ echo "銀河鉄道" | janome -g
銀河	名詞,一般,*,*,*,*,銀河,ギンガ,ギンガ
鉄道	名詞,一般,*,*,*,*,鉄道,テツドウ,テツドー
Graph was successfully output to lattice.gv.png
```

```
(venv) hands-on$ echo "仮想通貨取引" | janome -m -g
仮想	名詞,サ変接続,*,*,*,*,仮想,カソウ,カソー
通貨	名詞,一般,*,*,*,*,通貨,ツウカ,ツーカ
取引	名詞,サ変接続,*,*,*,*,取引,トリヒキ,トリヒキ
Graph was successfully output to lattice.gv.png
```

### 形態素解析が失敗する例

なぜ失敗するのか，ラティスグラフも観察してみましょう。

1. 

```
(venv) hands-on$ echo "庭には二羽にわとりがいる" | janome -g
(venv) hands-on$ echo "にわにはにわにわとりがいる" | janome -g
```

2.

```
(venv) hands-on$ echo "美ら海" | janome -g
(venv) hands-on$ echo "美ら海水族館" | janome -g
(venv) hands-on$ echo "図画コンクール" | janome -g
(venv) hands-on$ echo "美ら海図画コンクール" | janome -g
```

## NEologd 同梱 Janome の紹介

リソース使用・性能に課題があるので，プロダクションユースでは MeCab + mecab-ipadic-neologd を使うことをおすすめします。

[ここ](https://drive.google.com/drive/u/1/folders/0BynvpNc_r0kSd2NOLU01TG5MWnc) からビルド済みパッケージをダウンロード

Chrome だとダウンロード時に 403 エラーになるようなので，FireFox など別のブラウザを使ってみてください。

インストール

**PyPI の Janome を入れた環境とは別の環境に入れてください**

```
(venv2) hands-on$ pip install --no-compile ~/Downloads/Janome-0.3.7.neologd20181206.tar.gz
(venv2) hands-on$ python -c "from janome.tokenizer import Tokenizer; Tokenizer(mmap=True)"
```

CLI から使う (-m オプション必須)

ラティスグラフも見てみましょう。

```
(venv2) hands-on$ echo "すもももももももものうち" | janome -m -g
(venv2) hands-on$ echo "自然言語処理ことはじめ" | janome -m -g
(venv2) hands-on$ echo "銀河鉄道" | janome -m -g
(venv2) hands-on$ echo "仮想通貨取引" | janome -m -g
(venv2) hands-on$ echo "美ら海水族館" | janome -m -g
```
