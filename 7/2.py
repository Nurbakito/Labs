import pygame
import os

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("musicPlayer")
icon = pygame.image.load("music_icon.png")
pygame.display.set_icon(icon)

path = [
    "music1.mp3",
    "music2.mp3",
    "music3.mp3",
]

current_index = 0
pygame.mixer.music.load(path[current_index])


def play_music():
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()


def unpause_music():
    pygame.mixer.music.unpause()


def play_next():
    global current_index
    current_index = (current_index + 1) % len(path)
    pygame.mixer.music.load(path[current_index])
    play_music()


def play_previous():
    global current_index
    current_index = (current_index - 1) % len(path)
    pygame.mixer.music.load(path[current_index])
    play_music()

running = True
while running:
    screen.fill((255, 255, 255))  

    pygame.draw.circle(screen, "black", (250, 150), 50)
    pygame.draw.rect(screen, (0, 0, 0), (80, 100, 120, 100))  
    pygame.draw.rect(screen, (0, 0, 0), (300, 100, 120, 100))  

    pygame.display.update()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pause_music()
                else:
                    unpause_music()
            elif event.key == pygame.K_RIGHT:
                play_next()
            elif event.key == pygame.K_LEFT:
                play_previous()
pygame.quit()
