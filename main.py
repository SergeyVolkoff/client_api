# /client_api/main.py

from pyrogram import Client

api_id = 21147848
api_hash = '0258abacf0e4b4c4aa912c1b763775a7'

# Создаём программный клиент, передаём в него
# имя сессии и данные для аутентификации в Client API
app = Client('my_account', api_id, api_hash)

app.start()
# Отправляем сообщение
# Первый параметр - это id чата или имя получателя.
# Зарезервированное слово 'me' означает собственный аккаунт отправителя.
app.send_message('@OleVlV', 'Привет, это я, bot, AHAHAHA!')
app.stop()