#coding: utf-8
#requirement: Pillow

import urllib.request
import html.parser
import time
import tkinter
import PIL.Image
import PIL.ImageTk

app = None
img = None
img_name = ""
# img2= None
url = ""


#class Img(PIL.ImageTk.PhotoImage):
#    def __del__(self):
#        PIL.ImageTk.PhotoImage.__del__(self)
#        print("Deleted PhotoImg")

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

class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def log(self,s):
        print(s)
        self.helloLabel.config(text = s)

    def fetch_bipic(self):
        global img_name

        self.log("发送请求...")
        r = urllib.request.urlopen("https://cn.bing.com")
        self.log("请求完毕,开始解析")
        pic_parser = PicParser()
        pic_parser.feed(r.read().decode('UTF-8'))
        r.close()

        img_name = "bipic%d.jpg" % ( int(time.time()) )
        self.log("正在保存图片" + img_name + "...")
        urllib.request.urlretrieve(url,img_name)
        self.log("保存完毕")
        return img_name

    def get(self):
        global img
        path = self.fetch_bipic()
        img = PIL.ImageTk.PhotoImage(PIL.Image.open(path))
        # img2 = Img(PIL.Image.open(path))
        self.imgLable.config(image = img)

    def createWidgets(self):
        self.helloLabel = tkinter.Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.imgLable = tkinter.Label(self, text='Waiting for the picture')
        self.imgLable.pack()
        self.getButton = tkinter.Button(self, text='Get', command=self.get)
        self.getButton.pack()
        self.quitButton = tkinter.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

if __name__ == "__main__":
    app = Application()
    # 设置窗口标题:
    app.master.title('GetCNBingPic')
    # 主消息循环:
    app.mainloop()
