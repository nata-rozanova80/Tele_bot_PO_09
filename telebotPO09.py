# Telebot reminding about prayer
import telebot
import datetime
import time
import threading
import os

token = "token"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Христос воскресе, радость моя!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['help'])
def handle_help_command(message):
    """Обрабатывает команду /help."""
    help_list = [
        'Доступные команды:',
        '/start - начать чат',
        '/help - показать эту помощь',
        '/info - Предоставляет информацию о боте.',
        '/stop - Останавливает бота и завершает сессию.',
        '/pray - Выберите текст молитвы.',
        '/audio - Выберите аудио файл.'
    ]
    help_message = '\n'.join(help_list)
    bot.reply_to(message, help_message)

def send_reminders(chat_id):
    current_time = datetime.datetime.now()
    print(f'Время на сервере: {current_time.strftime("%Y-%m-%d %H:%M:%S")}')
    first_rem = '12:59'
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem:
            bot.send_message(chat_id, 'reminder')
        time.sleep(61)


@bot.message_handler(commands=['pray'])  # Обработчик для молитв
def handle_prayer_selection(message):
    """Обрабатывает выбор молитвы пользователем."""

    if message.text == '/pray 1':
        file_path = 'C:\\Users\\Иван\\PycharmProjects\\pythonProject\\Files_for_bot_PO_09\\Our_Father'  # Путь к файлу "Отче наш"
    elif message.text == '/pray 2':
        file_path = 'C:\\Users\\Иван\\PycharmProjects\\pythonProject\\Files_for_bot_PO_09\\Virgin Mary'  # Путь к файлу "Богородице"
    elif message.text == '/pray 3':
        file_path = 'C:\\Users\\Иван\\PycharmProjects\\pythonProject\\Files_for_bot_PO_09\\Symbol_of_faith'  # Путь к файлу "Символ веры"
    else:
        bot.reply_to(message, 'Пожалуйста, выберите правильный номер молитвы: /pray 1, /pray 2 или /pray 3.')
        return  # Завершаем выполнение функции, если введен неправильный номер

    # Проверяем существование файла
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:  # Используйте правильную кодировку
            file_content = file.read()
        bot.reply_to(message, file_content)
    else:
        bot.reply_to(message, 'Файл не найден.')


@bot.message_handler(commands=['audio'])  # Обработчик для аудио
def handle_audio_selection(message):
    """Обрабатывает выбор аудио пользователем."""

    if message.text == '/audio 1':
        file_path2 = 'C:\\Users\\Иван\\PycharmProjects\\pythonProject\\Files_for_bot_PO_09\\sem_our_father.mp3'  # Путь к первому аудио
    elif message.text == '/audio 2':
        file_path2 = 'C:\\Users\\Иван\\PycharmProjects\\pythonProject\\Files_for_bot_PO_09\\sem_bogorodise.mp3'  # Путь ко второму аудио
    elif message.text == '/audio 3':
        file_path2 = 'C:\\Users\\Иван\\PycharmProjects\\pythonProject\\Files_for_bot_PO_09\\Simvol_very.mp3'  # Путь к третьему аудио
    else:
        bot.reply_to(message, 'Пожалуйста, выберите правильный номер аудио: /audio 1, /audio 2 или /audio 3.')
        return  # Завершаем выполнение функции, если введен неправильный номер

    # Проверяем существование файла
    if os.path.exists(file_path2):
        with open(file_path2, 'rb') as file:  # Открываем файл в бинарном режиме
            bot.send_audio(message.chat.id, file)  # Отправляем аудио пользователю
    else:
        bot.reply_to(message, 'Файл не найден.')




bot.polling(none_stop=True)