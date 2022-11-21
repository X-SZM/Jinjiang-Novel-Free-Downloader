# -*- coding:utf-8 -*-
#小说
class get_html:
    import requests
    import re

    url="https://www.xpiaotian.com/book/248717/"
    headers = {
        "User-Agent":"Mozilla  /5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"
    }
    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8'

    x = resp.text
    child_list=[]
    obj = re.compile(r'<a href="(?P<hf>.*?)"', re.S)
    result = obj.finditer(x)
    for it in result:
        a=it.group("hf")
        child_herf = url + a
        print(child_herf)
        child_list.append(child_herf)

    for href in child_list:
        pass


if __name__ == "__main__":
    pass