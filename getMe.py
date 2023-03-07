import requests

TOKEN = '6097521187:AAHbPqQPSlFP54uT-Sj6MdnJpeBB_5Idsmg'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getMe'


response = requests.get(url=BASE_URL)
if response.status_code == 200:
    info = response.json()
    print(info)