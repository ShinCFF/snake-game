import pygame
from pygame import mixer
from color import BLACK, BLUE, YELLOW, GREEN, GREY, PINK, MINT, WHITE, RED
pygame.mixer.pre_init(44100,-16,2,512)
pygame.mixer.init()
#Display
screen_width = 600
screen_height = 600
cell_size = 20

#Fruit
numberOfFruits = 100
colorFruit = GREEN

#Initilize Img
background_intro = pygame.image.load('images/background_intro.jpg')
background_intro = pygame.transform.scale(background_intro, (800,600))
iconImg = pygame.image.load('images/snake.png')
winnerImg = pygame.image.load('images/win.jpg')
winnerImg = pygame.transform.scale(winnerImg, (600,600))
pause_icon = pygame.image.load('images/pause_icon.jpg')
pause_icon = pygame.transform.scale(pause_icon, (30, 30))
pause_icon_rect = pause_icon.get_rect(center = (550, 30))
pause_screen = pygame.image.load('images/pause_screen.png')
exit = pygame.image.load('images/exit.jpg')
exit = pygame.transform.scale(exit, (300, 140))
#Initilize sound
movingsound = mixer.sound('sounds/moving.wav')
movingsound.set_volume(0.1)
eatingsound = mixer.sound('sounds/eating.wav')
gameOversound = mixer.sound('sounds/gameOver.flac')
winnersound = mixer.sound('sounds/winner.ogg')
mouseClicksound = mixer.sound('sounds/mouseClick.wav')
crashsound = mixer.sound('sounds/crash.mp3')
crashsound.set_volume(0.1)

