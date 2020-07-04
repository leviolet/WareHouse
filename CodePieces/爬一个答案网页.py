# coding:  utf-8
# author:  leviolet
# license: MIT

import requests
import pyquery

def getOne(url: str):
    print(f"获取:{url}")
    headers = {
        'user-agent': r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        'Accept-Charset': r"utf-8"
    }
    r=None
    try:
        r = requests.get(url, headers=headers, timeout=30)
    except requests.exceptions.RequestException as e:
        print(e)
        return f"获取 {url} 失败\n"
    if r.status_code >= 300:
        print(f"请求失败: {r.status_code}")
        f"获取 {url} 失败\n"

    s = r.content.decode('gbk')
    #print(s)

    document = pyquery.PyQuery(s)
    p = document('#mainBody > div.contentbox')
    p.find(".mainstory").remove()
    print(p.text())
    return p.text()

f = open(r"./data.txt","w",encoding='utf-8')

for i in (2,20):
    url = r"https://3gmfw.cn/article/html2/2020/03/31/519097" + f"_{i}" + ".html"
    text = getOne(url)
    f.write(text)

for i in (2,17):
    url = r"https://3gmfw.cn/article/html2/2020/03/31/519098" + f"_{i}" + ".html"
    text = getOne(url)
    f.write(text)

f.close()