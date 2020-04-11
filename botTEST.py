import json, config#標準のjsonモジュールとconfig.pyの読み込み
import twitter
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = twitter.OAuth(consumer_key=CK,
consumer_secret=CS,
token=AT,
token_secret=ATS)

t = twitter.Twitter(auth=auth)

content = "bottest定期実行2"
t.statuses.update(status=content)