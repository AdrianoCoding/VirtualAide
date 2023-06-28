from comandos import *
from keys import *
from chatprivado import *
from telebot import types
import time, os,subprocess
import threading
last_message_time = {}

@bot.message_handler(commands=['aide', 'Aide', 'aidentro', 'aides', 'aids'])
def reply_to_message(message):
    global last_message_time
    chat_id = message.chat.id
    now = time.time()
    if chat_id not in last_message_time or now - last_message_time[chat_id] > 5: # O bot responde uma mensage a cada 30 segundos
        last_message_time[chat_id] = now
        bot.send_chat_action(chat_id, 'typing')
        response = reply_to_message(message.text)
        responseText = response.choices[0].text
        bot.reply_to(message, responseText)
    else:
        bot.reply_to(message, "Eu vou te responder, mas espera um minuto, meu café tá ficando pronto, já volto")

# Usuario Interação
def reply_to_message(message):
    # Obter a mensagem do usuário
    user_message = message + comp

# Enviar a mensagem do usuário para a OpenAI e obter uma resposta
    response = openai.Completion.create(
        model="text-davinci-003", #Altere caso necessite de um outro modelo de pensamento
        prompt=user_message,
        max_tokens=1024,
        chat_mode= "assistant",
        n=1,
        stop=None,
        temperature=0.1,
        frequency_penalty =  0,
        presence_penalty = 0
    )
    return response

# Definir a função principal do bot
def main():
    bot.infinity_polling()
    # bot.polling()

if __name__ == "__main__":
    main()
