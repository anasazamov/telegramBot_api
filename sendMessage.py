import os
import requests
from getUpdates import TOKEN


URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

payload = {
    "chat_id": 1258594598,
    "text": "ok"
}
requests.get(url=URL, params=payload)
