import urllib.request
import urllib.parse
import json

def search(query):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.find_all('a', class_='result__snippet')
        for r in results:
            print(r.text)
    except Exception as e:
        print("Error:", e)

search("غمرته الأحلام بالشفق الوردي")
search("هو في ميعة الشباب ولو حدقت")
