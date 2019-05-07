# -*- coding: utf-8 -*-
# pipenv run python main.py
import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
