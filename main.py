import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("hello")
exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('yopu have pressed right arrow key')

pygame.quit()
quit()