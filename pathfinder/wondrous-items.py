import requests
import urllib.request
import time
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
        attrs = row.findAll('td')
        name = attrs[1]
        if name.a is not None:
          name = name.a.string
        else:
          name = name.string
        items.append({'name': name, 'value': attrs[2].string})

