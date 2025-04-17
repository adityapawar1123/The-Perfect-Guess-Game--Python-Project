def timebound_mode() : 

    import random 
    import threading
    import time

    from modes.timebound_mode.prompts import roasts, otherprompts
    from data.prompts import common_prompts
    
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

    tts_lock = threading.Lock()
    #very imp as pyttsx3 gets cranky w engine.runAndWait() when mutliple threads are trynna access it

# pyttsx3 is pretty temperamental when you call it from multiple threads, 
# and your current approach of firing off a new thread every time you want to speak can cause the 
# engine to get “stuck” or simply go mute after the first successful call. 
# This is a known pain point with pyttsx3—once it gets into an unexpected state from overlapping runAndWait calls, it stops talking.
    
    def tts(text) : 
        with tts_lock : 
            engine.say(text)
            print(text)
            engine.runAndWait()
    
    def only_tts(text) : 
        with tts_lock : 
            engine.say(text)
            engine.runAndWait()
#If you ever get weird behavior like "works once but never again", look for variable/function 
#name collisions. Python won’t throw an error, but the results get janky real fast.

    import os
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide" #prevents pygame from printing that intro msg
    import pygame
    pygame.mixer.init()

    from audio import audio 
    def music_thread(func, file, duration=-1) : #by default duration stays on -1 i.e. runs song on infinite loop
        thread = threading.Thread(target= func, args=(file, duration), daemon=True)
        thread.start()

    def sound_effect_thread(func, file) : #by default duration stays on -1 i.e. runs song on infinite loop
        thread = threading.Thread(target= func, args=(file,), daemon=True)
        thread.start()
    #Seperating these functn(s) to prevent audio overlapping

    music_thread(audio.timebound_mode_music, "timebound_mode.wav") #Starts music

    tts(otherprompts.timebound_mode_explain())
    
    def game() : 
        lock = threading.Lock()

        while True : 

            tts("\nChoose the difficulty")

            print("Easy : Guess between 1 and 100\nMedium : Guess between 1 and 500\nHard : Guess between 1 and 1000")
            difficulty = input("Enter(e/m/h) : ")

            if difficulty not in ["e", "ez", "easy", "m", "mid", "medium", "normal", "diff", "dif", "h", "hard", "tough"] : 
                pygame.mixer.music.pause()
                tts("\nInvalid difficulty level! Please try again.")
                pygame.mixer.music.unpause()
                continue

            try : 
                tts("\nChoose timer")
                print("1. 20secs timer\n2. 30secs timer\n3. 40secs timer")
                timer = int(input("Enter timer(20/30/40) : "))

                if timer not in [20, 30, 40] : 
                    pygame.mixer.music.pause()
                    tts("\nPlease select the timer only between given options. Try again!")
                    pygame.mixer.music.unpause()
                    continue #loops back to choose difficulty

            except ValueError : #loops back if user doesn't enter an int
                pygame.mixer.music.pause()
                tts("\nInvalid input! Please enter a number only, try again")
                pygame.mixer.music.unpause()
                continue


            def countdown(shared_state) :
                while shared_state['remaining_time'] > 0 : 
                    time.sleep(1)
                    with lock : 
                        shared_state['remaining_time'] -= 1
                    
                    if shared_state['remaining_time'] == 10 : 
                        pygame.mixer.music.stop()
                        print("\n🕒 10 seconds remaining!!")
                        music_thread(audio.timebound_mode_music, "timebound_10_sec_left.wav")
                        continue
            
            def number_guesser():
                if difficulty.lower().strip() in ["e", "ez", "easy"] : 
                    guessNo = random.randint(1, 100)
                    difficulty_explain = "\nYou have to guess a number between 1 and 100."

                elif difficulty.lower().strip() in ["m", "mid", "medium", "normal"] : 
                    guessNo = random.randint(1, 500)
                    difficulty_explain = "\nYou have to guess a number between 1 and 500."


                elif difficulty.lower().strip() in ["diff", "dif", "h", "hard", "tough"] : 
                    guessNo = random.randint(1, 1000)
                    difficulty_explain = "\nYou have to guess a number between 1 and 1000."


                tts(difficulty_explain)

                shared_state = {'remaining_time' : timer}
                timer_thread = threading.Thread(target=countdown, args=(shared_state, ), daemon=True)
                timer_thread.start() #can't put this in loop as threads can only be started once
                while True : 
                    try : 
                        
                     try : 
                        print(f"\n 🕒 Time left : {shared_state['remaining_time']}")
                        n = int(input("\nGuess the number : "))

                        if shared_state['remaining_time'] == 0 : 
                            raise TimeoutError
                    #Now if the timer has ended, and even if player inputs the correct number after that
                    #they still lose, as after input we check if shared_state == 0, if it is then BYE BYE

                        else : 
            
                            if  guessNo==n : 
                                    pygame.mixer.music.stop() #Stops the bkg music
                                    sound_effect_thread(audio.sound_effects, "win_sound_effect.mp3")
                                    print("\n✨YOU WON!✨")
                                    only_tts("You won!")
                                    only_tts(otherprompts.win_prompts())
                                    return "won"
                                
                                    
                            elif n<guessNo : 
                                    tts("Guess a higher number")
                                    print(f"\nWrong guess\nPick a higher number than {n}")
                                    continue #continues inner loop
                                    

                            elif n>guessNo : 
                                    tts("Guess a lower number")
                                    print(f"\nWrong guess\nPick a lower number than {n}")
                                    continue #continues inner loop
                                    
                     except ValueError :  
                            pygame.mixer.music.pause()
                            tts(roasts.invalid_input_roasts())
                            print("\nEnter an integer DUMBASS")
                            pygame.mixer.music.unpause()
                            continue #loops back if user doesn't enter an int
                    
                    
                    except TimeoutError : 
                        pygame.mixer.music.stop()
                        sound_effect_thread(audio.sound_effects, "loss_sound_effect.mp3")
                        print("\n💥 Countdown finished! YOU LOST 💥")
                        only_tts(otherprompts.lose_prompts())
                        return "time over"

            result = number_guesser()

            if result == "won" or result == "time over" : 
                break #Breaks the outer loop, hence ending timebound mode and going back to main.py
    game()