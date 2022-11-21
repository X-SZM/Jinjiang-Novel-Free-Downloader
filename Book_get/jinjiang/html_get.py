# -*- coding:gbk -*-
#С˵
# -*- coding:utf-8 -*-
def HtmlGet(input_url):
    from book_get import BookGet
    import requests
    import re

    url = input_url
    headers = {
        "User-Agent":"Mozilla  /5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"
    }
    resp=requests.get(url,headers=headers)
    resp.encoding='gbk'

    #print(resp.text)

    x = resp.text
    child_list=[]
    obj = re.compile(r'<a itemprop="url" href="(?P<hf>.*?)"', re.S)

    result = obj.finditer(x)
    for it in result:
        links = it.group("hf")
        BookGet(links)



if __name__ == "__main__":
    HtmlGet()