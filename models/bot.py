import requests
from decouple import config
from .models import Came, Gone
def send_message_to_telegram(message):
    token = config('BOT_TOKEN')
    chat_id =config('CHAT_ID')
    if message['checking_status']!=Came:
        text = f"#Ketdi\n\n{message['user']}\n{message['time']}"
    else:
        text = f"#Keldi\n\n{message['user']}\n{message['time']}"

    response = requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage',
        data={'chat_id': chat_id, 'text': text}
    )

    if response.status_code == 200:
        print("Xabar muvaffaqiyatli yuborildi.")
    else:
        print(f"Xato: {response.status_code} - {response.text}")