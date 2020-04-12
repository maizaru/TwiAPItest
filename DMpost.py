import config#標準のjsonモジュールとconfig.pyの読み込み
import tweepy
import json
import time
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twi = OAuth1Session(CK,CS,AT,ATS)
    # 認証情報の設定
auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,ATS)
api = tweepy.API(auth)
    # ユーザーIDの確認
twitter = api.user_timeline()
MyId = twitter[0].user.id_str
followers_id = api.followers_ids(MyId)
following_id = api.friends_ids(MyId)
DMList = []
for following in following_id:
    if following in followers_id:
        DMList.append(following)
status = []
userName = []
for i in range(len(DMList)):
    status.append(api.get_user(DMList[i]))
    userName.append(status[i].screen_name)
    print(userName[i])

headers = {'content-type' : 'application/json'}
url = 'https://api.twitter.com/1.1/direct_messages/events/new.json'
#text = "test234"

def DMSubmit(textContent,sleepCount):
    for i in range(len(DMList)):
        while True:
            payload = {"event" :
                       {"type" : "message_create",
                           "message_create" : {
                               "target" : {"recipient_id" : DMList[i]},
                               "message_data" : {"text" : textContent}
                           }
                        }
                     }

            payJson = json.dumps(payload)
            res = twi.post(url,headers=headers,data=payJson)
            time.sleep(sleepCount)
            break

if __name__ == "__DMSubmit__":
    DMSubmit()