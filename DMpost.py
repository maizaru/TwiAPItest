import config#標準のjsonモジュールとconfig.pyの読み込み
import tweepy
import json
import scheduleTest
import time
import tk
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

print("フォロワー",followers_id)
print("*****************")

DMList = []
for following in following_id:
    if following in followers_id:
        DMList.append(following)
        print("following変数",following)
        print("********************")
print("DMList = ",DMList)


headers = {'content-type' : 'application/json'}
url = 'https://api.twitter.com/1.1/direct_messages/events/new.json'
text = "test234"

nowTime = time.time()
def DMSubmit():
    for i in range(len(DMList)):
        while True:
            targetTime = time.time()
            if targetTime - nowTime >= 5:
                payload = {"event" :
                       {"type" : "message_create",
                           "message_create" : {
                               "target" : {"recipient_id" : DMList[i]},
                               "message_data" : {"text" : text}
                           }
                        }
                     }

                payJson = json.dumps(payload)
                res = twi.post(url,headers=headers,data=payJson)
                time.sleep(5)
                break

DMSubmit()
#scheduleTest.scheduler(5,DMSubmit,2,False)