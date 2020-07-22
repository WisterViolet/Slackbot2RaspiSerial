# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to 
from slackbot.bot import default_reply

@listen_to('[Oo]pen|[開あ]けて')
def open_operation(message):
    message.react('unlock')

@listen_to('[Cc]lose|[閉し締]めて')
def close_operation(message):
    message.react('closed_lock_with_key')

@default_reply()
def default_func(message):
    message.react('question')