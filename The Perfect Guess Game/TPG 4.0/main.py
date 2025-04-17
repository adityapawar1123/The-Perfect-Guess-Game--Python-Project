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
      


while True :
 
 tts("\nChoose a game mode!")
 print("Available game modes : \n1.Normal mode 🎯\n2.Timebound mode 🕒")

 game_mode = input("Enter game mode(n/t) : ").lower().strip()

 if game_mode in ["normal", "n", "normal mode", "1", "1.", "one"] : 
    current_mode = "normal"

 elif game_mode in ["timebound", "time", "t", "two", "2", "2."] : 
    current_mode = "timebound"


 else : 
    tts("\nInvalid game mode. Choose again.")
    continue 
 #continue skips the current iteration so the inner loop never runs..this is good cuz we haven't
 #set a current_mode in else block, so it'd crash if the internal loop runs

 while True : #Internal loop
    
    pygame.mixer.music.stop() #Stops menu music before entering any game mode (so we can start the game mode music in the module)
    play_game_mode(current_mode)
    only_tts(common_prompts.rematch_prompts())


    music_thread(audio.menu_music, "menu_music.wav") #Starts menu music if player is back in menu
    
    loop_question = input(("\nWanna play one more game?(yes/no) : "))
    if loop_question.lower().strip() not in ["yes", "y"] : 
        pygame.mixer.music.stop()
        tts(common_prompts.no_loop_roasts())
        print("\nHope you enjoyed! Re-run the programme to play again")
        exit()

    tts("Wanna continue with the same game mode right?")
    game_mode_loop_question = input("Do you want to continue with the same game mode?(y/n) : ")

    if game_mode_loop_question.lower().strip() not in ["y", "yes"] : 
         break # break inner loop, go back to "choose a game mode"
    