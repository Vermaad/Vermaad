import time
import random
import os
import pygame

pygame.init()
pygame.mixer.init()

white =(255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (31, 40, 242)

screen_height =700
screen_width =1100
gameWindow = pygame.display.set_mode((screen_width,screen_height))

bgimg = pygame.image.load('playBack.jpg')
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def text_screen (text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow , color ,snk_list,snake_size):
    for  x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game= False
    while not exit_game:
        gameWindow.fill(white)
        bgimg = pygame.image.load('intro.jpg')
        bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(bgimg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(25)



def gameloop():
    exit_game = False
    game_over = False
    snake_x = 40
    snake_y = 55
    snake_size = 16
    velocity_x = 4
    velocity_y = 4
    snk_list = []
    snk_length = 1
    food_x = random.randint(20,1100)
    food_y = random.randint(20,700)
    score = 0
    fps = 25

    if (not os.path.exists('highscore.txt')):
        with open ('highscore.txt','w') as f:
            f.write("0")

    with open('highscore.txt', 'r') as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open('highscore.txt','w') as f:
                f.write(str(highscore))

            gameWindow.fill(white)
            antim = pygame.image.load('GameOver.jpg')
            antim = pygame.transform.scale(antim, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(antim, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('back.mp3')
                        pygame.mixer.music.play()
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y=0

                    if event.key == pygame.K_LEFT:
                        velocity_x =-10
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score+=5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) <14 and abs(snake_y - food_y)<14:
                score +=1
                food_x = random.randint(20,1100)
                food_y = random.randint(20,700)
                snk_length+=1
                pygame.mixer.music.load('food.wav')
                pygame.mixer.music.play()


                if score>int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen('Score: '+ str(score) + '   Hiscore: '+str(highscore),blue,8,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,13,13])

            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over= True
                pygame.mixer.music.load('gameOver.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameOver.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow,black,snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()