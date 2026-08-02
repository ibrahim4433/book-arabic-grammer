import urllib.request
import urllib.parse
import json

query = urllib.parse.quote("الملايين التي تكدح لا تحلم في موت فراشة أحزان البنفسج")
url = f"https://html.duckduckgo.com/html/?q={query}"
req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
)

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html[:2000])
except Exception as e:
    print(e)
