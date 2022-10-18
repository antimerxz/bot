import config
import telebot
import requests
import re

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def main(message):
    start = ("Salam @" + message.from_user.username)
    bot.reply_to(message, start) 
#    bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgQAAxkBAAEBZeVjTq2hERcq1Jy77GjeEZWM5nb0owACFA4AAtDNqFHHIz0mjQAB8EcqBA')

@bot.message_handler(commands=['josh', 'Josh', 'JOSH'])
def main(message):
    bot.reply_to(message, "give this guy some ass for godsake")

#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#	bot.reply_to(message, "error")

@bot.message_handler(content_types=["new_chat_members"])
def wlc(message):
    for new_member in message.new_chat_members:
        bot.reply_to(
                message, "khosh omadi @" + new_member.username + " <3")
@bot.message_handler(content_types=["left_chat_member"])
def left(message):
    bot.reply_to(message, "yeki sikesho zad")
@bot.message_handler(content_types=["pinned_message"])
def send(message):
    bot.reply_to(message, "pedareto pin mikoni koskesh ?")
@bot.message_handler(content_types=["location"])
def send(message):
    bot.reply_to(message, "lokht sho daram miam")
#@bot.message_handler(content_types=["sticker"])
#def send(message):
#    bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgQAAxkBAAEBZeFjTq0XVwM_TUOI3FP0hHixSEDVawAC0wsAAqKyAVPUrWzQVYb-5CoE')
#    bot.send_audio(chat_id=message.chat.id, audio=open('voices/joe2.ogg', 'rb'))


@bot.message_handler(func=lambda msg: msg.text is not None and '/' not in msg.text)
def amir(message):
    p = r"(?i)\bamir\b"
    if re.match(p, message.text):
        bot.reply_to(message, "kune sefid")
    f = r"(?i)\bامیر\b"
    if re.match(f, message.text):
        bot.reply_to(message, "kune sefid")
    t = r"(?i)\bjosh\b"
    if re.match(t, message.text):
        bot.send_audio(chat_id=message.chat.id, audio=open('voices/joe2.ogg', 'rb'))
    m = r"(?i)\bmersad\b"
    if re.match(m, message.text):
        bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgQAAxkBAAEBZeVjTq2hERcq1Jy77GjeEZWM5nb0owACFA4AAtDNqFHHIz0mjQAB8EcqBA')
    dick = r"(?i)\bmmd\b"
    if re.match(dick, message.text):
        bot.send_audio(chat_id=message.chat.id, audio=open('voices/mmd.ogg', 'rb'))     
    zi = r"(?i)\bضیایی\b"
    if re.match(zi, message.text):
        bot.reply_to(message, "dalal")
    mii = r"(?i)\bmisagh\b"
    if re.match(mii, message.text):
        bot.send_audio(chat_id=message.chat.id, audio=open('voices/mi.ogg', 'rb'))


bot.infinity_polling()
