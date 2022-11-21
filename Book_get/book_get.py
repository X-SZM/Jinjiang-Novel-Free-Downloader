import requests
import re


url="https://www.xpiaotian.com/book/248717/98713953.html"
headers = {
    "User-Agent":"Mozilla  /5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"
}
resp=requests.get(url,headers=headers)
resp.encoding='utf-8'

page = resp.text
obj = re.compile(r"&nbsp;&nbsp;&nbsp;&nbsp;(?P<word>.*?)<br/>", re.S)
parts = obj.finditer(page)
for i in parts:
    w = i.group("word")
    print(w)