# -*- coding:utf-8 -*-
'''developped by huangjinging independently  2333333333333333333333'''
import pygame
from pygame.locals import *
from sys import exit
from time import sleep
import random 
import pickle

#计分
score=-1
#pipe长度组合
list_path=[(50,350),(150,250),(200,200),(250,150),(350,50)]
#frog图片路径
frog_path='/img/frog.png'
#ground路径
ground_path='/img/ground.png'
#屏幕宽高
width,height=720,640
pygame.mixer.init()
pygame.init()
screen=pygame.display.set_mode((width,height),0,32)
clock=pygame.time.Clock()
#游戏结束字样
font=pygame.font.SysFont("arial",50)
gameover=font.render("GAME OVER",True,(255,0,0))
#pipe运动速度
v_pipe=0.1
#pipe和frog初始的x，y位置
x_pipe,x_pipe2,y_frog=1080,0,150
#frog和x坐标始终不变
x_frog=200
#frog宽度和高度
width_frog,height_frog=80,64
#输入玩家名字
player_name=str(input('请输入您的名字'))
#死亡条件
def death(y_pipe1,y_pipe2,x_pipe):
    if y_frog+height_frog>=height or y_frog<=0:
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    exit()
                pygame.mixer.music.load('/msc/haha8.mp3')
                pygame.mixer.music.play()
                screen.blit(gameover,(200,270))
                pygame.display.update()
                sleep(2)
                scoreList()
                exit()
    if y_frog<y_pipe1 or y_frog+height_frog>y_pipe2:
        if x_frog<=x_pipe<=x_frog+width_frog:  
            while True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        exit()
                screen.blit(gameover,(200,270))
                pygame.mixer.music.load('/msc/haha8.mp3')
                pygame.mixer.music.play()
                pygame.display.update()
                sleep(2.5)
                scoreList()
#当pipe到头之后重新开始从右往左移动
def repipe():
    global length1,length2
    length1,length2=random.choice(list_path)
    path1='/img/pipe'+str(length1)+'.png'
    path2='/img/pipe'+str(length2)+'.png'
    global pipe1
    global pipe2
    pipe1=pygame.image.load(path1).convert()
    pipe2=pygame.image.load(path2).convert()
    global x_pipe
    x_pipe=720
def repipe2():   
    global length3,length4
    length3,length4=random.choice(list_path)
    path3='/img/pipe'+str(length3)+'.png'
    path4='/img/pipe'+str(length4)+'.png'
    global pipe3
    global pipe4
    pipe3=pygame.image.load(path3).convert()
    pipe4=pygame.image.load(path4).convert() 
    global x_pipe2
    x_pipe2=720 
