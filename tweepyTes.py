# -*- coding: utf-8 -*-
# ~/.bashrc　にアクセス情報を記載(非ログインシェル＝イベント実行時に参照できる)
# 更新を反映するには次のコマンドを実施　$ source ~/.bashrc
from tracemalloc import stop
import tweepy
import os
import datetime
import random
imgPath = "./img/"


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

def tweetTextMedia(twText, imgName):
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    TW_API = tweepy.API(auth)
    media_ids = []
    img  = TW_API.media_upload(imgPath + imgName)
    media_ids.append(img.media_id)
    try:
        result = TW_API.update_status(status=twText, media_ids=media_ids)
        #print (result)
    except Exception as e:
        print (e)
    return

if __name__ == '__main__':
    print('start main func')
    #tweetTextMedia("がんばるぞい",imgPath)
    #tweetTextOnly("がんばるぞい")
    #fileリストを取得
    img_ext = [".jpg",".png"]
    files = os.listdir(imgPath)
    # ファイルのみリスト形式で取得
    files_file = [f for f in files if os.path.isfile(os.path.join(imgPath, f))]
    #拡張子が画像形式のものをリスト化
    img_files = [f for f in files_file if os.path.splitext((os.path.join(imgPath, f)))[1] in img_ext ]
    #print (img_files)
    #画像リストの中からランダムにimg nameを一つ選択
    img = img_files[random.randint(0, len(img_files) -1)]
    

    tweetTextMedia("がんばるぞい　ぞい \n 2022/11/06",img)