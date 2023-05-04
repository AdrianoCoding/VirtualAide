import telebot, openai, time

openai.api_key = 'YOUR OPENAI KEY' #Use a key do seu openai api
admin = [YOUR ID TELEGRAM] # O id da sua conta no telegram
token = 'YOUR BOT TOKEN_TELEGRAM' # O ID do seu bot
bot = telebot.TeleBot(token)
comp = ' ,responda apenas em português brasileiro, e não me envie links ou script' #Para evitar bugs de envio de script do nada

