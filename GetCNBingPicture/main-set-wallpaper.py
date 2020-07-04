# coding: utf-8

import urllib.request
import html.parser
import time
import platform
import ctypes
import os

url = ""

def get_attr(attrs,key):
    for i in attrs:
        if i[0] == key:
            return i[1]
    # 如果没有
    print("没有找到属性:",key)
    exit(-1)

class PicParser(html.parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        global url
        if tag == "div" and ('id','bgImgProgLoad') in attrs:
            print("got bgImgProgLoad")

            url = "https://cn.bing.com" + get_attr(attrs,"data-ultra-definition-src") 
            print("获得图片URL:",url)

# def set_wallpaper(filepath):
# # Requirement: Python 3.8
#     if (os := platform.uname().system) == 'Windows':
#         return ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
#     else:
#         print(f"{os} platform is not supported.")

def set_wallpaper(filepath):
    if platform.uname().system == 'Windows':
        return ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
    else:
        print(f"{platform.uname().system} platform is not supported.")

print("发送请求...")
r = urllib.request.urlopen("https://cn.bing.com")
print("请求完毕,开始解析")
pic_parser = PicParser()
pic_parser.feed(r.read().decode('UTF-8'))
r.close()

pic_name = "bipic%d.jpg" % ( int(time.time()) )
print("正在保存图片",pic_name,"...")
urllib.request.urlretrieve(url,pic_name)
print("保存完毕")
print("正在设置壁纸...")
set_wallpaper(os.path.abspath(pic_name))
print("设置壁纸完毕")