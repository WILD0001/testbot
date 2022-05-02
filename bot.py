import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def greet(message):
  bot.reply_to(message, "Hey how are you buddy?")

@bot.message_handler(commands=['help'])
def greet(message):
  bot.send_message(message.chat.id, "What do you want to do now?")
  
bot.polling()
