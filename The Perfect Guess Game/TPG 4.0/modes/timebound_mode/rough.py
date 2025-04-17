import time
import threading
import pyttsx3

engine = pyttsx3.init()


def countdown(seconds) :
    for i in range(seconds, 0, -1):
        #The :2 means “make sure it’s at least 2 characters wide,” so 9 becomes ' 9'.
        time.sleep(1)
        return i
    else : 
        print("\nTime's up!")
        exit()

def tts(text) : 
    engine.say(text)
    engine.runAndWait()


timer = threading.Thread(target=countdown, args=(10,))
timer.start()

tts_thread = threading.Thread(target=tts, args=("Hey how are you", ))
tts_thread.start()




