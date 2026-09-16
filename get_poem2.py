import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
import re

def search(query):
    url = 'https://html.duckduckgo.com/html/?q=' + urllib.parse.quote(query)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        for a in soup.find_all('a', class_='result__snippet'):
            print(a.text)
    except Exception as e:
        print(e)

search('زكي قنصل "دامي الفؤاد يمضه ألم"')
search('زكي قنصل "الشوك يزخر في مسالكها"')
search('زكي قنصل "ينبو به في الليل مضجعه"')
