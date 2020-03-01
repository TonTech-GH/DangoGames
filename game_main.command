#!/bin/sh
# このファイルのあるディレクトリに移動
cd $(dirname $0)

# このファイルの名前を取得
name=$(basename $0)

# 拡張子を除去して.pyを付与
pyname=${name%.*}.py

# Python実行
python3 $pyname
