import requests
import time

TOKEN = '6097521187:AAHbPqQPSlFP54uT-Sj6MdnJpeBB_5Idsmg'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

update_id = -1

while True:
    response = requests.get(url=BASE_URL)
    updates=response.json()['result']

    last_update = updates[-1]

    last_update_id = last_update['update_id']
    if update_id != last_update_id:

        last_msg = last_update['message']
        text = last_msg['text']
        first_name = last_msg['from']['first_name']

        print(text, first_name)

        update_id = last_update_id
    time.sleep(1)
