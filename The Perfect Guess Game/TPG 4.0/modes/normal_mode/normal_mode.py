def normal_mode() : 
    import random 
    
    from modes.normal_mode.prompts import roasts, otherprompts
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

    def tts(text) : 
        engine.say(text)
        print(text)
        engine.runAndWait()

    def only_tts(text) :
        engine.say(text)
        engine.runAndWait() 

    import os 
    path = os.path.dirname(os.path.abspath(__file__))


    tts(otherprompts.normal_mode_explain())
    
    while True : 
        tts("\nChoose the difficulty")

        print("Easy : Guess between 1 and 100\nMedium : Guess between 1 and 500\nHard : Guess between 1 and 1000")
        difficulty = input("Enter(e/m/h) : ")

        guessNo= 0

        def easy_highscore() : 
            easy_highscore_path = os.path.join(path, "highscores", "easy_highscore.txt")
            with open(easy_highscore_path) as f : 
                highscore = f.read().strip()

                if highscore!="" : 
                    highscore = int(highscore)
                else :
                    highscore = 100
                
                if guessNo>highscore : 
                    print(f"Highscore guess number : {highscore}")
                else : 
                    with open(easy_highscore_path, "w") as f1 : 
                        f1.write(str(guessNo))
                        tts("\nNew highscore unlocked!")
                        print(f"Highscore guess number : {guessNo}")

        def medium_highscore() :
            medium_highscore_path = os.path.join(path, "highscores", "medium_highscore.txt") 
            with open(medium_highscore_path) as f : 
                highscore = f.read().strip()

                if highscore!="" : 
                    highscore = int(highscore)
                else :
                    highscore = 100
                
                if guessNo>highscore : 
                    print(f"Highscore guess number : {highscore}")
                else : 
                    with open(medium_highscore_path, "w") as f1 : 
                        f1.write(str(guessNo))
                        tts("\nNew highscore unlocked!")
                        print(f"Highscore guess number : {guessNo}")

        def hard_highscore() : 
            hard_highscore_path = os.path.join(path, "highscores", "hard_highscore.txt")
            with open(hard_highscore_path) as f : 
                highscore = f.read().strip()

                if highscore!="" : 
                    highscore = int(highscore)
                else :
                    highscore = 100
                
                if guessNo>highscore : 
                    print(f"Highscore guess number : {highscore}")
                else : 
                    with open(hard_highscore_path, "w") as f1 :
                        f1.write(str(guessNo))
                        tts("\nNew highscore unlocked!")
                        print(f"Highscore guess number : {guessNo}")


        def game_win_prompts() :
            if guessNo==1 : 
                print(f"\nYou won! The answer is {n}\nNumber of guesses = {guessNo}")
                only_tts(otherprompts.first_guess_prompts())

            elif 2 <= guessNo < 4 :
                print(f"\nYou won! The answer is {n}\nNumber of guesses = {guessNo}")
                only_tts(otherprompts.under4_guess_prompts())  

            elif 4 <= guessNo <= 6 :
                print(f"\nYou won! The answer is {n}\nNumber of guesses = {guessNo}")
                only_tts(otherprompts.mid_guess_prompts())  

            else : 
                print(f"\nYou won! The answer is {n}\nNumber of guesses = {guessNo}")
                only_tts(roasts.slow_guess_roasts())  


        if difficulty.lower().strip() in ["e", "easy", "ez"] : 
                easyNo = random.randint(1, 100)
                
                tts("You have to guess a number between 1 and 100")
                while True : 
                    n1 = input("Guess the number : ")

                    if n1.isdigit() == True : 
                        n = int(n1)
                        if  easyNo==n : 
                            guessNo += 1
                            game_win_prompts()
                            easy_highscore()
                            break #breaks the inner loop 
                            
                        elif n<easyNo : 
                            only_tts("Guess a higher number")
                            print(f"\nWrong guess\nPick a higher number than {n}")
                            guessNo+=1

                        elif n>easyNo : 
                            only_tts("Guess a lower number")
                            print(f"\nWrong guess\nPick a lower number than {n}")
                            guessNo+=1

                    else : 
                        only_tts(roasts.invalid_input_roasts())
                        print("\nEnter an integer DUMBASS")
                break #Breaks the main loop
                    
            
            
        elif difficulty.lower().strip() in ["mid", "m", "medium", "normal"] :
                mediumNo = random.randint(1, 500)

                tts("You have to guess a number between 1 and 500")
                while True : 
                    n1 = input("Guess the number : ")

                    if n1.isdigit() == True : 
                        n = int(n1)
                        if  mediumNo==n : 
                            guessNo += 1
                            game_win_prompts()
                            medium_highscore()
                            break #breaks the inner loop
                            
                        elif n<mediumNo : 
                            only_tts("Guess a higher number")
                            print(f"\nWrong guess\nPick a higher number than {n}")
                            guessNo+=1

                        elif n>mediumNo : 
                            only_tts("Guess a lower number")
                            print(f"\nWrong guess\nPick a lower number than {n}")
                            guessNo+=1

                    else : 
                        only_tts(roasts.invalid_input_roasts())
                        print("\nEnter an integer DUMBASS")
                break #Breaks main loop
                    

        elif difficulty.lower().strip() in ["h", "hard", "difficult", "diff", "dif"] : 
                hardNo = random.randint(1, 1000)
                
                tts("You have to guess a number between 1 and 1000")
                while True : 
                    n1 = input("Guess the number : ")
                    
                    if n1.isdigit() == True : 
                        n = int(n1)
                        if  hardNo==n : 
                            guessNo += 1
                            game_win_prompts()
                            hard_highscore()
                            break #breaks inner loop
                            
                        elif n<hardNo : 
                            only_tts("Guess a higher number")
                            print(f"\nWrong guess\nPick a higher number than {n}")
                            guessNo+=1

                        elif n>hardNo : 
                            only_tts("Guess a lower number")
                            print(f"\nWrong guess\nPick a lower number than {n}")
                            guessNo+=1

                    else : 
                        only_tts(roasts.invalid_input_roasts())
                        print("\nEnter an integer DUMBASS")
                break #breaks main loop
                    
        else : 
            tts("\nInvalid difficulty level! Choose again")