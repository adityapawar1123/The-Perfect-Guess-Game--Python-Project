import random 
import os 
import time

# Set the environment variable BEFORE importing pygame
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame


def endgame_hint() : 
    pygame.init()
    n = random.randint(1, 22) #Cuz we have 22 voicelines
    dirname = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(dirname, "voicelines", "jokingo", "endgame_hints", f"line_{n}.wav")
    script_path = os.path.join(dirname, "voicelines", "jokingo", "endgame_hints", f"line_{n}.txt")
    
    with open(script_path) as f : 
        script = f.read()

    print(f"\nMysterious voice : {script}")
    line = pygame.mixer.Sound(audio_path)
    line.play()
    time.sleep(line.get_length() + 2.5)

