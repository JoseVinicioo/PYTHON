import pygame
import emoji
from time import sleep
print('-_-'*12)
print('CONTAGEM REGRESSIVA PARA O ANO NOVO')
print('-_-'*12)
for c in range(10 , 0 , -1):
    sleep(1)
    print(c)
sleep(1.2)
pygame.init()
pygame.mixer.music.load('ex046fogos.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
print(emoji.emojize(':fireworks:'*8))
print(' FELIZ ANO NOVO!!')
print(emoji.emojize(':fireworks:'*8))
input()
pygame.event.wait()
