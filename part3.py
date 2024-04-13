import requests
import json
from pprint import pprint

def translate_word(word):
    url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20220928T183617Z.4449b33063fe4328.b93679d48620ed6f3c20da6bff0237bcbd0e8d6a'
    token = 'dict.1.1.20220928T183617Z.4449b33063fe4328.b93679d48620ed6f3c20da6bff0237bcbd0e8d6a'
    params = {
        'lang': 'ru-en',
        "text": word
    }
    responce = requests.get(url, params=params)
    #pprint(responce.json()["def"])
    x = responce.json()["def"]
    return x[0]['tr'][0]["text"]

translate_word('кот')