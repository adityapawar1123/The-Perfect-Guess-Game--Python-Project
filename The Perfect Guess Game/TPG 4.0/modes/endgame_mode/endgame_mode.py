def endgame_mode() : 
    import random 
    import threading
    import os 
    import time
    
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
    endgame_unlock_path = os.path.join(dir_path, "endgame_unlock.txt")

    with open(endgame_unlock_path, "w") as f : 
        f.write("lock")
    #As soon as endgame mode starts we lock it again as we want this to be a one time event

    endgame_unlocker_path = os.path.join(os.path.dirname(dir_path), "gaslight_mode", "data", "endgame_unlocker.txt")
    with open(endgame_unlocker_path, "w") as f : 
        f.write("lock")
    #So that gaslight mode doesn't keep unlocking it everytime cuz of the highscore --> One-time event


    endgame_hinter_unlocker_path = os.path.join("data", "endgame_hinter_unlocker.txt")
    with open(endgame_hinter_unlocker_path, "w") as f : 
        f.write("lock")
    #So that Jokingo's creepy lines after every 4 games will stop

    
    def music_thread(func, file, duration=-1) : #by default duration stays on -1 i.e. runs song on infinite loop
        thread = threading.Thread(target= func, args=(file, duration), daemon=True)
        thread.start()

    def sound_effect_thread(func, file) : #by default duration stays on -1 i.e. runs song on infinite loop
        thread = threading.Thread(target= func, args=(file,), daemon=True)
        thread.start()
    #Seperating these functn(s) to prevent audio overlapping

    
    from audio import voicelines
    voicelines.endgame_kate_intro()   #Starts the sad/psycho Kate intro
    
    from audio import audio 
    music_thread(audio.normal_mode_music, "normal_mode.wav")
    
    print("\nGUESS A NUMBER BETWEEN 1 AND 500 UNDER 25 ATTEMPTS TO SAVE KATE\n")
    time.sleep(1.5)

    n = random.randint(1, 500)
    truth_serum = 7
    truth_serum_activate = False
    attempts_left = 25
    
    while True : 
        hints = random.choice(["\nGuess a higher number", "\nGuess a lower number"])
        print(f"The number is : {n}")
        
        if attempts_left == 22 : 
            pygame.mixer.music.pause()
            
            voicelines.endgame_jokingo_reveal()

            pygame.mixer.music.unpause()
            sound_effect_thread(audio.sound_effects, "new_highscore_sound_effect.mp3")  
            print("💉 GAINED 7 TRUTH SERUMS 💉")
            truth_serum_activate = True 

        elif attempts_left < 22 :
            truth_serum_activate = True           

        if truth_serum_activate == True : 
            guessNo = input("\nGuess number (type 'truth serum' to use it) : ").lower().strip()
        else : 
            guessNo = input("\nGuess number : ").lower().strip()

        endgame_result_path = os.path.join("modes", "endgame_mode", "endgame_result.txt")
        if attempts_left == 0 : 
            print("YOU LOST! KATE GLITCHED OFF INTO INSANITY")
            sound_effect_thread(audio.sound_effects, "loss_sound_effect.mp3")

            voicelines.endgame_lose()
            with open(endgame_result_path, "w") as f : 
                f.write("lost")
            break

        
        elif truth_serum > 0 and truth_serum_activate == True and guessNo.lower().strip() in ["truth serum", "truth"] : 
                truth_serum -= 1
                try : 
                    guessNo = int(input("\nGuess number (Kate won't lie) : "))

                    if guessNo>n : 
                        attempts_left -= 1
                        only_tts("Guess a lower number")
                        print(f"\nPick a lower number than {guessNo}")
                        print(f"\nAttempts left ⚠️ : {attempts_left}")
                        print(f"Truth serums left 💉 : {truth_serum}")
                        continue
                    
                    elif guessNo<n : 
                        attempts_left -= 1
                        only_tts("Guess a higher number")
                        print(f"\nPick a higher number than {guessNo}")
                        print(f"\nAttempts left ⚠️ : {attempts_left}")
                        print(f"Truth serums left 💉 : {truth_serum}")
                        continue

                    elif guessNo == n : 
                        sound_effect_thread(audio.sound_effects, "win_sound_effect.mp3")
                        print("YOU WON! YOU SAVED KATE")
                        with open(endgame_result_path, "w") as f : 
                            f.write("won")
                        
                        voicelines.endgame_win()
                        return #better than breaking loop, js exit the endgame mode
                
                except ValueError :
                    tts("You had to enter a number! You just lost a truth serum!")
                    continue
        
        elif truth_serum == 0 and truth_serum_activate == True and guessNo.lower().strip() in ["truth serum", "truth"] :

            only_tts("Hahaha....You are out of truth serums now....that's exactly what I wanted")
            print("\nYou're out of truth serums! 💉🚫")
            continue
        

        else : 
            try : 
                if truth_serum_activate == True : 
                    guessNo = int(guessNo)
                    
                    if guessNo>n or guessNo<n : 
                        attempts_left -= 1 
                        
                        only_tts(hints)
                        if hints == "\nGuess a higher number" : 
                            print(f"Pick a higher number than {guessNo}")
                        else : 
                            print(f"Pick a lower number than {guessNo}")

                        print(f"\nAttempts left ⚠️: {attempts_left}\nTruth serums left 💉 : {truth_serum}")
                        if attempts_left != 0 : 
                            voicelines.endgame_kate_attempts(attempts_left)
                            continue

                    elif guessNo == n : 
                        print("YOU WON! YOU SAVED KATE")
                        sound_effect_thread(audio.sound_effects, "win_sound_effect.mp3")
                        with open(endgame_result_path, "w") as f : 
                            f.write("won")
                        
                        voicelines.endgame_win()
                        return
                
                else : 
                    guessNo = int(guessNo)
                    if guessNo>n or guessNo<n : 
                        attempts_left -= 1 
                        
                        only_tts(hints)
                        if hints == "\nGuess a higher number" : 
                            print(f"Pick a higher number than {guessNo}")
                        else : 
                            print(f"Pick a lower number than {guessNo}")
                        
                        print(f"Attempts left ⚠️: {attempts_left}")

                        if attempts_left != 0 : 
                            voicelines.endgame_kate_attempts(attempts_left)
                            continue

                    elif guessNo == n : 
                        sound_effect_thread(audio.sound_effects, "win_sound_effect.mp3")
                        print("YOU WON! YOU SAVED KATE")
                        
                        with open(endgame_result_path, "w") as f : 
                            f.write("won")
                        
                        voicelines.endgame_win()
                        return

            except ValueError : 
                tts("\nYou're typing random numbers now? Hahaha that's what I want, looks like you're accepting your defeat.")
                print("\nC'mon this is not a joke, enter a number-- we need to save Kate")
                continue









