import telebot
# 6927785010:AAGDZytTd-2JixpU5SxSxNTciX1JkTQlroI
bot = telebot.TeleBot("Sizning telegram tokeningiz")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Fast food buyurtma qilish uchun /menu buyrug'ini kiriting.")

@bot.message_handler(commands=['menu'])
def send_menu(message):
    menu = "Fast food menusi:\n1. Burger - $5\n2. Pizza - $8\n3. Hot dog - $4\n4. Qatiqshirinlik - $3"
    bot.send_message(message.chat.id, menu)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "/menu":
        return
    bot.reply_to(message, "Buyurtmangiz qabul qilindi! Tez orada sizga javob beramiz.")

bot.polling()
