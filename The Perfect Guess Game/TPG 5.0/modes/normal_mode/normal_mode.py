def normal_mode(screen, screen_width, screen_height) : 
    import random 
    import threading
    import os 
    import time
    
    from modes.normal_mode.prompts import roasts, otherprompts
    from data.prompts.common_prompts import rematch_prompts
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
        
        words = text.split(' ') # splits whole text into words, words is a list now with each words as an item of the list
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
    from modes.normal_mode.prompts.roasts import invalid_input_roasts, slow_guess_roasts, game_quit
    
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
            n = random.randint(1,100)
            

            difficulty_selected = True

        elif medium_button.draw() : 
            difficulty = "medium"

            kate = kate_img[1]
            screen.blit(kate, (kate_x, kate_y))
            screen.blit(kate_db, (db_x, db_y))
            pygame.display.flip()

            tts(screen, "You have to guess a number between 1 and 500", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
            n = random.randint(1,500)
            
            difficulty_selected = True
        
        elif hard_button.draw() : 
            difficulty = "hard"

            kate = kate_img[1]
            screen.blit(kate, (kate_x, kate_y))
            screen.blit(kate_db, (db_x, db_y))
            pygame.display.flip()

            tts(screen, "You have to guess a number between 1 and 1000", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
            n = random.randint(1,1000)

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

    


    game_over = False 
    scoreboard_active = False 
    kate = kate_img[0]
    guessNo = 0 
    
    input_box_raw = pygame.image.load(os.path.join(tpg_5, "UI", "ui", "input_box.png")).convert_alpha()
    box_w = int(screen_width*0.4)
    box_h = int(screen_height*0.3)
    input_box = pygame.transform.scale(input_box_raw, (box_w, box_h))
    box_x  = int(screen_width * 0.5 - box_w * 0.5) # centered
    box_y  = int(screen_height * 0.5 - box_h*0.5)

    font_size = int(screen_height*0.05)
    input_font = pygame.font.Font(input_font_path, font_size)
    padding_x = int(box_w*0.23) # 23% of box width
    text_x = box_x + padding_x
    text_y = box_y + ((box_h - font_size) // 4) + box_y*0.06
    user_text = ""    # This will hold what the player types

    last_cusor_toggle = pygame.time.get_ticks()
    CURSOR_DURATION = 500 # in ms
    cursor_visible = True 

    quit_button = Button("01_quit.png", "02_quit.png", "03_quit.png", (0.88, 0.865), screen, screen_width, screen_height)
    #replace this w a BACK button later

    while not game_over : 
        current = pygame.time.get_ticks()

        screen.blit(bkg, (0,0))
        screen.blit(input_box, (box_x, box_y))

        if quit_button.draw() : 
            
            pygame.mixer.music.fadeout(2000)
            
            screen.blit(kate_img[1], (kate_x, kate_y))
            screen.blit(kate_db, (db_x, db_y))
            pygame.display.flip()

            tts(screen, game_quit(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
            music_thread(audio.menu_music, "menu_music.wav")
            game_over = True

        
        if current - last_cusor_toggle >= CURSOR_DURATION : 
            last_cusor_toggle = current 
            cursor_visible = not cursor_visible

        for event in pygame.event.get() :

            if event.type == pygame.QUIT : 
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN : 

                if event.key == pygame.K_RETURN:

                    if user_text != '' : 
                        try : 
                            user_text = int(user_text)
                            
                            if user_text > n : 
                                
                                screen.blit(kate_img[1], (kate_x, kate_y))
                                screen.blit(kate_db, (db_x, db_y))
                                pygame.display.flip()
                                
                                tts(screen, "Guess a lower number!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                guessNo += 1

                            elif user_text < n : 
                                
                                screen.blit(kate_img[1], (kate_x, kate_y))
                                screen.blit(kate_db, (db_x, db_y))
                                pygame.display.flip()
                                
                                tts(screen, "Guess a higher number!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                guessNo += 1

                            elif user_text == n : 
                                
                                if difficulty == "easy" : 
                                    if guessNo == 1 : 
                                        win_prompt = first_guess_prompts()
                                    elif 2 <= guessNo < 4 : 
                                        win_prompt = under4_guess_prompts(guessNo)
                                    elif 4 <= guessNo <= 6 : 
                                        win_prompt = mid_guess_prompts()
                                    else : 
                                        win_prompt = slow_guess_roasts()
                                
                                elif difficulty == "medium" : 
                                    if guessNo == 1 : 
                                        win_prompt = first_guess_prompts()
                                    elif 2 <= guessNo < 6 : 
                                        win_prompt = under4_guess_prompts(guessNo)
                                    elif 6 <= guessNo <= 8 : 
                                        win_prompt = mid_guess_prompts()
                                    else : 
                                        win_prompt = slow_guess_roasts()
                                
                                elif difficulty == "hard" : 
                                    if guessNo == 1 : 
                                        win_prompt = first_guess_prompts()
                                    elif 2 <= guessNo < 8 : 
                                        win_prompt = under4_guess_prompts(guessNo)
                                    elif 8 <= guessNo <= 9 : 
                                        win_prompt = mid_guess_prompts()
                                    else : 
                                        win_prompt = slow_guess_roasts()
                                
                                screen.blit(kate_img[1], (kate_x, kate_y))
                                screen.blit(kate_db, (db_x, db_y))
                                pygame.display.flip()

                                tts(screen, win_prompt, int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                guessNo += 1
                                print(guessNo) #FOR DEBUGGING
                                
                                pygame.mixer.music.fadeout(2000)
                                music_thread(audio.menu_music, "menu_music.wav")
                                game_over = True
                        
                        except ValueError : 

                            pygame.mixer.music.pause()

                            screen.blit(kate_img[1], (kate_x, kate_y))
                            screen.blit(kate_db, (db_x, db_y))
                            pygame.display.flip()
                                
                            tts(screen, invalid_input_roasts(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                            
                            pygame.mixer.music.unpause()
                    
                    user_text = ""       # clear after enter, or break loop, etc.
                
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]   # remove last character
                else:
                    new_text = user_text + event.unicode 
                    new_surf = input_font.render(new_text, True, (40, 209, 52, 255))
                    # only accept if it fits within the box (minus padding)
                    if new_surf.get_width() <= (box_w - 2*padding_x):
                        user_text = new_text
            
        text_surface = input_font.render(user_text, True, (40, 209, 52, 255))
        
        text_w = text_surface.get_width()
        text_h = text_surface.get_height()
        cursor_y = text_y + text_h
        cursor_start = text_x + text_w + 2
        cursor_end = cursor_start + font_size//2
    
        if cursor_visible : 
            pygame.draw.line(screen, # game window pe draw karo
                            (40, 209, 52, 255), # rgba color code for white
                            (cursor_start, cursor_y), # start coordinates (x,y)
                            (cursor_end, cursor_y), # end coordinates (x,y) --> 236 - 200 = 36 (to match font size)
                            2) #thickness of the line in pixels
            
        
        screen.blit(text_surface, (text_x, text_y))
        screen.blit(kate_img[0], (kate_x, kate_y))


        pygame.display.flip()
        clock.tick(60)





    