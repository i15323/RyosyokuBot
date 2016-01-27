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
CK = '52gM9Kqm0kyakg6bFuaTRadjD'
CS = '4nYS0gJOVCl4AGz1zJjRpgHlLL3h3NDn923qYK64HZSdLUN7km' 
AT = '1699390044-wXGIV448zEJy6dJgkNeuCf0vsF3dmCPWNTAXqJE'
AS = '4faPrVacqhgxWr3urabKjDKj1CvjoYD2BSs8ZmcnVgyZn'
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

#APIインスタンスの生成
api = tweepy.API(auth)


#作業
sys.stdout.write("id:@")
id = input()
print(id+"のツイートをふぁぼします！")

api.update_status('Hello, world!')

