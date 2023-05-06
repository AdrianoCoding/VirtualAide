from main import *
from keys import *
from telebot import *
import time, os,subprocess
import threading

@bot.message_handler(commands=['start'])
def responder (mensagem):
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(5)
    bot.reply_to(mensagem, 'Olá, meu nome é Aide. Estou aqui para ajudar. Uso inteligencia artificial para pensar na resposta de suas perguntas.\n Sou opensource, visite meu repositorio público em: https://github.com/Xituis/VirtualAide')
    if mensagem.chat.type == 'private':
        bot.reply_to(mensagem,'Me mande uma mensagem como se estivesse falando com uma pessoa normal, e assim, poderei conversar horas com você :)')
    else:
        bot.reply_to(mensagem,'Para me usar, você tem que iniciar sua frase com a palavra "aide" \n Exemplo: aide tudo bem?')

@bot.message_handler(commands=['on', 'help'])
def responder(mensagem):
    if mensagem.text.startswith('/on'):
        if mensagem.from_user.id in admin:
            time.sleep(2)
            bot.reply_to(mensagem, 'O servidor principal está ON')
            bot.reply_to(mensagem, 'Total de Memoria Usada')
            saida = subprocess.check_output(['free'])
            bot.reply_to(mensagem, saida)
        else:
            bot.reply_to(mensagem,'Você não tem permissão para este comando. (VERGONHA DA PROFISSION)')
    elif mensagem.text.startswith('/help'):
        bot.send_chat_action(mensagem.chat.id, 'typing')
        time.sleep(4)
        bot.reply_to(mensagem, 'Olá, meu nome é Aide e sou um bot com inteligência artificial. Estou aqui para ajudar você a encontrar as informações que precisa, ou apenas conversar. Para usar meus serviços, basta enviar uma mensagem com o que você deseja, se quer conversar: Converse, se quer perguntar: Pergunte. Estou aqui para ajudar e responder às suas perguntas. Se precisar de ajuda, não hesite em me contatar. Estou à sua disposição.')
