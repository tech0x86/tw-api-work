
ツイッターAPI叩いてランダムな画像を投稿する

## 2023/12/02 Twitter APIについて
APIの仕様が変わり従来のtweepyライブラリでは動作しなくなったため、改めて動作するように修正。以下主な点。
・APIのOath 1.0を利用
・twitter API v2系を利用

# 環境
## Twitter API
elevated アカウント
API V1.1

## python
python3.9

tweepy 4.x

## インストールするpythonライブラリ
・tweepy
$ pip install tweepy
