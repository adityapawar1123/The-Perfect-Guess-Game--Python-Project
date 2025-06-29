import os
import threading
import time

# Set the environment variable BEFORE importing pygame
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame 

'''
Using pygame.mixer.music for sound effects = not ideal
Using pygame.mixer.music for both music and sound effects, but mixer.music is meant for background music only
'''
pygame.mixer.init()

def menu_music(file, duration=-1, fade_in = 1000) : #default duration is -1 i.e. infinite loop
    folder = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(folder, "music", "menu", file)
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(0.7) #Max volume value is 1
    pygame.mixer.music.play(duration, fade_ms=fade_in) #runs infinitely i.e. on loop
#fade_ms fades in the music for seamless transition, I've set the default fade to 1000ms for this functn i.e. 1sec

def normal_mode_music(file, duration=-1, fade_in=2250) : 
    folder = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(folder, "music", "normal_mode", file)
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(0.85)
    pygame.mixer.music.play(duration, fade_ms=fade_in)

def timebound_mode_music(file, duration=-1, fade_in=2250) : 
    folder = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(folder, "music", "timebound_mode", file)
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(1.2)
    pygame.mixer.music.play(duration, fade_ms=fade_in)

def gaslight_mode_music(file, duration=-1, fade_in=2250) : 
    folder = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(folder, "music", "gaslight_mode", file)
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(0.85)
    pygame.mixer.music.play(duration, fade_ms=fade_in)

def endgame_mode_music(file, duration=-1, fade_in=2250, volume=0.85) : 
    folder = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(folder, "music", "endgame_mode", file)
    if file == "endgame_pleasant.wav" : 
        volume = 0.6 #because we're playing this only in the bkg when character is speaking
    
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(duration, fade_ms=fade_in)

def sound_effects(file) : 
    folder = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(folder, "sound_effect", file)
    sound = pygame.mixer.Sound(path)
    sound.set_volume(1.0)
    sound.play() #Plays the sound once and exits the file 
#If you ever wanna loop a sound then use this : 
#           sound.play(loops=-1)  # loops forever
#           sound.play(loops=3)   # plays 4 times (3 loops + 1 original)
