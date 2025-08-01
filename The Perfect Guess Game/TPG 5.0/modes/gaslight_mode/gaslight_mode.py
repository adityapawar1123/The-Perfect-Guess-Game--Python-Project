def gaslight_mode(screen, screen_width, screen_height) : 
    
    import random 
    import threading
    import os 
    import time
    import sys
    
    from modes.gaslight_mode.prompts import roasts, otherprompts
    from data.prompts.common_prompts import rematch_prompts
    from UI.utils import Button

    # Set the environment variable BEFORE importing pygame
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame
    pygame.init()
    
    import pyttsx3
    engine = pyttsx3.init()

    path = os.path.dirname(os.path.abspath(__file__))
    mode_path = os.path.dirname(path)
    tpg_5 = os.path.dirname(mode_path)

    with open(os.path.join(tpg_5, "modes", "endgame_mode", "endgame_result.txt")) as f : 
        endgame_result = f.read()

    def set_female_voice():
        voices = engine.getProperty('voices')
        # Try setting the first available female voice (you might need to tweak the index)
        for voice in voices:
            if "zira" in voice.id.lower():  # Adjust as needed
                engine.setProperty('voice', voice.id)
                break
    
    def set_male_voice():
        voices = engine.getProperty('voices')
        for voice in voices:
            # On Windows, one of them is usually called “David” or has “male” in its name
            if "david" in voice.id.lower() or "male" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                return

    if endgame_result != "lost" : 
        set_female_voice()
    else : 
        set_male_voice()

    
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

    def only_tts(text) :
        engine.say(text)
        engine.runAndWait() 


    
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
    jokingo_db_path = os.path.join(tpg_5, "UI", "ui", "jokingo_db.png")

    
    kate_db_raw = pygame.image.load(kate_db_path).convert_alpha()
    db_width  = int(screen_width * 0.4)   # like 1000/1280
    db_height = int(screen_height * 0.15)  # like 180/720
    kate_db = pygame.transform.scale(kate_db_raw, (db_width, db_height))
    db_x = int((kate_x + kate_w) - kate_w*0.15) 
    db_y = (kate_y - (kate_y*0.05))  # push db toward bottom

    jokingo_db_raw = pygame.image.load(jokingo_db_path).convert_alpha()
    jokingo_db = pygame.transform.scale(jokingo_db_raw, (db_width, db_height))
    jokingo_db_x = int(screen_width*0.075)
    jokingo_db_y = int(screen_height*0.65)
    

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
    

    def jokingo_hints(screen, text, font_size, color, pos, max_width=None) : 
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
    
    

    easy_button = Button("01_easy.png", "02_easy.png", "03_easy.png", (0.50, 0.40), screen, screen_width, screen_height)    
    medium_button = Button("01_medium.png", "02_medium.png", "03_medium.png", (0.50, 0.50), screen, screen_width, screen_height)    
    hard_button = Button("01_hard.png", "02_hard.png", "03_hard.png", (0.50, 0.60), screen, screen_width, screen_height)    


    from modes.gaslight_mode.prompts.otherprompts import gaslight_mode_explain, first_guess_prompts, under_5_guess_prompts, mid_guess_prompts
    from modes.gaslight_mode.prompts.roasts import invalid_input_roasts, slow_guess_roasts, game_quit
    
    #Game vars
    difficulty_selected = False 
    kate = kate_img[0]
    kate_talking = True
    intro = True 
    clock = pygame.time.Clock()
    fps = 60
    
    while not difficulty_selected : 

        screen.blit(bkg, (0,0))

        if endgame_result != "lost" :
            if (kate_talking == True) and (intro == True) : 
                kate = kate_img[1]
                screen.blit(kate, (kate_x, kate_y))
                screen.blit(kate_db, (db_x, db_y))
                pygame.display.flip()

                tts(screen, gaslight_mode_explain(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                
                screen.blit(kate_db, (db_x, db_y))
                pygame.display.flip()
                tts(screen, "Choose the difficulty!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))

                kate_talking = False
                intro = False  
        
        if easy_button.draw() : 
            difficulty = "easy"

            if endgame_result != "lost" :
                kate = kate_img[1]
                screen.blit(kate, (kate_x, kate_y))
                screen.blit(kate_db, (db_x, db_y))
                pygame.display.flip()
                tts(screen, "You have to guess a number between 1 and 100", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))

            n = random.randint(1,100)
            lie_attempt = random.sample(range(1,5), 2) #gets 2 random number between 1 and 4

            difficulty_selected = True

        elif medium_button.draw() : 
            difficulty = "medium"

            if endgame_result != "lost" :
                kate = kate_img[1]
                screen.blit(kate, (kate_x, kate_y))
                screen.blit(kate_db, (db_x, db_y))
                pygame.display.flip()
                tts(screen, "You have to guess a number between 1 and 500", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))

            n = random.randint(1,500)
            lie_attempt = random.sample(range(1,7), 2)
            
            difficulty_selected = True
        
        elif hard_button.draw() : 
            difficulty = "hard"

            if endgame_result != "lost" :
                kate = kate_img[1]
                screen.blit(kate, (kate_x, kate_y))
                screen.blit(kate_db, (db_x, db_y))
                pygame.display.flip()
                tts(screen, "You have to guess a number between 1 and 1000", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))

            n = random.randint(1,1000)
            lie_attempt = random.sample(range(1,9), 2)

            difficulty_selected = True
        
        else : 
            if endgame_result != "lost" :
                kate = kate_img[0]
                screen.blit(kate, (kate_x, kate_y))
                pygame.display.flip()

        for event in pygame.event.get() : 

            if event.type == pygame.QUIT : 
                pygame.quit()
                sys.exit()
        
        pygame.display.flip()
        clock.tick(fps)

    


    game_over = False 
    input_off = False 
    kate = kate_img[0]
    guessNo = 0
    
    input_box_raw = pygame.image.load(os.path.join(tpg_5, "UI", "ui", "input_box.png")).convert_alpha()
    box_w = int(screen_width*0.4)
    box_h = int(screen_height*0.3)
    input_box = pygame.transform.scale(input_box_raw, (box_w, box_h))
    box_x  = int(screen_width * 0.5 - box_w * 0.5) # centered
    box_y  = int(screen_height * 0.5 - box_h*0.5)

    attempt_box_raw = pygame.image.load(os.path.join(tpg_5, "UI", "ui", "attempt_box.png")).convert_alpha()
    attempt_box_w = int(screen_width*0.23)
    attempt_box_h = int(screen_height*0.10)
    attempt_box = pygame.transform.scale(attempt_box_raw, (attempt_box_w, attempt_box_h))
    attempt_box_x = int(screen_width*0.062)
    attempt_box_y = int(screen_height*0.15)
    attempt_text_font = pygame.font.Font(input_font_path, int(attempt_box_h*0.40))

    font_size = int(screen_height*0.05)
    input_font = pygame.font.Font(input_font_path, font_size)
    padding_x = int(box_w*0.23) # 23% of box width
    text_x = box_x + padding_x
    text_y = box_y + ((box_h - font_size) // 4) + box_y*0.06
    user_text = ""    # This will hold what the player types

    last_cusor_toggle = pygame.time.get_ticks()
    CURSOR_DURATION = 500 # in ms
    cursor_visible = True 

    back_button = Button("01_back.png", "02_back.png", "03_back.png", (0.88, 0.865), screen, screen_width, screen_height)
    yes_button = Button("01_yes.png", "02_yes.png", "03_yes.png", (0.46, 0.70), screen, screen_width, screen_height)
    no_button = Button("01_no.png", "02_no.png", "03_no.png", (0.56, 0.70), screen, screen_width, screen_height)
    back_confirmation_font = pygame.font.Font(input_font_path, int(screen_height*0.025))

    music_thread(audio.gaslight_mode_music, "gaslight_mode.wav")
    while not game_over : 
        current = pygame.time.get_ticks()

        screen.blit(bkg, (0,0))
        screen.blit(input_box, (box_x, box_y))
        screen.blit(attempt_box, (attempt_box_x, attempt_box_y))
        attempt_text = attempt_text_font.render(f"ATTEMPTS : {guessNo}", True, (40, 209, 52, 255))
        screen.blit(attempt_text, (attempt_box_x + (attempt_box_x*0.20), attempt_box_y + (attempt_box_y*0.20)))

        if back_button.draw() : 

            input_off = True 
            while True : 
                screen.blit(bkg, (0,0))
                if endgame_result != "lost" :
                    screen.blit(kate_img[0], (kate_x, kate_y))
                screen.blit(input_box, (box_x, box_y))
                back_confirmation = back_confirmation_font.render(f"WANNA GO BACK TO MENU?", True, (40, 209, 52, 255))
                screen.blit(back_confirmation, (text_x, text_y + text_y*0.02))
                
                
                if yes_button.draw() : 
                    
                    pygame.mixer.music.fadeout(2000)
                    screen.blit(bkg, (0,0))
                    screen.blit(input_box, (box_x, box_y))
                    screen.blit(back_confirmation, (text_x, text_y + text_y*0.02))
                    if endgame_result != "lost" :
                        screen.blit(kate_img[1], (kate_x, kate_y))
                        screen.blit(kate_db, (db_x, db_y))
                    pygame.display.flip()

                    if endgame_result != "lost" :
                        tts(screen, game_quit(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                    
                    music_thread(audio.menu_music, "menu_music.wav")
                    return # Exits normal game mode, instead of starting the score-board loop
                
                if no_button.draw() : 
                    input_off = False
                    pygame.event.clear() 
                    break #breaks the inner loop and goes back to game

                for event in pygame.event.get() : 
                    if event.type == pygame.QUIT: 
                        pygame.quit()
                        sys.exit()
                
                pygame.display.flip()
                clock.tick(60)
        
        if current - last_cusor_toggle >= CURSOR_DURATION : 
            last_cusor_toggle = current 
            cursor_visible = not cursor_visible

        for event in pygame.event.get() :

            if event.type == pygame.QUIT : 
                pygame.quit()
                sys.exit()
            
            if input_off == False : 

                if event.type == pygame.KEYDOWN : 

                    if event.key == pygame.K_RETURN:

                        if user_text != '' : 
                            try : 
                                input_off = True
                                user_text = int(user_text)
                                
                                if user_text > n : 
                                    
                                    if endgame_result != "lost" :
                                        screen.blit(kate_img[1], (kate_x, kate_y))
                                        screen.blit(kate_db, (db_x, db_y))
                                    else : 
                                        screen.blit(jokingo_db, (jokingo_db_x, jokingo_db_y))
                                    pygame.display.flip()
                                    
                                    if guessNo in lie_attempt :
                                        if endgame_result != "lost" : 
                                            tts(screen, "Guess a higher number!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                        else : 
                                            screen.blit(jokingo_db, (jokingo_db_x, jokingo_db_y))
                                            tts(screen, "Guess a higher number!", int(screen_height*0.025), (0, 0, 0), (jokingo_db_x + jokingo_db_x*0.063 , jokingo_db_y + jokingo_db_y*0.09))
                                    else : 
                                        if endgame_result != "lost" :
                                            tts(screen, "Guess a lower number!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                        else : 
                                            tts(screen, "Guess a lower number!", int(screen_height*0.025), (0, 0, 0), (jokingo_db_x + jokingo_db_x*0.063 , jokingo_db_y + jokingo_db_y*0.09))

                                    guessNo += 1

                                elif user_text < n : 

                                    if endgame_result != "lost" : 
                                        screen.blit(kate_img[1], (kate_x, kate_y))
                                        screen.blit(kate_db, (db_x, db_y))
                                    else : 
                                        screen.blit(jokingo_db, (jokingo_db_x, jokingo_db_y))
                                    pygame.display.flip()
                                    
                                    if guessNo in lie_attempt : 
                                        if endgame_result != "lost" :
                                            tts(screen, "Guess a lower number!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                        else : 
                                            tts(screen, "Guess a lower number!", int(screen_height*0.025), (0, 0, 0), (jokingo_db_x + jokingo_db_x*0.063 , jokingo_db_y + jokingo_db_y*0.09))
                                    else :
                                        if endgame_result != "lost" : 
                                            tts(screen, "Guess a higher number!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                        else : 
                                            tts(screen, "Guess a higher number!", int(screen_height*0.025), (0, 0, 0), (jokingo_db_x + jokingo_db_x*0.063 , jokingo_db_y + jokingo_db_y*0.09))

                                    guessNo += 1

                                elif user_text == n : 
                                    
                                    guessNo += 1

                                    sound_effect_channel = pygame.mixer.Channel(1)
                                    win_sound_effect_path = os.path.join(tpg_5, "audio", "sound_effect", "win_sound_effect.mp3")
                                    win_sound_effect = pygame.mixer.Sound(win_sound_effect_path)
                                    sound_effect_channel.set_volume(1) # volume on 100%
                                    
                                    pygame.mixer.music.fadeout(1000)
                                    sound_effect_channel.play(win_sound_effect)
                                    while sound_effect_channel.get_busy() : 
                                        pygame.time.wait(10) #Checks every 10sec if channel is still busy

                                    if difficulty == "easy" : 
                                        if guessNo == 1 : 
                                            win_prompt = first_guess_prompts()
                                        elif 2 <= guessNo < 3 : 
                                            win_prompt = under_5_guess_prompts(guessNo)
                                        elif 3 <= guessNo <= 5 : 
                                            win_prompt = mid_guess_prompts(guessNo)
                                        else : 
                                            win_prompt = slow_guess_roasts(guessNo)
                                    
                                    elif difficulty == "medium" : 
                                        if guessNo == 1 : 
                                            win_prompt = first_guess_prompts()
                                        elif 2 <= guessNo < 4 : 
                                            win_prompt = under_5_guess_prompts(guessNo)
                                        elif 4 <= guessNo <= 7 : 
                                            win_prompt = mid_guess_prompts(guessNo)
                                        else : 
                                            win_prompt = slow_guess_roasts(guessNo)
                                    
                                    elif difficulty == "hard" : 
                                        if guessNo == 1 : 
                                            win_prompt = first_guess_prompts()
                                        elif 2 <= guessNo < 6 : 
                                            win_prompt = under_5_guess_prompts(guessNo)
                                        elif 6 <= guessNo <= 8 : 
                                            win_prompt = mid_guess_prompts(guessNo)
                                        else : 
                                            win_prompt = slow_guess_roasts(guessNo)
                                    
                                    if endgame_result != "lost" :
                                        screen.blit(kate_img[1], (kate_x, kate_y))
                                        screen.blit(kate_db, (db_x, db_y))

                                    screen.blit(attempt_box, (attempt_box_x, attempt_box_y))
                                    attempt_text = attempt_text_font.render(f"ATTEMPTS : {guessNo}", True, (40, 209, 52, 255))
                                    screen.blit(attempt_text, (attempt_box_x + (attempt_box_x*0.20), attempt_box_y + (attempt_box_y*0.20)))
                                    pygame.display.flip()
                                    
                                    if endgame_result != "lost" :
                                        tts(screen, win_prompt, int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                    
                                    music_thread(audio.menu_music, "menu_music.wav")
                                    game_over = True
                            
                            except ValueError : 

                                if endgame_result != "lost" :
                                    pygame.mixer.music.pause()

                                    screen.blit(kate_img[1], (kate_x, kate_y))
                                    screen.blit(kate_db, (db_x, db_y))
                                    pygame.display.flip()
                                        
                                    tts(screen, invalid_input_roasts(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                    
                                    pygame.mixer.music.unpause()
                                continue
                            
                            finally : 
                                input_off = False 
                                pygame.event.clear()
                        
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
        if endgame_result != "lost" :
            screen.blit(kate_img[0], (kate_x, kate_y))


        pygame.display.flip()
        clock.tick(60)

    
    
    endgame_unlocker_path = os.path.join(path, "data", "endgame_unlocker.txt")
    endgame_hinter_unlocker_path = os.path.join(tpg_5, "data", "endgame_hinter_unlocker.txt")
    highscore_path = os.path.join(tpg_5, "modes", "gaslight_mode", "highscores", f"{difficulty}_highscore.txt")
    with open(highscore_path) as f : 
        highscore = f.read().strip()

        if highscore != "" : 
            highscore = int(highscore)
        else : 
            highscore = 1000
        
        if guessNo < highscore : 
            highscore = guessNo
            with open(highscore_path, "w") as f1 : 
                f1.write(str(highscore))
            
            highscore_sound_effect_path = os.path.join(tpg_5, "audio", "sound_effect", "new_highscore_sound_effect.mp3")
            highscore_sound_effect = pygame.mixer.Sound(highscore_sound_effect_path)

            sound_effect_channel_2 = pygame.mixer.Channel(2)
            sound_effect_channel_2.set_volume(1)
            sound_effect_channel_2.play(highscore_sound_effect)
            while sound_effect_channel_2.get_busy() : 
                screen.blit(bkg, (0,0))
                
                screen.blit(input_box, (box_x, box_y))
                highscore_msg = input_font.render("NEW HIGHSCORE!", True, (40, 209, 52, 255))
                screen.blit(highscore_msg, (text_x, text_y))
                
                if endgame_result != "lost" :
                    screen.blit(kate_img[0], (kate_x, kate_y))
                
                pygame.display.flip()
                clock.tick(60)
            time.sleep(3)
    

    endgame_unlocked_screen = False #By default
    with open(endgame_unlocker_path) as f : 
        endgame_unlocker = f.read()

    if difficulty == "easy" : 
        if endgame_unlocker != "lock" and highscore <= 9 : 
            endgame_unlocked_screen = True 
    
    elif difficulty == "medium" : 
        if endgame_unlocker != "lock" and highscore <= 15 : 
            endgame_unlocked_screen = True 
    
    elif difficulty == "hard" : 
        if endgame_unlocker != "lock" and highscore <= 20 : 
            endgame_unlocked_screen = True 
    

    endgame_locker = os.path.join(tpg_5, "modes", "endgame_mode", "endgame_unlock.txt")
    if endgame_unlocked_screen == True : 

        with open(endgame_locker, "w") as f : 
            f.write("unlock")

        pygame.mixer.music.pause()
        endgame_sound_effect_path = os.path.join(tpg_5, "audio", "sound_effect", "endgame_unlock_sound_effect.wav")
        endgame_sound_effect = pygame.mixer.Sound(endgame_sound_effect_path)

        sound_effect_channel_3 = pygame.mixer.Channel(2)
        sound_effect_channel_3.set_volume(1)
        sound_effect_channel_3.play(endgame_sound_effect)
        while sound_effect_channel_3.get_busy() : 
                screen.blit(bkg, (0,0))
                
                screen.blit(input_box, (box_x, box_y))
                endgame_unlock_text1 = input_font.render("ENDGAME", True, (40, 209, 52, 255))
                endgame_unlock_text2 = input_font.render("UNLOCKED", True, (40, 209, 52, 255))
                screen.blit(endgame_unlock_text1, (text_x, text_y))
                screen.blit(endgame_unlock_text2, (text_x, int(text_y + endgame_unlock_text1.get_height() + endgame_unlock_text1.get_height()*0.25)))
                
                
                pygame.display.flip()
                clock.tick(60)
        time.sleep(3)
        pygame.mixer.music.unpause()
        
        

    with open(endgame_hinter_unlocker_path) as f : 
        unlocker = f.read()
    
    endgame_hinter = os.path.join(tpg_5, "data", "endgame_hinter.txt")

    if unlocker != "lock" : 
        with open(endgame_hinter) as f : 
            data = f.read().strip()
        
        if int(data)%4 == 0 and int(data) != 0 : 
            jokingo_hint_active = True 
            
            random_hint = random.randint(1,22)
            hint_path = os.path.join(tpg_5, "audio", "voicelines", "jokingo", "endgame_hints", f"line_{random_hint}.txt")
            with open(hint_path, "r", encoding="utf-8") as f : 
                hint = f.read().strip()
            hint_audio = pygame.mixer.Sound(os.path.join(tpg_5, "audio", "voicelines", "jokingo", "endgame_hints", f"line_{random_hint}.wav"))        
        
        else :
            jokingo_hint_active = False

        updated_data = int(data) + 1
        with open(endgame_hinter, "w") as f : 
            f.write(str(updated_data))
        

    
        if jokingo_hint_active == True : 
            voice_db_raw = pygame.image.load(voice_db_path).convert_alpha()
            db_width  = int(screen_width * 0.4)   # like 1000/1280
            db_height = int(screen_height * 0.15)  # like 180/720
            voice_db = pygame.transform.scale(voice_db_raw, (db_width, db_height))
            voice_db_x = int(screen_width*0.53) 
            voice_db_y = (screen_height*0.70)  # push db toward bottom
    
    else : 
        jokingo_hint_active = False
    
    continue_button = Button("01_continue.png", "02_continue.png", "03_continue.png", (0.88, 0.865), screen, screen_width, screen_height)
    scoreboard_font = pygame.font.Font(input_font_path, int(screen_height*0.025))

    scoreboard_exit = False 
    kate_rematch_prompt = True
    while not scoreboard_exit : 

        screen.blit(bkg, (0,0))
        if endgame_result != "lost" :
            screen.blit(kate_img[0], (kate_x, kate_y))
        screen.blit(input_box, (box_x, box_y))
        
        current_score = scoreboard_font.render(f"CURRENT SCORE : {guessNo}", True, (40, 209, 52, 255))
        highscore_render = scoreboard_font.render(f"HIGHSCORE : {highscore}", True, (40, 209, 52, 255))
        screen.blit(current_score, (text_x, text_y))
        screen.blit(highscore_render, (text_x, text_y + text_h + (text_h*0.20)))


        if jokingo_hint_active == True : 
            screen.blit(bkg, (0,0))
            screen.blit(input_box, (box_x, box_y))
            screen.blit(voice_db, (voice_db_x, voice_db_y))
            
            current_score = scoreboard_font.render(f"CURRENT SCORE : {guessNo}", True, (40, 209, 52, 255))
            highscore_render = scoreboard_font.render(f"HIGHSCORE : {highscore}", True, (40, 209, 52, 255))
            screen.blit(current_score, (text_x, text_y))
            screen.blit(highscore_render, (text_x, text_y + text_h + (text_h*0.20)))

            pygame.display.flip()

            jokingo_hints(screen, hint, int(screen_height*0.025), (0,0,0), 
                          (voice_db_x + voice_db_x*0.02, voice_db_y + voice_db_y*0.07),)
            
            sound_effect_channel_3 = pygame.mixer.Channel(3)
            sound_effect_channel_3.set_volume(1)
            
            pygame.mixer.music.pause()
            sound_effect_channel_3.play(hint_audio)
            while sound_effect_channel_3.get_busy() : 
                pygame.time.wait(10)
            time.sleep(3)
            pygame.mixer.music.unpause()
            
            jokingo_hint_active = False 

        if endgame_result != "lost" :
            if kate_rematch_prompt == True : 
                screen.blit(bkg, (0,0))
                screen.blit(kate_img[1], (kate_x, kate_y))
                screen.blit(kate_db, (db_x, db_y))
                
                screen.blit(input_box, (box_x, box_y))
                current_score = scoreboard_font.render(f"CURRENT SCORE : {guessNo}", True, (40, 209, 52, 255))
                highscore_render = scoreboard_font.render(f"HIGHSCORE : {highscore}", True, (40, 209, 52, 255))
                screen.blit(current_score, (text_x, text_y))
                screen.blit(highscore_render, (text_x, text_y + text_h + (text_h*0.20)))

                pygame.display.flip()
                
                tts(screen, rematch_prompts(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                kate_rematch_prompt = False
        
        if continue_button.draw() : 
            scoreboard_exit = True 
            
        
        for event in pygame.event.get() : 

            if event.type == pygame.QUIT : 
                pygame.quit()
                sys.exit()
        
        
        pygame.display.flip()
        clock.tick(60)
    
    