import json
import config#標準のjsonモジュールとconfig.pyの読み込み
import tweepy
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

# 認証
twitter = OAuth1Session(CK,CS,AT,ATS)

# パラメータ設定
endpoint = 'https://api.twitter.com/1.1/direct_messages/events/list.json'
params = {'count':'50'}

# リクエスト送信
res = twitter.get(endpoint, params = params)

# レスポンスはJson文字列なので、Json文字列を辞書形式に変換
dic = json.loads(res.text)
print(dic)