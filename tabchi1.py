#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot import util
import sys
import json
import os
import subprocess
import requests
import random
import urllib
import urllib2
import redis
import requests as req
reload(sys)
sys.setdefaultencoding("utf-8")
TOKEN = '389259949:AAGElB8V5Mv2bqLCj7iIqc2B1cx9LojQXaI'
bot = telebot.TeleBot(TOKEN)
redis = redis.StrictRedis(host='localhost', port=6379, db=0)
db = "https://api.telegram.org/bot{}/getMe?".format(TOKEN)
#AFBOTS
f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n \033[01;34m Bot Username: {} \033[0m".format(bot.get_me().username)
i = "\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n \033[01;31m by @botreborn_ch \033[0m"
print(f + u + i + c)

@bot.message_handler(commands=['start'])
def start(m):
    if m.from_user.id == 344363589 :
     markup = types.InlineKeyboardMarkup()
     c = types.InlineKeyboardButton("@UnknowCyberArmy",callback_data='amar')
     markup.add(c)
     bot.send_message(m.chat.id, "سلام ادمین خوش اومدید برای دیدن امار ربات دستور /panel رو ارسال کنید و برای فرواد متن از /fwdall", reply_markup=markup, parse_mode='Markdown')
	 
@bot.message_handler(commands=['panel'])
def panel(m):
    if m.from_user.id == 344363589 :
     markup = types.InlineKeyboardMarkup()
     c = types.InlineKeyboardButton("امار🌟",callback_data='amar')
     markup.add(c)
     bot.send_message(m.chat.id, "پنل مدیریتی🖥", reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(commands=['fwdall'])
def fwdall(m):
    if m.from_user.id == 344363589 :
        if m.reply_to_message:
            mid = m.reply_to_message.message_id
            ids = redis.smembers('alls')
            for id in ids :
                try:
                    bot.forward_message(id,m.chat.id,mid)
                except:
                    redis.srem('alls',id)	
		
@bot.message_handler(commands=['bc'])
def clac(m):
    if m.from_user.id == 344363589 :
        text = m.text.replace("/bc ","")
        rd = redis.smembers('alls')
        for id in rd:
            try:
                bot.send_message(id, "{}".format(text), parse_mode="Markdown")
            except:
                redis.srem('alls', id)
		
@bot.message_handler(content_types=['new_chat_member'])
def new_member(m):
     id = m.chat.id
     redis.sadd('chatpys',id)
     redis.sadd('alls',id)
	  
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
 if call.message: 
     if call.data == "amar":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بروز رسانی💎",callback_data='amar')
       markup.add(c)
       usrs = str(redis.scard('seenchipy'))
       cha = str(redis.scard('chatpys'))
       tex = 'تعداد کاربران👤 : {}\nتعداد گروه🎯: {}'.format(usrs,cha)
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = tex, reply_markup=markup, parse_mode='Markdown')

bot.polling(True)
