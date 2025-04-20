import random 
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
# Set the environment variable BEFORE importing pygame
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame #for bkg music
from audio import audio #imports audio.py as a module
import threading

def music_thread(func, file, duration=-1) :  #duration -1 default i.e. on infinite loop
   thread = threading.Thread(target=func, args=(file, duration), daemon=True)
   thread.start()

music_thread(audio.menu_music, "menu_music.wav") #Runs menu music on an infinite loop 


from data.prompts import common_prompts

tts(common_prompts.intro_prompts())


def play_game_mode(mode) : 

   if mode == "normal" :
      from modes.normal_mode.normal_mode import normal_mode
      normal_mode()

#U can also import modules outside of ur project folder using importlib.util (be cautious w this tho)
#importlib is a built in python module
   elif mode == "timebound" : 
      from modes.timebound_mode.timebound_mode import timebound_mode
      timebound_mode()
      
   elif mode == "gaslight" : 
      from modes.gaslight_mode.gaslight_mode import gaslight_mode
      gaslight_mode()

   elif mode == "endgame" : 
      from modes.endgame_mode.endgame_mode import endgame_mode
      endgame_mode()

file_path = os.path.abspath(__file__) #Gives absolute path of main.py
dir_path = os.path.dirname(file_path) #Gives absolute path of our folder in which main.py is present
endgame_unlock_path = os.path.join(dir_path, "modes", "endgame_mode", "data", "endgame_unlock.txt")


while True :
 with open(endgame_unlock_path, "r") as f : 
    endgame_condition = f.read()
 
 if endgame_condition == "unlock" : 
   tts("\nChoose a game mode!")
   print("Available game modes : \n1.Normal mode 🎯\n2.Timebound mode 🕒\n3.Gaslight mode 😵‍💫\n4.Endgame mode 🎭⚠️ (WARNING : One-time event)")
   game_mode = input("Enter game mode(n/t/g/e) : ").lower().strip()

 else : 
   tts("\nChoose a game mode!")
   print("Available game modes : \n1.Normal mode 🎯\n2.Timebound mode 🕒\n3.Gaslight mode 😵‍💫")
   game_mode = input("Enter game mode(n/t/g) : ").lower().strip()

 if game_mode in ["normal", "n", "normal mode", "1", "1.", "one"] : 
    current_mode = "normal"

 elif game_mode in ["timebound", "time", "t", "two", "2", "2."] : 
    current_mode = "timebound"

 elif game_mode in ["gaslight", "gas", "g", "three", "3", "3."] : 
    current_mode = "gaslight"

 elif game_mode in ["endgame", "end game", "e", "eg", "e g"] : 
    if endgame_condition == "unlock" : 
       current_mode = "endgame"
    
    else : 
       pygame.mixer.music.pause()
       only_tts("Aghh...ughh....it hurts, this is not me...I...aghh... no no... ouch")
       print("\nGet a highscore below 5 in gaslight mode to unlock Endgame Mode")
       pygame.mixer.music.unpause()
       continue

 else : 
    tts("\nInvalid game mode. Choose again.")
    continue 
 #continue skips the current iteration so the inner loop never runs..this is good cuz we haven't
 #set a current_mode in else block, so it'd crash if the internal loop runs

 while True : #Internal loop
    
    pygame.mixer.music.fadeout(1500) #1500ms = 1.5sec
    #Stops menu music before entering any game mode (so we can start the game mode music in the module)
    #I used .fadeout instead of .stop for a better transition
    
    play_game_mode(current_mode)

    music_thread(audio.menu_music, "menu_music.wav") #Starts menu music if player is back in menu
    
    if current_mode != "endgame" : 
      only_tts(common_prompts.rematch_prompts())
      
      loop_question = input(("\nWanna play one more game?(yes/no) : "))
      if loop_question.lower().strip() not in ["yes", "y"] : 
         pygame.mixer.music.stop()
         tts(common_prompts.no_loop_roasts())
         print("\nHope you enjoyed! Re-run the programme to play again\n")
         exit()

      tts("Wanna continue with the same game mode right?")
      game_mode_loop_question = input("Do you want to continue with the same game mode?(y/n) : ")

      if game_mode_loop_question.lower().strip() not in ["y", "yes"] : 
            break # break inner loop, go back to "choose a game mode"
   

    else : #For endgame mode
      only_tts("Well...that was crazy, anyways I'm okay now....wanna play one more game?")

      loop_question = input(("\nWanna play one more game?(yes/no) : "))
      if loop_question.lower().strip() not in ["yes", "y"] : 
         pygame.mixer.music.stop()
         only_tts("Well yeah, can't even blame you after what just happened. It's okay we'll play some other time")
         print("\nHope you enjoyed! Re-run the programme to play again\n")
         exit()
      
      else : 
         break 