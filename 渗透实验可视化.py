import random
import pygame

pygame.init()       #开头必备
keep_going=True
gawidth=1200       #游戏窗口大小常量
gaheight=900
screen=pygame.display.set_mode([gawidth,gaheight])       #创建游戏窗口
water=pygame.image.load("water.bmp")       #导入图片在同目录下
space=pygame.image.load("space.bmp")       #导入图片在同目录下
stone=pygame.image.load("stone.bmp")       #导入图片在同目录下
BLACK=(0,0,0)       #填充颜色
WHITE=(255,255,255)
timer=pygame.time.Clock()
picw=water.get_width()
pich=water.get_height()
font=pygame.font.SysFont('Time',50)
x0=100
y0=100

n = 10
m=-1
size = n * n
block = 40
ls = [['-' for ti in range(n)] for tj in range(n)]  # list
for i in range(block):
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    ls[x][y] = '*'

def select(ls,i,j):  #由i，j从列表中定位元素，返回该元素名字，水，石头，空间
    if ls[i][j]=='o':
        return water
    if ls[i][j]=='-':
        return space
    if ls[i][j]=='*':
        return stone
                

def expend(ls,i, j):#给一个元素位置，水平渗透，尝试修改左右的值
    if j == 0:
        if ls[i][j + 1] == '-':
            ls[i][j + 1] = 'o'
            expend(ls,i, j + 1)
    elif j == n-1:
        if ls[i][j - 1] == '-':
            ls[i][j - 1] = 'o'
            expend(ls,i, j - 1)
    else:
        if ls[i][j - 1] == '-':
            ls[i][j - 1] = 'o'
            expend(ls,i, j - 1)
        if ls[i][j + 1] == '-':
            ls[i][j + 1] = 'o'
            expend(ls,i, j + 1)


def update(ls, i):#更新第i行的列表
    if i == 0:
        for j in range(n):
            if ls[i][j] == '-':
                ls[i][j] = 'o'
    else:
        for j in range(n):  # 垂直渗透
            if ls[i - 1][j] == 'o' and ls[i][j] == '-':
                ls[i][j] = 'o'
        for j in range(n):
            if ls[i][j]=='o':#水平渗透
                expend(ls,i,j)

while keep_going:
    
    for event in pygame.event.get():       #监听退出事件
        if event.type==pygame.QUIT:
            keep_going=False
                        
    screen.fill(BLACK)       #填充背景颜色去掉后将显示轨迹            
    for i in range(n):
        for j in range(n):
            pic=select(ls,i,j)
            picx=x0+(j+1)*picw
            picy=y0+(i+1)*pich
            screen.blit(pic,(picx,picy))       #画图
            
          

    draw_string="NO."+str(m+1)+"times try"
    if m==n-1:
        flag = 0
        for i in range(n):
            if ls[n - 1][i] == 'o':
                flag = 1
            if flag == 0:
                draw_string="NO."+str(m+1)+"times try,and finally failure"
            else:
                draw_string="NO."+str(m+1)+"times try,and finally suceseful"
    
    text=font.render(draw_string,True,WHITE)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y=50
    screen.blit(text,text_rect)


    
    pygame.display.update()       #更新窗口
    timer.tick(1)       #每次循环的时间频率60帧每秒60次
    m+=1
    if m>=n-1:
        m=n-1 
    update(ls,m)     

pygame.quit()       