#将姓名和成绩存入文件，并且给出高分榜，这里用到了序列化
def scoreList():
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    dic=[]
    dic.append((score,player_name))
    f=open('score.txt','rb')
    data=pickle.load(f)
    f.close()
    for i in data:
        dic.append(i)
    dic.sort(reverse=True)
    if len(dic)>=10:
        dic=dic[:10]
    f=open('score.txt','wb')
    pickle.dump(dic,f)
    f.close()
    #成绩显示到屏幕上
    screen.fill((0,0,0))
    #出现了为True，否则为False
    flag=False
    while True:
        count=1
        for item in dic:
            font=pygame.font.SysFont('arial',25)
            if count<10:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        exit()
                if score==item[0] and player_name==item[1] and not flag:
                    result=font.render(str(count)+' '*10+item[1]+' '*(25-len(item[1])),True,(255,0,0))
                else:
                    result=font.render(str(count)+' '*10+item[1]+' '*(25-len(item[1])),True,(255,255,255))
                screen.blit(result,(width//2-150,30*count+50))
                if score==item[0] and player_name==item[1] and not flag:
                    result=font.render(str(item[0]),True,(255,0,0))
                    flag=True
                else:
                    result=font.render(str(item[0]),True,(255,255,255))
                screen.blit(result,(width-200,30*count+50))
                count+=1
            else:
                #当前玩家的成绩
                if score==item[0] and player_name==item[1] and not flag:
                    result=font.render(str(count)+' '*10+item[1]+' '*(25-len(item[1])),True,(255,0,0))
                else:
                    result=font.render(str(count)+' '*10+item[1]+' '*(25-len(item[1])),True,(255,255,255))
                screen.blit(result,(width//2-160,30*count+50))
                if score==item[0] and player_name==item[1] and not flag:
                    result=font.render(str(item[0]),True,(255,0,0))
                    flag=True
                else:
                    result=font.render(str(item[0]),True,(255,255,255))
                screen.blit(result,(width-200,30*count+50))
                count+=1
        if flag==False:
            font=pygame.font.SysFont('arial',30)
            result=font.render('Your score is too low to show in this ranklist! Keep up!',True,(255,255,0))
            screen.blit(result,(width//2-300,height-100))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    exit()
        
#载入模式选择图片
mode_easy=pygame.image.load('/img/easy.png').convert()
mode_common=pygame.image.load('/img/common.png').convert()
mode_difficult=pygame.image.load('/img/difficult.png').convert()
mode_hard=pygame.image.load('/img/hard.png').convert()
#模式图片的宽高
mode_width,mode_height=250,80
#显示游戏简介
start=pygame.image.load('/img/start.png').convert()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    font=pygame.font.SysFont('arial',25)
    text0=font.render('Brief Introduction',True,(185,185,185))
    text1=font.render('This game is developped by HuangJingping.How to play it',True,(185,185,185))
    text2=font.render('is very easy.Click the mouse to control the flybird,click',True,(185,185,185))
    text3=font.render('the left button to make the flyfrog fly upper,right button',True,(185,185,185))
    text4=font.render('to make it fly lower.',True,(185,185,185))
    screen.blit(text0,(width//2-150,150))
    screen.blit(text1,(width//2-300,200))
    screen.blit(text2,(width//2-300,250))
    screen.blit(text3,(width//2-300,300))
    screen.blit(text4,(width//2-300,350))
    screen.blit(start,(width//2-100,height-200))
    pressed=pygame.mouse.get_pressed()
    #当按下鼠标左键时
    if pressed[0]:
        pos=pygame.mouse.get_pos()
        #点击坐标在start图标区域内时
        if width//2-100<=pos[0]<=width//2-100+150 and height-200<=pos[1]<=height-200+80:
            sleep(1)
            break
    pygame.display.update()
#选择模式
while True:
    global mode
    screen.fill((220,220,220))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()   
    slot=10
    y_temp=(height-mode_height*4-slot*3)//2
    x_temp=(width-mode_width)//2
    screen.blit(mode_easy,(x_temp,y_temp))
    screen.blit(mode_common,(x_temp,y_temp+mode_height+slot))
    screen.blit(mode_difficult,(x_temp,y_temp+mode_height*2+slot))
    screen.blit(mode_hard,(x_temp,y_temp+mode_height*3+slot))
    #获取鼠标点击位置,不同模式导入不同音乐
    pressed=pygame.mouse.get_pressed()
    if pressed[0]:
        pos=pygame.mouse.get_pos()
        if x_temp<pos[0]<x_temp+mode_width:
            if y_temp<pos[1]<y_temp+mode_height:
                mode='easy'
                pygame.mixer.music.load('/msc/music1.mp3')
                break
            elif y_temp+mode_height+slot<pos[1]<y_temp+mode_height*2+slot:
                mode='common'
                pygame.mixer.music.load('/msc/music2.mp3')
                break
            elif y_temp+mode_height*2+slot*2<pos[1]<y_temp+mode_height*3+slot*2:
                mode='difficult'
                pygame.mixer.music.load('/msc/music3.mp3')
                break
            elif y_temp+mode_height*3+slot*3<pos[1]<y_temp+mode_height*4+slot*3:
                mode='hard'
                pygame.mixer.music.load('/msc/music4.mp3')
                break
    pygame.display.update()

#初始化pipe
repipe()
repipe2()
#初始化pipe的x
x_pipe,x_pipe2=0,1080
#后两种模式的背景图
frogs=pygame.image.load('/img/frogs.png').convert()
#载入frog图片:这里用了convert_alpha()就不会显示出frog周围的黑框
frog=pygame.image.load(frog_path).convert_alpha()
#载入栏杆
ground=pygame.image.load(ground_path).convert_alpha()
#困难模式
if mode=='difficult':
    v_pipe=0.15
#炼狱模式
if mode=='hard':
    v_pipe=0.2
#播放音乐
pygame.mixer.music.play()

#主运行程序
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    #frog速度
    v_frog=0.15
    if mode=='difficult':
        v_frog=0.4
    if mode=='hard':
        v_frog=0.6
    screen.fill((0,0,0))
    if mode=='easy':
        pass
    elif mode=='common':
        v_pipe+=0.000001
    elif mode=='difficult':
        screen.blit(frogs,(0,0))
        v_pipe+=0.00001
    elif mode=='hard':
        screen.blit(frogs,(0,0))
        v_pipe+=0.00002
    #
    if x_pipe<=-10:
        score+=1
        if mode=='difficult':
            score+=2
        elif mode=='hard':
            score+=4
        repipe()        
    if x_pipe2<=-10:
        score+=1
        if mode=='difficult':
            score+=1
        elif mode=='hard':
            score+=2
        repipe2()
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    #左上角显示分数
    font=pygame.font.SysFont('arial',40)
    show_score=font.render('current scores: %d'%score,True,(0,255,255))
    screen.blit(show_score,(0,0))
    passed_time=2#clock.tick()
    event=pygame.mouse.get_pressed()
    #鼠标左键上升
    if event[0]:
        v_frog=-0.3
        if mode=='difficult':
            v_frog=-0.6
        if mode=='hard':
            v_frog=-0.7
    #鼠标右键快速下降
    elif event[2]:
        y_frog+=0.8
    y_frog+=v_frog*passed_time
    x_pipe-=v_pipe*passed_time
    x_pipe2-=v_pipe*passed_time
    #显示第一对pipe
    screen.blit(pipe1,(x_pipe,0))
    screen.blit(pipe2,(x_pipe,height-length2))
    #显示第二对pipe
    screen.blit(pipe3,(x_pipe2,0))
    screen.blit(pipe4,(x_pipe2,height-length4))
    #显示frog
    screen.blit(frog,(x_frog,y_frog))
    #显示下面的栏杆
    screen.blit(ground,(0,height-60))
    #显示标题
    pygame.display.set_caption("huangjingping's work")
    pygame.display.update()
    #判断frog有没有撞上pipe
    death(length1,height-length2,x_pipe)#传入上面pipe最下端和下面pipe最上端
    death(length3,height-length4,x_pipe2)
    


