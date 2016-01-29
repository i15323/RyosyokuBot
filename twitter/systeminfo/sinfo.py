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
CK = 
CS = 
AT = 
AS = 


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
