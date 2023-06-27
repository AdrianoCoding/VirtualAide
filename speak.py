from comandos import *
from keys import *
from chatprivado import *
from telebot import types
import time, os,subprocess, threading, pyttsx3

@bot.message_handler(func=lambda message: True)
def reply_to_message(message):
           bot.send_chat_action(message.chat.id, 'recorder')
           bot.reply_to('Estou no ônibus, não posso mandar audio agora')