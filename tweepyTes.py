# -*- coding: utf-8 -*-
# ~/.profile　にアクセス情報を記載
# 更新を反映するには次のコマンドを実施　$ source ~/.profile
from tracemalloc import stop
import tweepy
import os
import datetime

CK=os.environ.get("MY_TW_CONSUMER_KEY")
CS=os.environ.get('MY_TW_CONSUMER_SEC')
AT=os.environ.get('MY_TW_ACC_KEY')
AS=os.environ.get('MY_TW_ACC_SEC')

dt_now = datetime.datetime.now()

client = tweepy.Client(consumer_key=CK, consumer_secret=CS, access_token=AT, access_token_secret=AS)
# test
tweetText = "がんばるぞい"+"\n"+ str(dt_now)
client.create_tweet(text=tweetText)
