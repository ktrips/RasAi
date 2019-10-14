import requests
IFTTT_URL = 'https://maker.ifttt.com/trigger/zero_line/with/key/'
IFTTT_KEY = 'ctRhEui8F6QSaJye-1IfGi'
requests.post(IFTTT_URL + IFTTT_KEY, json = {'value1':'aaa', 'value2':'bbb', 'value3':'https://shoppinglist.google.com'})
