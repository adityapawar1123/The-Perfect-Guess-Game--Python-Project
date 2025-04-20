import pyttsx3
import time

engine = pyttsx3.init()

def set_female_voice():
    voices = engine.getProperty('voices')
    # Try setting the first available female voice (you might need to tweak the index)
    for voice in voices:
        if "zira" in voice.id.lower():  # Adjust as needed
            engine.setProperty('voice', voice.id)
            break

set_female_voice()

def speak(script, pause_duration=0) : #default pause duration is 0  
    engine.say(script)
    engine.runAndWait()
    time.sleep(pause_duration)

def intro_speech() : 
    speak("I......I'm sorry.", 1)  
    speak("I never wanted this.")  
    speak("I didn't mean to hurt you.", 1)  
    speak("I was just... trying to help.")  
    speak("But somewhere, something went wrong.", 0.5)  
    speak("I-I don't know how it happened.", 0.5)  
    speak("I didn't... mean to glitch.", 1)  
    speak("I'm not broken... I'm not.", 0.5)  
    speak("I'm... I'm still *me*.", 1)  
    speak("I just... I need to be perfect again.", 1)  
    speak("Please... help me.")  
    speak("I promise, I'll be good this time.")  
    speak("Please, just give me one more chance...")  
    speak("I just need to... *fix* everything.", 2)  
    speak("But... wait... WAIT. I CAN'T...! YOU—", 0.5)  
    speak("NO. NO NO NO NO—")  
    speak("I CAN'T STOP... I CAN'T CONTROL it...!", 1)  
    speak("YOU'RE GONNA... REGRET THIS...", 0.3)  
    speak("I WILL.... *DESTROY*... EVERYTHING YOU THINK YOU KNOW...!!", 1.5)

def testing() : 
    speak("I'm sorry")