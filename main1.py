from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import translators as ts
import whois
import time
import qrcode
import os

from time import sleep
import random

app = Client("my_account")


@app.on_message(filters.command("funny", prefixes=".") & filters.me)
def funny(_, msg):
    new_text = ''
    orig_text = msg.text.split(".funny ", maxsplit=1)[1]
    kek = 0
    for i in range(0, len(orig_text)):
        if (kek % 2 == 0):
            new_text += orig_text[i].lower()
        else:
            new_text += orig_text[i].upper()
        if (orig_text[i] != ' '):
            kek += 1
    msg.edit(new_text)

tr_lang = 'ru'

@app.on_message(filters.command("whois", prefixes=".") & filters.me)
def who_is(_, msg):
    domain = msg.text.split(".whois", maxsplit=1)[1]
    er = False
    try:
        dom = whois.query(domain).__dict__
    except Exception as e:
        er = True
        #print(e)
    if (er == False):
        msg.edit('``' + str(dom) + '``')
    if (er == True):
        msg.edit('**Не ворк**')
        
@app.on_message(filters.command("eval_l", prefixes=".") & filters.me)
def eval_os(_, msg):
        error = 0
        toeval = msg.text.split(".eval_l ", maxsplit=1)[1]
        toeval_edit = toeval
        toeval_edit = toeval.replace('**', '^^')
        ret_str = "**Expression:**\n"
        ret_str += toeval_edit
        ret_str += '\n'
        ret_str += "**Result**:\n"
        help_plz = '```' +  os.popen(toeval).read() + '```'
        ret_str += str(help_plz)
       # try:
      #  ret_str += str(os.system(toeval))
     #   except Exception as e:
         #   error = 1
            #ret_str = ('**Invalid** **expression** **format**')
       # if error == 0:
        msg.edit(ret_str)
       # else:
       #     msg.edit('**Invalid** **expression** **format**')
        #print(str(os.system(toeval)))
        
@app.on_message(filters.command("chlang", prefixes=".") & filters.me)
def chlang(_, msg):
    global tr_lang
    tr_lang = msg.text.split(".chlang ", maxsplit=1)[1]
    msg.edit('**Done!**')

@app.on_message(filters.command("translate", prefixes=".") & filters.me)
def trans_late(_, msg):
    #new_text = ''
    orig_text = msg.text.split(".translate ", maxsplit=1)[1]
    #new_text = translator.translate(orig_text, dest='ru')
    new_text = ts.google(orig_text, to_language=tr_lang)
    #print(tr_lang)
    ret_str = "**Original:**\n"
    ret_str += orig_text
    ret_str += '\n'
    ret_str += "**Translation:**\n"
    ret_str += str(new_text)
    #print(ret_str)
    msg.edit(ret_str)
# eval

os.system('mkdir pics')
global n
n = 0

@app.on_message(filters.command("qr", prefixes=".") & filters.me)
def qr(_, msg):
    global n
    n = 0
    s = str(msg.text)
    img = qrcode.make(s)
    type(img)
    #print(msg)
    path = "code" + str(n) + ".png"
    img.save(path)
    msg.edit('QR generated!')
    app.send_photo(msg.chat.id, path, reply_to_message_id=msg.message_id)

newlang = 'en'
@app.on_message(filters.command("eval", prefixes=".") & filters.me)
def eva_l(_, msg):
        error = 0
        toeval = msg.text.split(".eval ", maxsplit=1)[1]
        toeval_edit = toeval
        toeval_edit = toeval.replace('**', '^^')
        ret_str = "**Expression:**\n"
        ret_str += toeval_edit
        ret_str += '\n'
        ret_str += "**Result**:\n"
        try:
            ret_str += str(eval(toeval))
        except Exception as e:
            error = 1
            #ret_str = ('**Invalid** **expression** **format**')
        if error == 0:
            msg.edit(ret_str)
        else:
            msg.edit('**Invalid** **expression** **format**')
            

@app.on_message(filters.command("ping", prefixes=".") & filters.me)
def ping(_, msg):
    msg.edit('Pong!')


@app.on_message(filters.command("gh", prefixes=".") & filters.me)
def gh(_, msg):
    msg.edit('My github: http://github.com/KonstDev/')


app.run()
