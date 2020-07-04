
import pygame.time
import pygame.mixer

# 初始化
pygame.mixer.init()

# 加载默认音效
default_sound = pygame.mixer.Sound("default_typingsound.ogg")

def coolprint(
        content,
        milsec=150,
        after_milsec=1000,
        top = 0,
        left = 0,
        typing_sound=default_sound,
    ):

    # 打印边距
    print(
        '\n' * top,
        ' ' * left,
        end='',
    )

    # 无限循环播放音效
    typing_sound.play(loops=-1)
    
    # 逐个打印字符串,并延时
    for i in content:
        print(i,end='',flush=True)
        pygame.time.wait(milsec)

    # 换行
    print('')

    # 停止播放音效,停顿一会儿
    typing_sound.stop()
    pygame.time.wait(after_milsec)

def print_color(s,color=37):
    result = "echo \x1b[%dm" % color   # 改变颜色
    result += s                        # 打印内容
    result += "\x1b[37m"               # 恢复原来的颜色
    system(result)                     # 执行命令

# 以下内容只是用来显示提示,没有别的作用
if __name__=="__main__":
    notice = '''
    欢迎使用coolprint模块,实现电影中的'炫酷'打印方式,就像这样
    导入
        将coolprint.py放到你的Python文件的同一文件夹下
        并导入:
        from coolprint import coolprint
    使用方法:
        coolprint(content,milsec,after_milsec,top,left,typing_sound)
    参数说明:
        content: 你要打印的内容               字符串
        milsec:  每一个字的时间(毫秒)         整形
        after_milsec:打印完后停顿的时间(毫秒) 整形
        top:     间隔几行                     整形
        left:    左边间距几个字符             整形
    其中只有第一个参数是必须的
    示例:
        from coolprint import coolprint
        coolprint("Hello")
    '''
    coolprint(notice)
