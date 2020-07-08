#coding : utf-8

import pygame
import json

srcpath = "./resource/"

def now():
    return pygame.time.get_ticks() - startup_time

class music_sign(object):
    def __init__(self,img_path,channal=0,speed=5,showup_time=0):
        global channals
        global time

        self.surface = pygame.image.load(srcpath + img_path).convert()

        # 加入轨道
        self.channal = channal
        channals[channal].append(self)

        self.showup_time = showup_time

        # 位置,速度,状态
        self.y = 0
        self.x = channal * 100
        self.speed = speed
            # 实际速度(像素/秒) = self.speed * 帧率
        self.status = -2
            # 0 正在下落
            # -1 已经错过
            # 1 已经弹奏
            # 2 可被弹奏
            # -2 没有到出现时间

    def move(self):
        global startup_time
        if pygame.time.get_ticks() - startup_time >= self.showup_time:
            self.status = 0
            
        if self.status == -2:
            return False

        if self.y >= 768:
            self.status = -1
        elif self.y <= 600 and self.y >= 500:
            self.status = 2
        
        self.y += self.speed
    
    def show(self):
        if self.status >= 0:
            global screen
            screen.blit(self.surface,(self.x,self.y))


def create_sign_from_dict(d):
    return music_sign(
        img_path = d.get("img_path"),
        channal = d.get("channal"),
        speed = d.get("speed"),
        showup_time = d.get("showup_time"),
    )

def create_signs():
    # 开始设计
    # 实际速度(像素/秒) = self.speed * 帧率
    # showup_time单位为毫秒(1s = 1000ms)
    # channal以0开始,最高为7
    with open("./recorder/mus.json",'r') as json_file:
        channals = json.load(json_file)
        for channal in channals:
            for sign in channal:
                create_sign_from_dict(sign)
        json_file.close()

if __name__ == "__main__":
    score = 500    # 计分
    time = 0       # 计时

    # 初始化
    pygame.init()
    screen = pygame.display.set_mode((1024,768), 0, 32)
    pygame.display.set_caption("OMG MUSIC")

    surface_background = pygame.image.load(srcpath+"img/background.bmp").convert()
    surface_line = pygame.image.load(srcpath+"img/line.bmp").convert()

    # 轨道(通道)
    channal0 = []
    channal1 = []
    channal2 = []
    channal3 = []
    channal4 = []
    channal5 = []
    channal6 = []
    channal7 = []
    channals = (channal0,channal1,channal2,channal3,channal4,channal5,channal6,channal7)

    # 加载音符
    create_signs()

    fps_clock = pygame.time.Clock()
    startup_time = pygame.time.get_ticks()

    # 主循环
    while True:
        fps_clock.tick(60)
        
        tuple_key =(
            pygame.K_a,
            pygame.K_s,
            pygame.K_d,
            pygame.K_f,
            pygame.K_g,
            pygame.K_h,
            pygame.K_j,
            pygame.K_k
        )

        # 处理输入
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in tuple_key:
                    channal_id = tuple_key.index(event.key)
                    for sign in channals[channal_id]:
                        if sign.status == 2:
                            #可被弹奏
                            sign.status = 1
                            score += 20
                            print("channal[%d]弹奏成功,sing.status=%d,分数=%d" % (channal_id,sign.status,score))

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # 绘制背景
        screen.blit(surface_background,(0,0))
        screen.blit(surface_line,(0,600))

        # 绘制音符
        for channal in channals:
            for sign,i in zip(channal,range(len(channal))):
                # 检查是否没有被演奏
                if sign.status in (-1,1):
                    print('移除了一个元素,原因:',sign.status)
                    channal.pop(i)
                else:
                    sign.show()
                    sign.move()
        
        # 刷新屏幕
        pygame.display.update()
        print("Time:",now(),"FPS:",fps_clock.get_fps(),end='\r')

# Todo
# 连按慢速音符轨道导致多次计分
# 会存在\r引起的print的问题，不影响后续
