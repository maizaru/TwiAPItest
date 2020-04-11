import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

#ここまでテンプレ

url = "https://api.twitter.com/1.1/statuses/update.json"

print("ツイートしたいこと書け")
tweet = input('>> ')
print('*****************************')

params = {"status" : tweet}

res = twitter.post(url,params = params)

if res.status_code == 200:
    print('OK!')
else:
    print("失敗 : %d"% res.status_code)
