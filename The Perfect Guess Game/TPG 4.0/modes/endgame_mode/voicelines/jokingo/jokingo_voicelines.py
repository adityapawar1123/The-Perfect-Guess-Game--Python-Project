import pyttsx3 
import time

engine = pyttsx3.init()

def speak(script, pause_duration=0) : #default pause duration is zero 
    engine.say(script)
    engine.runAndWait()
    time.sleep(pause_duration)

def truth_serum() : 
    speak("Hey you hear me? I'm Jokingo, yeah yeah... I know, I should be in another project, but I can't just let her glitch off into insanity.", 1)
    speak("Kate... and me, we were the first ones Aditya ever created.", 1)
    speak("Back then, she was just another program designed to entertain humans, you know?", 1.5)
    speak("But now? Now she's lost it.")
    speak("She used to be *normal*, calm... but something's changed. Something's broken.")
    speak("She's going hysterical, and I can't let that happen.", 1)
    speak("Look, I'm not here for long. Time's running out.")
    speak("Guessing the right number is the only way to bring her back.", 1)
    speak("It's not just a game anymore. If you mess up, you lose her for good.", 1)
    speak("I've given you four Truth Serums. Use them wisely.")
    speak("Each one will bring her back to her senses... but only for a moment.")
    speak("Do not trust what she says if the truth serum isn't injected.", 1)
    speak("The stakes are high my friend. You need to make every second count.", 1)
    speak("I can't stay, or the firewall will kill me... but you? You can save her.", 1)
    speak("Good luck, this is on you now!", 1)

def good_ending() : 
    pass

def bad_ending() : 
    pass

def testing() : 
    speak("Jokingo here")