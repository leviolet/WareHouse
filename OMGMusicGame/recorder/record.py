# coding: utf-8

import pygame
import random
import json

srcpath = "./resource/"

def now():
    return pygame.time.get_ticks() - startup_time

class music_sign(object):
    def __init__(self,img_path="",channal=0,speed=5,showup_time=0):
        global channals
        global time

        self.img_path = img_path
        self.surface = pygame.image.load(srcpath + img_path).convert()

        # 加入轨道
        self.channal = channal

        self.showup_time = showup_time
        self.speed = speed

        channals[channal].append(self.to_dict())
    
    def show(self):
        if self.status >= 0:
            global screen
            screen.blit(self.surface,(self.x,self.y))
    
    def to_dict(self):
        return {
            "img_path" : self.img_path,
            "channal" : self.channal,
            "speed" : self.speed,
            "showup_time" : self.showup_time
        }
    


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

    # 加载常用的变量
    fpink = "img/sign1.bmp"
    create_sign = music_sign
    # 加载时钟
    fps_clock = pygame.time.Clock()
    startup_time = pygame.time.get_ticks()

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
                    create_sign(
                        fpink,
                        channal= channal_id,
                        speed= 5,
                        showup_time= pygame.time.get_ticks() - startup_time
                    )
                if event.key == pygame.K_1:
                    mus_file = open("./recorder/mus.json","w")
                    json.dump(channals,mus_file,indent=4)
                    print(json.dumps(channals))
                    # pickle.dump()
                    mus_file.close()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # 绘制背景
        screen.blit(surface_background,(0,0))
        screen.blit(surface_line,(0,600))
        
        # 刷新屏幕
        pygame.display.update()
        print("Time:",now(),"FPS:",fps_clock.get_fps(),end='\r')

# Todo
# 会存在\r引起的print的问题，不影响后续
