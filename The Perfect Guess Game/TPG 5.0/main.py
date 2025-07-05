import pygame 
import pyttsx3
engine = pyttsx3.init()
import time

def set_female_voice():
    voices = engine.getProperty('voices')
    # Try setting the first available female voice (you might need to tweak the index)
    for voice in voices:
        if "zira" in voice.id.lower():  # Adjust as needed
            engine.setProperty('voice', voice.id)
            break

set_female_voice()
def tts(text) : 
   engine.say(text)
   print(text)
   engine.runAndWait()

def only_tts(text) :
   engine.say(text)
   engine.runAndWait() 

def fade(screen, fade_in=True, speed=10, color=(0, 0, 0)):
    fade_surface = pygame.Surface((screen.get_width(), screen.get_height())) #This creates a brand new surface the size of the screen
    fade_surface.fill(color)

    if fade_in:
        alpha_range = range(0, 256, speed) #0 is fully transparent, 255 is fully opaque, so invisible -> opaque
        #The speed decides how big the jumps are in each step. Smaller = smoother.
    else:
        alpha_range = range(255, -1, -speed) #opaque -> invisible

    for alpha in alpha_range:
        fade_surface.set_alpha(alpha) #sets how transparent the surface is. More alpha = more opaque
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)  # controls the speed of fade effect


import os
file_path = os.path.abspath(__file__) #Gives absolute path of main.py
dir_path = os.path.dirname(file_path) #Gives absolute path of our folder in which main.py is present
endgame_unlock_path = os.path.join(dir_path, "modes", "endgame_mode", "endgame_unlock.txt")
endgame_hinter_unlocker_path = os.path.join(dir_path, "data", "endgame_hinter_unlocker.txt")
# Set the environment variable BEFORE importing pygame
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from audio import audio #imports audio.py as a module
import threading

def music_thread(func, file, duration=-1) :  #duration -1 default i.e. on infinite loop
   thread = threading.Thread(target=func, args=(file, duration), daemon=True)
   thread.start()

music_thread(audio.menu_music, "menu_music.wav") #Runs menu music on an infinite loop 


from data.prompts import common_prompts
from UI.utils import Button

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

fps = 60 

pygame.display.set_caption("The Perfect Guess")
pygame.display.update 

clock = pygame.time.Clock()

