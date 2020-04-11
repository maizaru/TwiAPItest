import json, config#標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK,CS,AT,ATS)

headers = {'content-type' : 'application/json'}
url = 'https://api.twitter.com/1.1/direct_messages/events/new.json'
targetID = "********************"#送り先のTwitterID
text = "testDM2"

payload = {"event" :
          {"type" : "message_create",
              "message_create" : {
                  "target" : {"recipient_id" : targetID},
                  "message_data" : {"text" : text}
              }
          }
}

payJson = json.dumps(payload)

res = twitter.post(url,headers=headers,data=payJson)