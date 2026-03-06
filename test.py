import pygame

pygame.mixer.init()
pygame.mixer.music.load("data/music/Of-Legends-and-Fables-3_LoFi-1.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, fade_ms=2000)

input("Press Enter to stop...")
pygame.mixer.music.fadeout(1000)