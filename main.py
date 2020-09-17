#!/usr/bin/env python3

import requests
import json
import random

r = requests.get('https://randomstoicquotesapi.herokuapp.com/api/v1/quotes')

json_data = json.loads(r.text)

num_quotes = len(json_data['data'])

random_quote = random.randint(0,num_quotes-1) 

print(json_data['data'][random_quote]['attributes']['text'])
