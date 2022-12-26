import pygame
from pygame.locals import *
from pygame import mixer
import random
import math
from sys import exit

pygame.init()
mixer.init()

screen = pygame.display.set_mode((600, 600))
icon = pygame.image.load("Coin Racer/Graphics/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Coin Racer")

# Clock
clock = pygame.time.Clock()

# Sound
mixer.music.load('Coin Racer/Audio/03-Stargunner-Main-Title.wav')
mixer.music.play(-1)


# Score
score = 0
textX = 10
textY = 2
font = pygame.font.Font("freesansbold.ttf", 32)

def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))

# Player
playerImg = pygame.image.load("Coin Racer/Graphics/spaceship.png")
playerX = 268
playerY = 500
player_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemy
enemyImg = pygame.image.load("Coin Racer/Graphics/enemy.png")
enemyX = random.randrange(10, 526)
enemyY = -65
enemy_change = 1.1

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Other Enemy
enemyImg1 = pygame.image.load("Coin Racer/Graphics/monster.png")
enemyX1 = random.randint(10, 526)
enemyY1 = -65
enemy_change1 = 1.1

def enemy1(x, y):
    screen.blit(enemyImg1, (x, y))

# Coin
coinImg = pygame.image.load("Coin Racer/Graphics/coin.png")
coinX = random.randint(10, 526)

coinY = -65
coin_change = 1.1

def coin(x, y):
    screen.blit(coinImg, (x, y))

def recheck_x(coin, ENEMY): 
    if  coin == ENEMY or coinX == enemyX1:
        coin = random.randint(10, 526)
        recheck_x(coin, ENEMY)
    
    if ENEMY == enemyX1:
        ENEMY = random.randint(10, 526)
        recheck_x(coin, ENEMY)

recheck_x(coinX, enemyX)

def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    if distance < 64:
        return True
    else:
        return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -1.1
            
            if event.key == pygame.K_RIGHT:
                player_change = 1.1
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_change = 0
            
            if event.key == pygame.K_RIGHT:
                player_change = 0
    
    enemy_collision = isCollision(enemyX, enemyY, playerX, playerY)
    
    if enemy_collision:
        print("Game Over!")
        print("Score: " + str(score))
        pygame.quit()
        exit()
    
    coin_collision = isCollision(coinX, coinY, playerX, playerY)
    
    if coin_collision:
        coin_sound = mixer.Sound("Coin Racer/Audio/Mario-coin-sound.wav")
        coin_sound.play()
        coinY = -65
        coinX = random.randint(10, 526)
        coin(coinX, coinY)
        screen.fill((0, 128, 128))
        enemy(enemyX, enemyY)
        enemy1(enemyX1, enemyY1)
        score +=1

    enemy1_collision = isCollision(enemyX1, enemyY1, playerX, playerY)

    if enemy1_collision:
        print("Game Over!")
        pygame.quit()
        exit()

    playerX += player_change
    player(playerX, playerY)
    if playerX <= 10:
        playerX = 10
    
    elif playerX >= 526:
        playerX = 526

    enemyY += enemy_change
    enemy(enemyX, enemyY)
    
    if enemyY >= 601:
        enemyY = -65
        enemyX = random.randint(10, 526)
        screen.fill((0, 128, 128))
        enemy(enemyX, enemyY)

    enemyY1 += enemy_change1
    enemy1(enemyX1, enemyY1)
    if enemyY1 >= 601:
        enemyY1 = -65
        enemyX1 = random.randint(10, 526)
        screen.fill((102, 255, 102))
        enemy(enemyX1, enemyY1)    
    
    screen.fill((0, 128, 128))
    enemy(enemyX, enemyY)
    enemy1(enemyX1, enemyY1)
    player(playerX, playerY)
    show_score(textX, textY)
    
    coinY += coin_change
    coin(coinX, coinY)
    if coinY >= 601:
        coinY = -65
        coinX = random.randint(10, 526)
        screen.fill((0, 128, 128))
        coin(coinX, coinY)
    
    pygame.display.update()
    clock.tick(600)