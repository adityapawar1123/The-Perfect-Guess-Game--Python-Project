def endgame_mode() : 
    import random 
    import threading
    import os 
    import time
    
    from modes.normal_mode.prompts import roasts, otherprompts
    from data.prompts import common_prompts

    # Set the environment variable BEFORE importing pygame
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
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

    file_path = os.path.abspath(__file__) #Gives absolute path of our current file
    dir_path = os.path.dirname(file_path) #Gives absolute path of the current folder in which this file is present
    endgame_unlock_path = os.path.join(dir_path, "data", "endgame_unlock.txt")

    with open(endgame_unlock_path, "w") as f : 
        f.write("lock")
    #As soon as endgame mode starts we lock it again as we want this to be a one time event

    endgame_unlocker_path = os.path.join(os.path.dirname(dir_path), "gaslight_mode", "data", "endgame_unlocker.txt")
    with open(endgame_unlocker_path, "w") as f : 
        f.write("lock")
    #So that gaslight mode doesn't keep unlocking it everytime cuz of the highscore --> One-time event

    from audio import audio 
    
    def music_thread(func, file, duration=-1) : #by default duration stays on -1 i.e. runs song on infinite loop
        thread = threading.Thread(target= func, args=(file, duration), daemon=True)
        thread.start()

    def sound_effect_thread(func, file) : #by default duration stays on -1 i.e. runs song on infinite loop
        thread = threading.Thread(target= func, args=(file,), daemon=True)
        thread.start()
    #Seperating these functn(s) to prevent audio overlapping

    music_thread(audio.normal_mode_music, "normal_mode.wav")
    
    from modes.endgame_mode.voicelines.kate import intro_speech
    intro_speech.testing()   #Starts the sad Kate intro
    
    print("\nGUESS A NUMBER BETWEEN 1 AND 500 UNDER 25 ATTEMPTS TO SAVE KATE\n")
    time.sleep(1.5)

    n = random.randint(1, 500)
    truth_serum = 4
    truth_serum_activate = False
    attempts_left = 25
    
    while True : 
        hints = random.choice(["\nGuess a higher number", "\nGuess a lower number"])
        print(f"number : {n}, attempts : {attempts_left}")
        
        if attempts_left == 22 : 
            pygame.mixer.music.pause()
            from modes.endgame_mode.voicelines.jokingo import jokingo_voicelines
            jokingo_voicelines.testing()
            pygame.mixer.music.unpause()
            sound_effect_thread(audio.sound_effects, "new_highscore_sound_effect.mp3")  
            print("💉 GAINED 4 TRUTH SERUMS 💉")
            truth_serum_activate = True 

        elif attempts_left < 22 :
            truth_serum_activate = True           

        if truth_serum_activate == True : 
            guessNo = input("\nGuess number (type 'truth serum' to use it) : ").lower().strip()
        else : 
            guessNo = input("\nGuess number : ").lower().strip()


        if attempts_left == 0 : 
            tts("Ohh no, ohh no no no")
            print("YOU LOST! KATE GLITCHED OFF INTO INSANITY")
            break

        
        elif truth_serum > 0 and truth_serum_activate == True and guessNo.lower().strip() in ["truth serum", "truth"] : 
                truth_serum -= 1
                try : 
                    guessNo = int(input("\nGuess number (Kate won't lie) : "))

                    if guessNo>n : 
                        attempts_left -= 1
                        tts("\nGuess a lower number")
                        print(f"\nAttempts left ⚠️ : {attempts_left}")
                        print(f"Truth serums left 💉 : {truth_serum}")
                        continue
                    
                    elif guessNo<n : 
                        attempts_left -= 1
                        tts("Guess a higher number")
                        print(f"\nAttempts left ⚠️ : {attempts_left}")
                        print(f"Truth serums left 💉 : {truth_serum}")
                        continue

                    else : 
                        tts("You saved me!")
                        print("YOU WON! YOU SAVED KATE")
                        break
                except ValueError :
                    tts("You had to enter a number! You just lost a truth serum hahaha")
                    continue
        
        elif truth_serum == 0 and truth_serum_activate == True and guessNo.lower().strip() in ["truth serum", "truth"] :

            tts("Hahaha....You are out of truth serums now....that's exactly what I wanted")
            print("You're out of truth serums!")
            continue
        

        else : 
            try : 
                if truth_serum_activate == True : 
                    guessNo = int(guessNo)
                    if guessNo>n or guessNo<n : 
                        attempts_left -= 1 
                        tts(hints)
                        print(f"\nAttempts left ⚠️: {attempts_left}\nTruth serums left 💉 : {truth_serum}")
                        continue

                    elif guessNo == n : 
                        tts("\nWhat? How did you guess the number even when I was lying to you?")
                        print("YOU WON! YOU SAVED KATE")
                        break
                
                else : 
                    guessNo = int(guessNo)
                    if guessNo>n or guessNo<n : 
                        attempts_left -= 1 
                        tts(hints)
                        print(f"\nAttempts left ⚠️: {attempts_left}")
                        continue

                    elif guessNo == n : 
                        tts("\nWhat? How did you guess the number even when I was lying to you?")
                        print("YOU WON! YOU SAVED KATE")
                        break

            except ValueError : 
                tts("\nYou're typing random numbers now? Hahaha that's what I want, looks like you're accepting your defeat.")
                print("\nC'mon this is not a joke, enter a number-- we need to save Kate")
                continue









