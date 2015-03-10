import requests
from random import randint
import json

postdata = {}
items = []
colours = ['Red', 'Yellow', 'Blue', 'Green', 'Mauve']

with open('fruits') as fruit_stream:
  for line in fruit_stream:
    items.append({'key' : line.rstrip(),'value' : {'count' : randint(10,3000),'colour' : colours[randint(0, len(colours)-1)]}})
    postdata['items'] = items


headers={ 'Content-Type' : 'application/json' }
r = requests.post('http://localhost:8079/api/buckets/fruit/keys', data=json.dumps(postdata), headers=headers)
print r.text
