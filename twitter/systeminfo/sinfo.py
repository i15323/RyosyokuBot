#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#---時刻関係---
import sys
import datetime
import locale
#---Twitter関係---
from requests_oauthlib import OAuth1Session
import tweepy
import json
#---コマンド実行---
import subprocess


#各種キーをセット
CK = '52gM9Kqm0kyakg6bFuaTRadjD'
CS = '4nYS0gJOVCl4AGz1zJjRpgHlLL3h3NDn923qYK64HZSdLUN7km' 
AT = '1699390044-wXGIV448zEJy6dJgkNeuCf0vsF3dmCPWNTAXqJE'
AS = '4faPrVacqhgxWr3urabKjDKj1CvjoYD2BSs8ZmcnVgyZn'


url = "https://api.twitter.com/1.1/statuses/update.json"

#作業
for i in range(1,21):
	TweetString = "@AkihisaYoshii4 チノちゃんかわいい..."+str(i)+"回目"
	params = {"status": TweetString}
	twitter = OAuth1Session(CK, CS, AT, AS)
	req = twitter.post(url, params = params)
	if req.status_code == 200:
    		print ("OK")
	else:
		pass
