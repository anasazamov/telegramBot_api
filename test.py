from requests import get
TOKEN = '6058623152:AAGROkpnAa7tK6gXhGiE_F-DpMqqFuxK8ns'
get_update= f'https://api.telegram.org/bot{TOKEN}/getUpdates'
get_send= f'https://api.telegram.org/bot{TOKEN}/sendMessage'

l=len(get(get_update).json()['result'])

while True:
    l_2=len(get(get_update).json()['result'])
    _key_= get(get_update).json()['result'][-1]['message'].keys()
    if l<l_2 and  "text" in _key_:
        text= get(get_update).json()['result'][-1]["message"]['text']
        chat_id=get(get_update).json()['result'][-1]["message"]['from']["id"]
        payload = {"chat_id":chat_id,"text":text}
        get(get_send,params=payload)
        l= len(get(get_update).json()['result'])