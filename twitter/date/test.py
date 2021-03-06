#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import locale
from requests_oauthlib import OAuth1Session

CK = ''                          # Consumer Key
CS = '' # Consumer Secret
AT = '' # Access Token
AS = ''      # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"


# 作業
date = datetime.datetime.today()

y = str(date.year)
m = str(date.month)
d = str(date.day)
h = str(date.hour)
mi = str(date.minute)
s = str(date.second)

TweetString = "現在の時刻："+ y +"年"+ m +"月"+ d +"日"+ h +"時"+ mi +"分"+ s +"秒です。\nFrom ICT Lab. NIT, Kagawa College\n#TwitterBot制作"

# ツイート本文
params = {"status": "新サーバからの投稿です。\n ServerOS : Arch Linux \n #TwitterBot制作"}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
