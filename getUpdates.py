import requests

TOKEN = '6097521187:AAHbPqQPSlFP54uT-Sj6MdnJpeBB_5Idsmg'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'


response = requests.get(url=BASE_URL)
updates=response.json()['result']

last_update = updates[-1]
last_msg = last_update['message']
text = last_msg['text']
first_name = last_msg['from']['first_name']
print(text, first_name)