def game_mode() : 
   bkg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "UI", "ui")
   raw_bkg = [
      pygame.image.load(os.path.join(bkg_path, "01_mode_bkg.png")),
      pygame.image.load(os.path.join(bkg_path, "02_mode_bkg.png")),
      pygame.image.load(os.path.join(bkg_path, "03_mode_bkg.png"))
   ]

   bkg = [
      pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()
      for img in raw_bkg
   ]
   frame = bkg[0]
   
   quit_screen_bkg_raw = [
      pygame.image.load(os.path.join(bkg_path, "01_quit_screen_bkg.png")),
      pygame.image.load(os.path.join(bkg_path, "02_quit_screen_bkg.png")),
      pygame.image.load(os.path.join(bkg_path, "03_quit_screen_bkg.png"))
   ]

   quit_screen_bkg = [ 
      pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()
      for img in quit_screen_bkg_raw
   ]
   quit_screen_frame = quit_screen_bkg[0]
   

   IDLE_TIME = 2000 #in ms
   FRAME_DURATION = 300

   last_cycle_time = pygame.time.get_ticks()
   # pygame.time.get_ticks() is a func which stores time passed by (in ms) ever since pygame.init() was called
   anim_playing = False 

   mode_exit = False 

   yes_button = Button("01_yes.png", "02_yes.png", "03_yes.png", 
                        (0.10, 0.75), screen, screen_width, screen_height)
   no_button = Button("01_no.png", "02_no.png", "03_no.png", 
                        (0.25, 0.75), screen, screen_width, screen_height)
   quit_button_mode = Button("01_quit.png", "02_quit.png", "03_quit.png", 
                        (0.92, 0.865), screen, screen_width, screen_height)
   
   normal_button = Button("01_normal.png", "02_normal.png", "03_normal.png",
                         (0.10, 0.725), screen, screen_width, screen_height)
   timebound_button = Button("01_timebound.png", "02_timebound.png", "03_timebound.png",
                         (0.225, 0.725), screen, screen_width, screen_height)
   gaslight_button = Button("01_gaslight.png","02_gaslight.png", "03_gaslight.png",
                         (0.35, 0.725), screen, screen_width, screen_height)
   endgame_button = Button("01_endgame.png", "02_endgame.png", "03_endgame.png",
                         (0.225, 0.80), screen, screen_width, screen_height)
   secret_button = Button("01_secret_mode.png", "02_secret_mode.png", "03_secret_mode.png", 
                          (0.225, 0.80), screen, screen_width, screen_height)
   secret_button_sound_effect = pygame.mixer.Sound(os.path.join(dir_path, "audio", "sound_effect", "secret_button_sound_effect.wav"))
   
   fade(screen, fade_in=True)
   while not mode_exit : 
      
      current = pygame.time.get_ticks()

      with open(endgame_unlock_path) as f : #Need to keep in loop so if player returns from gaslight/endgame then the buttons will update
         endgame_condition = f.read()
   
      with open(endgame_hinter_unlocker_path) as f : 
         endgame_played = f.read()

      if not anim_playing : # i.e. anim_playing == False 
         if current - last_cycle_time >= IDLE_TIME : 
            anim_playing = True 
            anim_start = current # to track frame duration of each frame in bkg
            frame_index = 0 
         frame = bkg[0]
      
      else : 

         elapsed = current - anim_start
         frame_index = elapsed//FRAME_DURATION

         if frame_index >= len(bkg) : 
            anim_playing = False 
            last_cycle_time = current #So last cycle time gets updated
            frame = bkg[0]

         else : 
            frame = bkg[frame_index]

      screen.blit(frame, (0,0))

      if quit_button_mode.draw() : 
         fade(screen, fade_in=True)
         while True : 
            current = pygame.time.get_ticks()
            screen.blit(quit_screen_frame, (0,0))
            
            if not anim_playing : # i.e. anim_playing == False 
               if current - last_cycle_time >= IDLE_TIME : 
                  anim_playing = True 
                  anim_start = current # to track frame duration of each frame in bkg
                  frame_index = 0 
                  quit_screen_frame = quit_screen_bkg[0]
      
            else : 
               elapsed = current - anim_start
               frame_index = elapsed//FRAME_DURATION

               if frame_index >= len(bkg) : 
                  anim_playing = False 
                  last_cycle_time = current #So last cycle time gets updated
                  quit_screen_frame = quit_screen_bkg[0]

               else : 
                  quit_screen_frame = quit_screen_bkg[frame_index]
            
            if yes_button.draw() : 
               pygame.quit()
               quit()
            if no_button.draw() : 
               break #breaks the inner loop and returns to game selection screen

            for event in pygame.event.get() : 
               if event.type == pygame.QUIT : 
                  pygame.quit()
                  quit()

            pygame.display.flip()
            clock.tick(fps)


      if normal_button.draw() : 
         from modes.normal_mode.normal_mode import normal_mode
         fade(screen, fade_in=True)
         normal_mode(screen, screen_width, screen_height)
         fade(screen, fade_in=True) #Fades to menu after game mode ends
      
      elif timebound_button.draw() : 
         from modes.timebound_mode.timebound_mode import timebound_mode
         fade(screen, fade_in=True)
         timebound_mode(screen, screen_width, screen_height)
         fade(screen, fade_in=True)
      
      elif gaslight_button.draw() : 
         from modes.gaslight_mode.gaslight_mode import gaslight_mode
         fade(screen, fade_in=True)
         gaslight_mode(screen, screen_width, screen_height)
         fade(screen, fade_in=True)
      
      elif endgame_condition == "unlock" : 
         if endgame_button.draw() : 
            from modes.endgame_mode.endgame_mode import endgame_mode 
            fade(screen, fade_in=True)
            endgame_mode(screen, screen_width, screen_height)
            fade(screen, fade_in=True)
      
      elif endgame_condition != "unlock" : 
         if endgame_played != "lock" : 
            if secret_button.draw() : 
               pygame.mixer.music.pause()
               pygame.mixer.Channel(1).set_volume(0.1)
               pygame.mixer.Channel(1).play(secret_button_sound_effect)
               while pygame.mixer.Channel(1).get_busy() : 
                  pygame.time.wait(10)
               time.sleep(1)
               pygame.mixer.music.unpause()
      


      for event in pygame.event.get() : 
         if event.type == pygame.QUIT : 
            pygame.quit()
            quit()
      
      pygame.display.flip()
      clock.tick(fps)

