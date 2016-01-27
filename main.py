#!/usr/bin/env python
# -*- coding: utf-8 -*-

# main.py for "RyosyokuBot on Twitter"
# Author : KOMATSU Seiya @ NIT, Kagawa College Takuma Campus Dept. of IT




#----------import library----------
import os
import os.path
import sys
import urllib
#import tweepy
import json
import commands
import re
#from requests_oauthlib import OAuth1Session
import datetime
import locale






#----------define alias----------
path = './pdfData/kondate.pdf'
url = "http://www.kagawa-nct.ac.jp/dormitoryE/kondate.pdf"


#----------main----------
if os.path.exists("./pdfData"):
	pass
else:
	os.mkdir("./pdfData")



data = urllib.urlopen(url)

f1 = open(path, "wb")
f1.write(data.read())
f1.close()


os.system("pdftotext -layout -enc UTF-8 ./pdfData/kondate.pdf ./pdfData/kondate.txt")


#↓ こっからが面倒くさいんだよな(・・；)
#//////////////////////
#一応表示テスト
#f2 = open("./pdfData/kondate.txt")
#text = f2.read()
#f2.close()
#print text;
#//////////////////////

#空白行の削除
datafile = './pdfData/kondate.txt'
savefile = './pdfData/kondate01.txt'
input = open(datafile, 'r')
output = open(savefile, 'w')
L = input.readlines()
input.close()
for s in xrange(len(L)):
  if L[s] != '\n':
    #print L[s]
    output.write(L[s])
output.close()



#一行ずつ表示ver(条件付き・余分な行を消す)
for line in open('pdfData/kondate01.txt', 'r'):
	if re.match('^[0-9]{1,}$', line[1:2]):	
		pass
	#elif re.match('^\S', line[1:2]):
	#	print(line)
	elif (line.find('[') != -1):
		pass
	elif (line.find('ｴﾈﾙｷﾞ') != -1):
		pass
	elif (line.find('脂質') != -1):
		pass
	elif (line.find('g') != -1):
		pass
	elif (len(line) <= 5):
		pass
	elif (line.find('ジャム') != -1):
		pass
	elif (line.find('パン') != -1):
		pass
	elif (line.find('牛乳') != -1):
		pass
	elif (line.find('食塩') != -1):
		pass
	else:
		f9 = open('./pdfData/kondate02.txt', 'a')
		f9.write(line)
		f9.close()


#曜日データ取得
os.system("./bin/DeleteSpace ./pdfData/kondate02.txt 4")
week = commands.getoutput("./bin/DeleteSpace ./pdfData/kondate02.txt 4")
wlen = len(week) / 3
print(wlen)

#日付データ取得
d = datetime.datetime.today()
print '%s年%s月%s日' % (d.year, d.month, d.day)
# hour, minute, second, microsecond
print '%s時%s分' % (d.hour, d.minute)

os.system("./bin/DeleteSpace ./pdfData/kondate02.txt 5")
