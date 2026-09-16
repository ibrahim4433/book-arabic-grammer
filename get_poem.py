import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def search_poem(query):
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

search_poem('زكي قنصل البناء الريح ما تنفك')
