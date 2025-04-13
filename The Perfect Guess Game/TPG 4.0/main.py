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


from data.prompts import common_prompts

tts(common_prompts.intro_prompts())


def play_game_mode(mode) : 

   if mode == "normal" :
      from modes.normal_mode.normal_mode import normal_mode
      normal_mode()

#U can also import modules outside of ur project folder using importlib.util (be cautious w this tho)
#importlib is a built in python module
   elif mode == "timebound" : 
      pass
      


while True :
 
 tts("\nChoose a game mode!")
 print("Available game modes : \n1.Normal mode\n2.Timebound mode")

 game_mode = input("Enter game mode(n/t) : ").lower().strip()

 if game_mode in ["normal", "n", "normal mode", "1", "1.", "one"] : 
    current_mode = "normal"

 elif game_mode in ["timebound", "time", "t", "two", "2", "2."] : 
    current_mode = "timebound"
    tts("We are currently working on that game mode, come again soon to check it out!")
    continue


 else : 
    tts("\nInvalid game mode. Choose again.")
    continue 
 #continue skips the current iteration so the inner loop never runs..this is good cuz we haven't
 #set a current_mode in else block, so it'd crash if the internal loop runs

 while True : #Internal loop

    play_game_mode(current_mode)
    only_tts(common_prompts.rematch_prompts())
    
    loop_question = input(("\nWanna play one more game?(yes/no) : "))
    if loop_question.lower().strip() not in ["yes", "y"] : 
        tts(common_prompts.no_loop_roasts())
        print("\nHope you enjoyed! Re-run the programme to play again")
        exit()

    tts("Wanna continue with the same game mode right?")
    game_mode_loop_question = input("Do you want to continue with the same game mode?(y/n) : ")

    if game_mode_loop_question.lower().strip() not in ["y", "yes"] : 
         break # break inner loop, go back to "choose a game mode"
    

     


   
       
    



