def normal_mode(screen, screen_width, screen_height) : 
    import random 
    import threading
    import os 
    import time
    
    from modes.normal_mode.prompts import roasts, otherprompts
    from data.prompts import common_prompts
    from UI.utils import Button

    # Set the environment variable BEFORE importing pygame
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame
    pygame.init()
    
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

    
    from audio import audio 
    def music_thread(func, file, duration=-1) : #by default duration stays on -1 i.e. runs song on infinite loop
        thread = threading.Thread(target= func, args=(file, duration), daemon=True)
        thread.start()

    def sound_effect_thread(func, file) : #by default duration stays on -1 i.e. runs song on infinite loop
        thread = threading.Thread(target= func, args=(file,), daemon=True)
        thread.start()
    #Seperating these functn(s) to prevent audio overlapping

    def voiceline_thread(func) : 
        thread = threading.Thread(target=func, daemon=False)
        thread.start()

    
    path = os.path.dirname(os.path.abspath(__file__))
    mode_path = os.path.dirname(path)
    tpg_5 = os.path.dirname(mode_path)
    
    db_font_path = os.path.join(tpg_5, "UI", "pixellari.ttf")
    input_font_path = os.path.join(tpg_5, "UI", "vcr.ttf") 
    
    raw_kate = [
    pygame.image.load(os.path.join(tpg_5, "UI", "ui", "kate", "01_kate.png")).convert_alpha(),
    pygame.image.load(os.path.join(tpg_5, "UI", "ui", "kate", "02_kate.png")).convert_alpha(),
    ]
    kate_w = int(screen_width*0.2)
    kate_h = int(screen_height*0.4)
    kate_img = [
    pygame.transform.scale(img, (kate_w, kate_h))
    for img in raw_kate
    ]  
    kate_x = int(screen_width*0.03) 
    kate_y = int(screen_height*0.7)  
    
    raw_bg = pygame.image.load(os.path.join(tpg_5, "UI", "ui", "game_bkg.png")).convert_alpha()
    bkg = pygame.transform.scale(raw_bg, (screen_width, screen_height))
    input_box_raw = pygame.image.load(os.path.join(tpg_5, "UI", "ui", "input_box.png")).convert_alpha()
    box_w = int(screen_width*0.4)
    box_h = int(screen_height*0.3)
    input_box = pygame.transform.scale(input_box_raw, (box_w, box_h))

    kate_db_path = os.path.join(tpg_5, "UI", "ui", "kate_db.png")
    voice_db_path = os.path.join(tpg_5, "UI", "ui", "voice_db.png")

    
    kate_db_raw = pygame.image.load(kate_db_path).convert_alpha()
    db_width  = int(screen_width * 0.4)   # like 1000/1280
    db_height = int(screen_height * 0.15)  # like 180/720
    kate_db = pygame.transform.scale(kate_db_raw, (db_width, db_height))
    db_x = int((kate_x + kate_w) - kate_w*0.15) 
    db_y = (kate_y - (kate_y*0.05))  # push db toward bottom
    

    def tts(screen, text, font_size, color, pos, max_width=None) : 
        font = pygame.font.Font(db_font_path, font_size)

        if max_width is None : 
            max_width = int(db_width*0.9) # 90% of db width
        
        words = text.split(' ') # splits whole text into words
        lines = []              # stores each final line that will be rendered
        current_line = ''       # current line being built

        for word in words : 
            test_line = current_line + word + ' '

            if font.size(test_line)[0] <= max_width : # [0] is for width cuz font.size func of python gives a tuple (width, height)
                current_line = test_line #it fits, add it
            
            else : 
                lines.append(current_line.strip())  # doesn't fit, push current line to final lines
                current_line = word + ' '           # start a new line with the current word
            
        lines.append(current_line.strip())

        x,y = pos # So that we can later edit y for each new line
        line_spacing = font_size + 5

        #Render each line
        for line in lines : 
            rendered = font.render(line, True, color)
            screen.blit(rendered, (x,y))

            y += line_spacing # After drawing one line, you move down by the amount defined in line_spacing so the next line appears underneath it.
            
        pygame.display.flip()
        
        engine.say(text)
        engine.runAndWait()

    def only_tts(text) :
        engine.say(text)
        engine.runAndWait() 
    

    def jokingo_hints() : 
        endgame_hinter_unlocker_path = os.path.join(tpg_5, "data", "endgame_hinter_unlocker.txt")
        with open(endgame_hinter_unlocker_path) as f : 
            unlocker = f.read()
        
        endgame_hinter = os.path.join(tpg_5, "data", "endgame_hinter.txt")
        
        if unlocker != "lock" : 
            with open(endgame_hinter) as f :
                data1 = f.read()

            if int(data1)%4 == 0 and int(data1) != 0 : 
                from audio.voicelines import endgame_hint
                voiceline_thread(endgame_hint())
            
            data_update = int(data1) + 1
            with open(endgame_hinter, "w") as f : 
                f.write(str(data_update))
    
    def easy_highscore(guessNo) : 
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
                    sound_effect_thread(audio.sound_effects, "new_highscore_sound_effect.mp3") #plays new highscore music
                    with open(easy_highscore_path, "w") as f1 : 
                        f1.write(str(guessNo))
                        tts("\nNew highscore unlocked!")
                        print(f"Highscore guess number : {guessNo}")

    def medium_highscore(guessNo) :
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
                sound_effect_thread(audio.sound_effects, "new_highscore_sound_effect.mp3")
                with open(medium_highscore_path, "w") as f1 : 
                    f1.write(str(guessNo))
                    tts("\nNew highscore unlocked!")
                    print(f"Highscore guess number : {guessNo}")

    def hard_highscore(guessNo) : 
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
                sound_effect_thread(audio.sound_effects, "new_highscore_sound_effect.mp3")
                with open(hard_highscore_path, "w") as f1 :
                    f1.write(str(guessNo))
                    tts("\nNew highscore unlocked!")
                    print(f"Highscore guess number : {guessNo}")


    def game_win_prompts(guessNo, n) :
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

    

    easy_button = Button("01_easy.png", "02_easy.png", "03_easy.png", (0.50, 0.40), screen, screen_width, screen_height)    
    medium_button = Button("01_medium.png", "02_medium.png", "03_medium.png", (0.50, 0.50), screen, screen_width, screen_height)    
    hard_button = Button("01_hard.png", "02_hard.png", "03_hard.png", (0.50, 0.60), screen, screen_width, screen_height)    


    music_thread(audio.normal_mode_music, "normal_mode.wav")

    from modes.normal_mode.prompts.otherprompts import normal_mode_explain, first_guess_prompts, under4_guess_prompts, mid_guess_prompts
    from modes.normal_mode.prompts.roasts import invalid_input_roasts, slow_guess_roasts
    
    #Game vars
    difficulty_selected = False 
    kate = kate_img[0]
    kate_talking = True
    intro = True 
    clock = pygame.time.Clock()
    fps = 60
    
    while not difficulty_selected : 

        screen.blit(bkg, (0,0))

        if (kate_talking == True) and (intro == True) : 
            kate = kate_img[1]
            screen.blit(kate, (kate_x, kate_y))
            screen.blit(kate_db, (db_x, db_y))
            pygame.display.flip()

            tts(screen, normal_mode_explain(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
            
            screen.blit(kate_db, (db_x, db_y))
            pygame.display.flip()
            tts(screen, "Choose the difficulty!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))

            kate_talking = False
            intro = False  
        
        if easy_button.draw() : 
            difficulty = "easy"

            kate = kate_img[1]
            screen.blit(kate, (kate_x, kate_y))
            screen.blit(kate_db, (db_x, db_y))
            pygame.display.flip()

            tts(screen, "You have to guess a number between 1 and 100", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))

            difficulty_selected = True

        elif medium_button.draw() : 
            difficulty = "medium"

            kate = kate_img[1]
            screen.blit(kate, (kate_x, kate_y))
            screen.blit(kate_db, (db_x, db_y))
            pygame.display.flip()

            tts(screen, "You have to guess a number between 1 and 500", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))

            difficulty_selected = True
        
        elif hard_button.draw() : 
            difficulty = "hard"

            kate = kate_img[1]
            screen.blit(kate, (kate_x, kate_y))
            screen.blit(kate_db, (db_x, db_y))
            pygame.display.flip()

            tts(screen, "You have to guess a number between 1 and 1000", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))

            difficulty_selected = True
        
        else : 
            kate = kate_img[0]
            screen.blit(kate, (kate_x, kate_y))
            pygame.display.flip()

        for event in pygame.event.get() : 

            if event.type == pygame.QUIT : 
                pygame.quit()
                quit()
        
        clock.tick(fps)

    