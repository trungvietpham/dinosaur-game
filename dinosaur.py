from os import close, truncate
from numpy import true_divide
import pygame
pygame.init()
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dinosaur')
WHITE = (255,255,255)
RED = (255,0,0)

#set location for components
background_x =0
background_y = 0
dinosaur_x = 0
dinosaur_y = 220
tree_x = 550
tree_y = 227
x_velocity = 5 #pixel per frame
y_jump = 7 #Độ cao để nhảy

jump=False
pausing=False

clock = pygame.time.Clock()

running = True

background = pygame.image.load('material/background.jpg')
dinosaur = pygame.image.load('material/dinosaur.png')
tree = pygame.image.load('material/tree.png')
sound_jump= pygame.mixer.Sound('material/tick.wav')
sound_game_over = pygame.mixer.Sound('material/te.wav')

#Ghi điểm 
score = 0
font = pygame.font.SysFont('san', 20)
fontOver = pygame.font.SysFont('san', 40)

while running: #Trong khi chơi: 

    clock.tick(60) #FPS
    screen.fill(WHITE) #Đổ màu trắng cho giao diện 

    #setup 2 background để liên tục thay phiên nhau hiển thị lên màn hình 
    background1_rect = screen.blit(background, (background_x, background_y)) 
    background2_rect = screen.blit(background, (background_x+width, background_y))
    
    dinosaur_rect = screen.blit(dinosaur, (dinosaur_x, dinosaur_y))
    tree_rect = screen.blit(tree, (tree_x, tree_y))

    score_txt = font.render("Score:"+str(score),True, RED)
    screen.blit(score_txt, (5,5))

    #Cho đối tượng di chuyển
    background_x-=x_velocity
    if background_x+width<=0:
        background_x=0 #reset tọa độ của background về background kế tiếp

    #Kiểm tra vị trí dinosaur và cho phép nhảy
    if 220 >= dinosaur_y>=80:
        if jump==True:
            dinosaur_y-=y_jump
    else:
        jump=False
    
    if dinosaur_y<220:
        if jump==False:
            dinosaur_y+=y_jump

    #Kiểm tra nếu chạm vào cây thì thua 
    if dinosaur_rect.colliderect(tree_rect): 
        pausing = True
        gameover_txt = fontOver.render("GAME OVER" + "\n Press space to play again",True, RED)
        screen.blit(gameover_txt, (200, 150))
        pygame.mixer.Sound.play(sound_game_over)
        x_velocity=0
        y_jump=0
    
    tree_x -= x_velocity 
    if tree_x <=-20: #khi cây chạy hết màn hình 
        tree_x = 550 #Cho cây tiếp theo xuất hiện 
        score+=1 #Tăng điểm lên 1

    for event in pygame.event.get(): #nhận sự kiện  
        if event.type == pygame.QUIT: #Ấn vào nút thoát 
            running = False
        if event.type == pygame.KEYDOWN: #Ấn vào bàn phím
            if event.key == pygame.K_SPACE:
                if dinosaur_y == 220: #đang đứng ở mặt đất
                    pygame.mixer.Sound.play(sound_jump)
                    jump=True #cho phép nhảy
            
            if pausing==True:
                background_x =0
                background_y = 0
                dinosaur_x = 0
                dinosaur_y = 220
                tree_x = 550
                tree_y = 227
                x_velocity = 5 #pixel per frame
                y_jump = 7 #Độ cao để nhảy

                jump=False    
                pausing=False

                score=0

    
    pygame.display.flip()

pygame.quit() #Xóa khi kết thúc
