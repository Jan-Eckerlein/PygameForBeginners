from tkinter import Y
import pygame
import os

#modifiable CONSTANTS
SIZE = WIDTH, HEIGHT = 900,500
BORDER_WIDTH = 10
FPS = 60
VEL = 5
SPACESHIP_OFFSET_Y = 15
SPACESHIP_OFFSET_X = 15
BULLETS_MAX = 3
BULLET_VEL = 7
BULLET_SIZE = BULLET_WIDTH, BULLET_HEIGHT = 10, 5

#immutable CONSTANTS
BORDER_START = WIDTH/2 - BORDER_WIDTH/2
BORDER_END = WIDTH/2 + BORDER_WIDTH/2
SPACESHIP_SIZE = SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 46, 32

#COLORS
BORDER_COLOR = (255, 255, 255)
BACKGROUND = (10, 10, 10)

#WINDOW Objects
BORDER = pygame.Rect(BORDER_START, 0, BORDER_WIDTH, HEIGHT)
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("First Game")

#loading Player Images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, SPACESHIP_SIZE), 90)
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, SPACESHIP_SIZE), -90)

def draw_window(yellow, red):
    WIN.fill(BACKGROUND)
    pygame.draw.rect(WIN, BORDER_COLOR, BORDER)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    pygame.display.update()
    
def yellow_move(keys_pressed, rect):
    if keys_pressed[pygame.K_a] and (rect.left - VEL) > 0: #LEFT
        rect.x -= VEL
    if keys_pressed[pygame.K_d] and (rect.right + VEL) < BORDER_START + SPACESHIP_OFFSET_X: #RIGHT
        rect.x += VEL
    if keys_pressed[pygame.K_w] and (rect.top - VEL) > 0: #UP
        rect.y -= VEL
    if keys_pressed[pygame.K_s] and (rect.bottom + VEL) < HEIGHT - SPACESHIP_OFFSET_Y: #DOWN
        rect.y += VEL

def red_move(keys_pressed, rect):
    if keys_pressed[pygame.K_LEFT] and (rect.left - VEL) > BORDER_END: #LEFT
        rect.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and (rect.right + VEL) < WIDTH + SPACESHIP_OFFSET_X: #RIGHT
        rect.x += VEL
    if keys_pressed[pygame.K_UP] and (rect.top - VEL) > 0: #UP
        rect.y -= VEL
    if keys_pressed[pygame.K_DOWN] and (rect.bottom + VEL) < HEIGHT - SPACESHIP_OFFSET_Y: #DOWN
        rect.y += VEL
        
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < BULLETS_MAX:
                    bullet = pygame.Rect(yellow.right, yellow.centery, BULLET_WIDTH, BULLET_HEIGHT)
                    yellow_bullets.append(bullet)
                    
                if event.key == pygame.K_RCTRL and len(red_bullets) < BULLETS_MAX:
                    bullet = pygame.Rect(red.left, red.centery, BULLET_WIDTH, BULLET_HEIGHT)
                    red_bullets.append(bullet)
        
        keys_pressed = pygame.key.get_pressed()
        yellow_move(keys_pressed, yellow)
        red_move(keys_pressed, red)
        
                
        draw_window(yellow, red)
    pygame.quit()

if __name__ == "__main__":
    main()