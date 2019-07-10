import requests
import urllib.request
import time
import json
import os
from bs4 import BeautifulSoup

url = 'https://www.d20pfsrd.com/magic-items/wondrous-items/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.findAll('table')
items = []

for table in tables:
  if table.caption is not None:
    if 'lesser' in table.caption.string.lower() or 'greater' in table.caption.string.lower():
      rows = table.tbody.findAll('tr')
      for row in rows:
        if row.a is not None:
          attrs = row.findAll('td')
          name = attrs[1]
          stringName = ''
          for part in name.contents:
            stringName += part.string
          items.append({'name': stringName, 'value': attrs[2].string, 'category': 'wondrous', 'wiki': row.a['href']})

if not os.path.exists('output'):
  os.makedirs('output')

with open('output/wondrous.json', 'w+') as output:
  json.dump(items, output)
