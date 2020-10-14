#!/usr/bin/env python3

import requests
import json
import random

r = requests.get('https://randomstoicquotesapi.herokuapp.com/api/v1/quotes')

json_data = json.loads(r.text)

num_quotes = len(json_data['data'])

random_quote = random.randint(0,num_quotes-1) 

authors = {}

authors_data = json_data['included']

# Build the id -> author_name dictionary 
for author in authors_data:
	id = author['id']
	name = author['attributes']['name']
	authors[id] = name

quote = json_data['data'][random_quote]['attributes']['text']

quote_author_id = json_data['data'][random_quote]['relationships']['author']['data']['id']

author_name = authors[quote_author_id]

print('"' + quote + '"' + ' - ' + author_name)

