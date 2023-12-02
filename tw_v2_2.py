from requests_oauthlib import OAuth1Session
import json
import base64
import os

# API key, secret, Bearer token, Access token and Access token secret
API_KEY = os.environ.get('MY_TW_CONSUMER_KEY')
API_SECRET_KEY = os.environ.get('MY_TW_CONSUMER_SEC')
ACCESS_TOKEN = os.environ.get('MY_TW_ACC_KEY')
ACCESS_TOKEN_SECRET = os.environ.get('MY_TW_ACC_SEC')

# API endpoint
url = "https://api.twitter.com/2/tweets"

# Create OAuth1 session
twitter = OAuth1Session(API_KEY, client_secret=API_SECRET_KEY, resource_owner_key=ACCESS_TOKEN, resource_owner_secret=ACCESS_TOKEN_SECRET)

# 現在のファイルのディレクトリを取得
current_dir = os.path.dirname(os.path.abspath(__file__))
# 画像ファイルのパスを設定（同一ディレクトリ内の 'zunda1.png'）
file_path = os.path.join(current_dir, 'zunda1.png')

with open(file_path, 'rb') as file:
    media_data = base64.b64encode(file.read()).decode()

# メディアアップロードのエンドポイント
media_url = 'https://upload.twitter.com/1.1/media/upload.json'

# メディアのアップロード
media_response = twitter.post(media_url, data={'media': media_data})

if media_response.status_code != 200:
    raise Exception(f"Media upload is not 200: {media_response.status_code}, {media_response.text}")

media_id = media_response.json()['media_id_string']

# Data (body)
tweet_data = {
    "text": "はろ2",
    "media": {
        "media_ids": [media_id]
    }
}

# headers
headers = {
    "Content-Type": "application/json"
}

# Send request with headers
response = twitter.post(url, headers=headers, data=json.dumps(tweet_data))

# Check the response
if response.status_code != 200:
    print(f"status code is {response.status_code}")
    raise Exception(
        f"Request returned with error: {response.status_code}, {response.text}"
    )
print(response.json())