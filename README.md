# README

python の CLI についてまとめる。  
argparseライブラリを用いてサブコマンドを実装する。  
具体的にはプログラム(`python_cli_samples/tools/__main__.py`)に記載しているように行うとサブコマンドが実装できる。  

またサブコマンドは更にサブコマンドを追加できる（サブサブコマンド？と呼べばよいだろうか？）  
その内容は `python_cli_samples/tools/print` ディレクトリを参照すると理解できる。  

またディレクトリ構成に関しても本リポジトリが参考になるだろう

実際に動かしてみる際には以下のプログラムで実行できる。

## 実行

helpコマンドをつけて実行すると以下のように表示させる。

```bash
python python_cli_samples --help
#usage: [-h] {find_imgs,print} ...
#
#positional arguments:
#  {find_imgs,print}
#    find_imgs        find imgs in dir
#    print            print tools
#
#options:
#  -h, --help         show this help message and exit
```