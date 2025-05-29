import pygame 
import pyttsx3
engine = pyttsx3.init()

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

import os
file_path = os.path.abspath(__file__) #Gives absolute path of main.py
dir_path = os.path.dirname(file_path) #Gives absolute path of our folder in which main.py is present
endgame_unlock_path = os.path.join(dir_path, "modes", "endgame_mode", "endgame_unlock.txt")
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

   IDLE_TIME = 3500 #in ms
   FRAME_DURATION = 300

   last_cycle_time = pygame.time.get_ticks()
   # pygame.time.get_ticks() is a func which stores time passed by (in ms) ever since pygame.init() was called
   anim_playing = False 

   mode_exit = False 

   normal_button = Button("01_normal.png", "02_normal.png", "03_normal.png",
                         (0.10, 0.70), screen, screen_width, screen_height)
   timebound_button = Button("01_timebound.png", "02_timebound.png", "03_timebound.png",
                         (0.25, 0.70), screen, screen_width, screen_height)
   
   with open(endgame_unlock_path) as f : 
      endgame_condition = f.read()
   
   if endgame_condition == "unlock" : 
      gaslight_button = Button("01_gaslight.png","02_gaslight.png", "03_gaslight.png",
                         (0.10, 0.80), screen, screen_width, screen_height)

      endgame_button = Button("01_endgame.png", "02_endgame.png", "03_endgame.png",
                         (0.25, 0.80), screen, screen_width, screen_height)
   
   else : 
      gaslight_button = Button("01_gaslight.png", "02_gaslight.png", "03_gaslight.png",
                         (0.175, 0.80), screen, screen_width, screen_height)
      
      endgame_button = None
   
   while not mode_exit : 
      
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

      if normal_button.draw() : 
         from modes.normal_mode.normal_mode import normal_mode
         normal_mode()
      
      elif timebound_button.draw() : 
         from modes.timebound_mode.timebound_mode import timebound_mode
         timebound_mode()
      
      elif gaslight_button.draw() : 
         from modes.gaslight_mode.gaslight_mode import gaslight_mode
         gaslight_mode()
      
      elif endgame_condition == "unlock" : 
         if endgame_button.draw() : 
            from modes.endgame_mode.endgame_mode import endgame_mode 
            endgame_mode()

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
         quit_prompt = common_prompts.no_loop_roasts()
         
         pygame.mixer.music.stop()
         engine.say(quit_prompt)
         engine.runAndWait()
         
         pygame.quit()
         quit()

      for event in pygame.event.get() :

         if event.type == pygame.QUIT : 
            pygame.quit()
            quit()
      
      pygame.display.flip()
      clock.tick(fps)


menu()

