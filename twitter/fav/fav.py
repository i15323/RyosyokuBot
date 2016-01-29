#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import datetime
import locale
#---Twitter関係---
from requests_oauthlib import OAuth1Session
import tweepy
import json


#各種キーをセット
CK = ''
CS = ''
AS = ''
AT = ''
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

#APIインスタンスの生成
api = tweepy.API(auth)


#作業
sys.stdout.write("id:@")
id = input()
print(id+"のツイートをふぁぼします！")

api.update_status('Hello, world!')

