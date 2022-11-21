# -*- coding:utf-8 -*-
def BookGet(links):
    import requests
    import re
    import os

    if not os.path.exists('C:/X-SZM晋江免费文下载'):
        os.mkdir("C:/X-SZM晋江免费文下载")


    url=links
    headers = {
        "User-Agent":"Mozilla  /5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"
    }
    resp=requests.get(url,headers=headers)
    resp.encoding='gbk'

    page = resp.text
    obj = re.compile(r'<div style="clear:both;">.*?</div>(?P<word>.*?)<div id="favoriteshow_3" style="display:none" align="center"></div>', re.S)
    tt = re.compile(r"<h2>(?P<title>.*?)</h2>")
    title = tt.finditer(page)
    parts = obj.finditer(page)
    for t in title:
        title = t.group("title")
        print(title)
    for i in parts:
        w = i.group("word")
        wx = w.replace("<br>", "\r\n")
        print(wx)
        filename = title
        with open(r"C:/X-SZM晋江免费文下载/{}.txt".format(title), 'w', encoding='gbk') as f:
            f.write(title)
            f.write(wx)
