#!/bin/sh

echo ------------------------
# ゲーム作成を支援するモジュール
# Python3.8以上では正常にインストールできないもよう。(2020/02/10現在)
# Python3.7.3でインストールできたとの記事あり
# Anaconda環境で実行すべし
pip install pygame

echo ------------------------
# インストール済みモジュールリストの確認
pip list
echo ------------------------
