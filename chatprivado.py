from main import *
from keys import *
from telebot import *
from comandos import *
import time, os,subprocess
import threading

# Usuario Interação
def reply_to_message(message):
    # Obter a mensagem do usuário
    user_message = message + comp

# Enviar a mensagem do usuário para a OpenAI e obter uma resposta
    response = openai.Completion.create(
        model="text-davinci-003", #Altere caso necessite de um outro modelo de pensamento
        prompt=user_message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.1,
        frequency_penalty =  0,
        presence_penalty = 0
    )
    return response

@bot.message_handler(commands=['aide', 'Aide', 'aidentro', 'aides', 'aids'],chat_types='private')
def alerta(message):
      bot.reply_to(message,'Não é necessario usar /aide aqui :) \n Para agilizar sua pergunta, é só mandar ela, e responderei normalmente')
# Interação do usuario sem o uso do comando
@bot.message_handler(func=lambda message: True,chat_types='private')
def echo_all(message):
        bot.send_chat_action(message.chat.id, 'typing')
        response = reply_to_message(message.text)
        responseText = response.choices[0].text
    # Enviar a resposta do ChatGPT de volta ao usuário
        bot.reply_to(message, responseText)
