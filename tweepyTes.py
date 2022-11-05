# -*- coding: utf-8 -*-
# ~/.bashrc　にアクセス情報を記載
# 更新を反映するには次のコマンドを実施　$ source ~/.bashrc
from tracemalloc import stop
import tweepy
import os
import datetime
imgPath = "./img/"
# javanyan.jpg

CK=os.environ.get("MY_TW_CONSUMER_KEY")
CS=os.environ.get('MY_TW_CONSUMER_SEC')
AT=os.environ.get('MY_TW_ACC_KEY')
AS=os.environ.get('MY_TW_ACC_SEC')

def tweetTextOnly(twText):
    dt_now = datetime.datetime.now()
    client = tweepy.Client(consumer_key=CK, consumer_secret=CS, access_token=AT, access_token_secret=AS)
    tweetText = twText +"\n"+ str(dt_now)
    client.create_tweet(text=tweetText)
    return

def tweetTextMedia(twText, imgPath):
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    TW_API = tweepy.API(auth)
    media_ids = []
    img  = TW_API.media_upload(imgPath + "javanyan.jpg")
    media_ids.append(img.media_id)
    TW_API.update_status(status=twText, media_ids=media_ids)
    return

if __name__ == '__main__':
    print('start main func')
    #tweetTextMedia("がんばるぞい",imgPath)
    tweetTextOnly("がんばるぞい \n 2022/11/06")