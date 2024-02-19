import time

import requests
from celery import shared_task
from django.conf import settings


@shared_task
def send_telegram_notification(order_id, product_name, quantity, customer_username, phone_number):
    time.sleep(5)
    token = settings.TELEGRAM_BOT_TOKEN
    method = 'sendMessage'
    message_text = f"Buyurtma: {order_id}\n Mahsulot: {product_name}\n Soni: {quantity}\n " \
                   f"Buyurtmachi: {customer_username}\n tel: {phone_number}"

    response = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id': 182534710, 'text': message_text}
    ).json()
