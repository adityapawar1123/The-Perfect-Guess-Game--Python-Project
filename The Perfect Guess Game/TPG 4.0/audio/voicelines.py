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

def endgame_kate_intro() : 
    path = os.path.join("audio", "voicelines", "kate", "endgame_intro", "kate_endgame_intro.wav")
    intro = pygame.mixer.Sound(path)
    intro.set_volume(0.7) #Volume at 70%
    intro.play()
    time.sleep(intro.get_length())

def endgame_jokingo_reveal() : 
    path = os.path.join("audio", "voicelines", "jokingo", "endgame_reveal", "jokingo_reveal.wav")    
    intro = pygame.mixer.Sound(path)
    intro.set_volume(0.9) 
    intro.play()
    time.sleep(intro.get_length() + 2)

def endgame_kate_attempts(attempts_left) : 
    path = os.path.join("audio", "voicelines", "kate", "endgame_attempts", f"attempt_{attempts_left}.mp3")
    script_path = os.path.join("audio", "voicelines", "kate", "endgame_attempts", f"attempt_{attempts_left}.txt")
    with open(script_path) as f : 
        script = f.read()

    attempt = pygame.mixer.Sound(path)
    attempt.set_volume(0.8)
    print("\n",script,"\n")
    pygame.mixer.music.set_volume(0.4)
    attempt.play()
    pygame.mixer.music.set_volume(0.8)
    time.sleep(attempt.get_length() + 1.5)

def endgame_win() : 
    kate_path = os.path.join("audio", "voicelines", "kate", "endgame_win", "kate_endgame_win.wav")
    jokingo_path = os.path.join("audio", "voicelines", "jokingo", "endgame_win", "jokingo_endgame_win.wav")
    
    pygame.mixer.music.stop()

    jokingo = pygame.mixer.Sound(jokingo_path)
    jokingo.play()
    time.sleep(jokingo.get_length() + 1.5)
    
    kate = pygame.mixer.Sound(kate_path)
    kate.play()
    time.sleep(kate.get_length() + 2)

def endgame_lose() : 
    kate_path = os.path.join("audio", "voicelines", "kate", "endgame_lose", "kate_endgame_lose.wav")
    jokingo_path = os.path.join("audio", "voicelines", "jokingo", "endgame_lose", "jokingo_endgame_lose.wav")

    pygame.mixer.music.stop()

    jokingo = pygame.mixer.Sound(jokingo_path)
    jokingo.play()
    time.sleep(jokingo.get_length() + 1.5)
    
    kate = pygame.mixer.Sound(kate_path)
    kate.play()
    time.sleep(kate.get_length() + 2)





