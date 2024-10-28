import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('7162191296:AAG1xbvrkpP0Vd_OaMfOuwNkYqQSg5g6qiA')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе пить водичку!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    facts = [
        "Вода на Земле может быть старше самой Солнечной системы...",
        "Горячая вода замерзает быстрее холодной...",
        "Больше воды в атмосфере, чем во всех реках мира..."
    ]
    random_fact = random.choice(facts)
    bot.reply_to(message, f'Лови факт о воде: {random_fact}')

def send_reminders(chat_id):
    reminders = ['13:29', '14:18', '18:00']
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now in reminders:
            bot.send_message(chat_id, "Напоминание - выпей стакан воды 1405")
            # Ждем 60 секунд, чтобы избежать повторной отправки в тот же интервал времени
            time.sleep(60)
        else:
            # Проверяем каждую минуту
            time.sleep(60)

bot.polling(none_stop=True)