def menu() : 
   
   bkg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "UI", "ui")
   raw_bkg = [
      pygame.image.load(os.path.join(bkg_path, "01_menu_bkg.png")),
      pygame.image.load(os.path.join(bkg_path, "02_menu_bkg.png")),
      pygame.image.load(os.path.join(bkg_path, "03_menu_bkg.png"))
   ]
   
   bkg = [
      pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()
      for img in raw_bkg
   ]
   frame = bkg[0]

   quit_screen_bkg_raw = [
      pygame.image.load(os.path.join(bkg_path, "01_quit_screen_bkg.png")),
      pygame.image.load(os.path.join(bkg_path, "02_quit_screen_bkg.png")),
      pygame.image.load(os.path.join(bkg_path, "03_quit_screen_bkg.png"))
   ]

   quit_screen_bkg = [ 
      pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()
      for img in quit_screen_bkg_raw
   ]
   quit_screen_frame = quit_screen_bkg[0]

   IDLE_TIME = 3500 #in ms
   FRAME_DURATION = 300

   last_cycle_time = pygame.time.get_ticks()
   # pygame.time.get_ticks() is a func which stores time passed by (in ms) ever since pygame.init() was called
   anim_playing = False 

   menu_exit = False 

   start_button = Button("01_start.png", "02_start.png","03_start.png",
                         (0.10, 0.75), screen, screen_width, screen_height)
   quit_button = Button("01_quit.png", "02_quit.png", "03_quit.png",
                         (0.25, 0.75), screen, screen_width, screen_height)
   yes_button = Button("01_yes.png", "02_yes.png","03_yes.png",
                         (0.10, 0.75), screen, screen_width, screen_height)
   no_button = Button("01_no.png", "02_no.png", "03_no.png",
                         (0.25, 0.75), screen, screen_width, screen_height)
   
   while not menu_exit : 
      
      current = pygame.time.get_ticks()

      if not anim_playing : # i.e. anim_playing == False 
         if current - last_cycle_time >= IDLE_TIME : 
            anim_playing = True 
            anim_start = current # to track frame duration of each frame in bkg
            frame_index = 0 
         frame = bkg[0] 
      
      else : 

         elapsed = current - anim_start
         frame_index = elapsed//FRAME_DURATION

         if frame_index >= len(bkg) : 
            anim_playing = False 
            last_cycle_time = current #So last cycle time gets updated
            frame = bkg[0]

         else : 
            frame = bkg[frame_index]

      screen.blit(frame, (0,0))

      if start_button.draw() : 
         game_mode()

      if quit_button.draw() : 
         fade(screen, fade_in=True)
         while True : 
            current = pygame.time.get_ticks()
            screen.blit(quit_screen_frame, (0,0))
            
            if not anim_playing : # i.e. anim_playing == False 
               if current - last_cycle_time >= IDLE_TIME : 
                  anim_playing = True 
                  anim_start = current # to track frame duration of each frame in bkg
                  frame_index = 0 
                  quit_screen_frame = quit_screen_bkg[0]
      
            else : 
               elapsed = current - anim_start
               frame_index = elapsed//FRAME_DURATION

               if frame_index >= len(bkg) : 
                  anim_playing = False 
                  last_cycle_time = current #So last cycle time gets updated
                  quit_screen_frame = quit_screen_bkg[0]

               else : 
                  quit_screen_frame = quit_screen_bkg[frame_index]
            
            if yes_button.draw() : 
               pygame.quit()
               quit()
            if no_button.draw() : 
               break #breaks the inner loop and returns to game selection screen

            for event in pygame.event.get() : 
               if event.type == pygame.QUIT : 
                  pygame.quit()
                  quit()

            pygame.display.flip()
            clock.tick(fps)


      for event in pygame.event.get() :

         if event.type == pygame.QUIT : 
            pygame.quit()
            quit()
      
      pygame.display.flip()
      clock.tick(fps)


menu()