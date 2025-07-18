def timebound_mode(screen, screen_width, screen_height) : 
    import random 
    import threading
    import os 
    import time
    import sys
    
    from modes.timebound_mode.prompts import roasts, otherprompts
    from data.prompts.common_prompts import rematch_prompts, custom_reversed_range_roasts
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

    set_female_voice()

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
        set_male_voice() #AFTERMATH UPDATE

    
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

    clock_ticking_sound_effect = pygame.mixer.Sound(os.path.join(tpg_5, "audio", "sound_effect", "clock_ticking.wav"))
    clock_ticking_sound_effect.set_volume(0.3)
    def countdown(countdown_secs) :
        while countdown_secs['remaining_time'] > 0 : 
            
            if countdown_secs.get('pause_timer', False) : 
                time.sleep(0.1)
                continue
            
            else : 
                time.sleep(1)
                countdown_secs['remaining_time'] -= 1
                pygame.mixer.Sound.play(clock_ticking_sound_effect)
                    
                if countdown_secs['remaining_time'] == 10 : 
                    pygame.mixer.music.stop()
                    music_thread(audio.timebound_mode_music, "timebound_10_sec_left.wav")
    
    
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
        clock.tick(fps)
    
    
    def custom_input(screen, screen_width, screen_height, bkg, input_box, kate_img, kate_db, endgame_result, prompt_text) : 
        
        n1 = ""
        prompt = False
        input_font = pygame.font.Font(input_font_path, font_size)

        last_cusor_toggle = pygame.time.get_ticks()
        CURSOR_DURATION = 500 # in ms
        cursor_visible = True

        box_w = int(screen_width*0.4)
        box_h = int(screen_height*0.3)
        box_x  = int(screen_width * 0.5 - box_w * 0.5) # centered
        box_y  = int(screen_height * 0.5 - box_h*0.5)
        kate_x = int(screen_width*0.03) 
        kate_y = int(screen_height*0.7)
        kate_w = int(screen_width*0.2)
        kate_h = int(screen_height*0.4)
        db_x = int((kate_x + kate_w) - kate_w*0.15) 
        db_y = (kate_y - (kate_y*0.05))  # push db toward bottom  

        while True : 
                current = pygame.time.get_ticks()

                screen.blit(bkg, (0,0))
                screen.blit(input_box, (box_x, box_y))
                if endgame_result != "lost" : 
                    screen.blit(kate_img[0], (kate_x, kate_y))
                
                if prompt == False and endgame_result != "lost" : 
                    screen.blit(bkg, (0,0))
                    screen.blit(input_box, (box_x, box_y))
                    screen.blit(kate_img[1], (kate_x, kate_y))
                    screen.blit(kate_db, (db_x, db_y))
                    tts(screen, prompt_text, int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                    prompt = True
                    continue

                if current - last_cusor_toggle >= CURSOR_DURATION : 
                    last_cusor_toggle = current 
                    cursor_visible = not cursor_visible # Flips True to False and False to True

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:

                            try : 
                                n1 = int(n1)
                                if n1 < 0 : 
                                    raise Exception("Negative_Number")
                                else : 
                                    return n1
                            
                            except ValueError :

                                if endgame_result != "lost" :
                                    
                                    screen.blit(bkg, (0,0))
                                    screen.blit(input_box, (box_x, box_y))
                                    screen.blit(kate_img[1], (kate_x, kate_y))
                                    screen.blit(kate_db, (db_x, db_y))

                                    pygame.mixer.music.pause()
                                    tts(screen, invalid_input_roasts(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                    pygame.mixer.music.unpause()
                                    
                                    continue
                            
                            except Exception as e : 

                                if str(e) == "Negative_Number" : 

                                    if endgame_result != "lost" :

                                        negative_num_roasts = random.choice(["Seriously? A negative number?",
                                                                             "What you thought you'd break the game? Enter a POSITIVE number!",
                                                                             "Cute try, now enter a positive goddamn number!",
                                                                             "Aww my little hacker, look at you entering negative numbers.",
                                                                             "You thought that'd do something huh? Enter a POSITIVE number!"])
                                    
                                        screen.blit(bkg, (0,0))
                                        screen.blit(input_box, (box_x, box_y))
                                        screen.blit(kate_img[1], (kate_x, kate_y))
                                        screen.blit(kate_db, (db_x, db_y))

                                        pygame.mixer.music.pause()
                                        tts(screen, negative_num_roasts, int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                        pygame.mixer.music.unpause()

                                        n1 = str(n1)
                                        
                                        continue

                            n1 = ""       # clear after enter, or break loop, etc.
                        
                        elif event.key == pygame.K_BACKSPACE:
                            n1 = n1[:-1]   # remove last character
                        else:
                            new_text = n1 + event.unicode 
                            new_surf = input_font.render(str(new_text), True, (40, 209, 52, 255))
                            # only accept if it fits within the box (minus padding)
                            if new_surf.get_width() <= (box_w - 2*padding_x):
                                n1 = new_text

                # 3) Render the current text
                text_surface = input_font.render(str(n1), True, (40, 209, 52, 255))

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

                pygame.display.flip()
                clock.tick(60)
    
    

    easy_button = Button("01_easy.png", "02_easy.png", "03_easy.png", (0.50, 0.35), screen, screen_width, screen_height)    
    medium_button = Button("01_medium.png", "02_medium.png", "03_medium.png", (0.50, 0.45), screen, screen_width, screen_height)    
    hard_button = Button("01_hard.png", "02_hard.png", "03_hard.png", (0.50, 0.55), screen, screen_width, screen_height)
    custom_button = Button("01_custom.png", "02_custom.png", "03_custom.png", (0.50, 0.65), screen, screen_width, screen_height)    


    from modes.timebound_mode.prompts.otherprompts import timebound_mode_explain, win_prompts, lose_prompts
    from modes.timebound_mode.prompts.roasts import invalid_input_roasts, game_quit
    
    #Game vars
    difficulty_selected = False 
    kate = kate_img[0]
    kate_talking = True
    intro = True 
    clock = pygame.time.Clock()
    fps = 60

    input_box_raw = pygame.image.load(os.path.join(tpg_5, "UI", "ui", "input_box.png")).convert_alpha()
    box_w = int(screen_width*0.4)
    box_h = int(screen_height*0.3)
    input_box = pygame.transform.scale(input_box_raw, (box_w, box_h))
    box_x  = int(screen_width * 0.5 - box_w * 0.5) # centered
    box_y  = int(screen_height * 0.5 - box_h*0.5)

    timer_box_raw = pygame.image.load(os.path.join(tpg_5, "UI", "ui", "timer.png"))
    timer_w = int(screen_width*0.25)
    timer_h = int(screen_height*0.15)
    timer_box = pygame.transform.scale(timer_box_raw, (timer_w, timer_h))
    timer_x = int(screen_width*0.50 - timer_w*0.50)
    timer_y = int(screen_height*0.15)
    countdown_secs_text_font = pygame.font.Font(input_font_path, int(timer_h*0.40))

    font_size = int(screen_height*0.05)
    input_font = pygame.font.Font(input_font_path, font_size)
    padding_x = int(box_w*0.23) # 23% of box width
    text_x = box_x + padding_x
    text_y = box_y + ((box_h - font_size) // 4) + box_y*0.06
    user_text = ""    # This will hold what the player types
    
    while not difficulty_selected : 

        screen.blit(bkg, (0,0))

        if endgame_result != "lost" :
            if (kate_talking == True) and (intro == True) : 
                kate = kate_img[1]
                screen.blit(kate, (kate_x, kate_y))
                screen.blit(kate_db, (db_x, db_y))
                pygame.display.flip()

                tts(screen, timebound_mode_explain(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                
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
            difficulty_selected = True
        
        elif custom_button.draw() : 
            difficulty = "custom" 
            
            n1_prompt = random.choice(["What number do you want to start the range from?", 
                                       "I swear, if you say 69, I'm judging you. What's the starting number?",
                                       "Alright, what's the first number in your custom range?"])
            n1 = custom_input(screen, screen_width, screen_height, bkg, input_box, 
                              kate_img, kate_db, endgame_result, n1_prompt)
            
            if endgame_result == "lost" :
                screen.blit(bkg, (0,0))
                screen.blit(jokingo_db, (jokingo_db_x, jokingo_db_y))
                tts(screen, "Enter the maximum number you want in range.", 
                    int(screen_height*0.025), (0, 0, 0), (jokingo_db_x + jokingo_db_x*0.063 , jokingo_db_y + jokingo_db_y*0.09))
            
            n2_prompt = random.choice(["Now, what's the last number in your range?", 
                                       "Alright, what's the maximum number?",
                                       "You better not make this too easy. What's the top number?",
                                       "Enter end of the range. And no, infinity isn't allowed."])
            n2 = custom_input(screen, screen_width, screen_height, bkg, input_box, 
                              kate_img, kate_db, endgame_result, n2_prompt)

            
            try :  
                
                n = random.randint(n1, n2)
                if endgame_result != "lost" : 
                    screen.blit(bkg, (0,0))
                    screen.blit(kate_img[1], (kate_x, kate_y))
                    screen.blit(kate_db, (db_x, db_y))
                    tts(screen, f"You have to guess a number between {n1} and {n2}.", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                difficulty_selected = True
            
            except ValueError : #if the players switch the order of n1 and n2
                if endgame_result != "lost" :
                    screen.blit(bkg, (0,0))
                    screen.blit(kate_img[1], (kate_x, kate_y))
                    screen.blit(kate_db, (db_x, db_y))
                    tts(screen, custom_reversed_range_roasts(n1,n2), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                else : 
                    screen.blit(bkg, (0,0))
                    screen.blit(jokingo_db, (jokingo_db_x, jokingo_db_y))
                    tts(screen, "Please put the number range in increasing order.", 
                    int(screen_height*0.025), (0, 0, 0), (jokingo_db_x + jokingo_db_x*0.063 , jokingo_db_y + jokingo_db_y*0.09))
        
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

    timer_selected = False 
    timer_prompt = True
    
    ten_secs_button = Button("01_10secs.png", "02_10secs.png", "03_10secs.png", (0.50, 0.30), screen, screen_width, screen_height)
    twenty_secs_button = Button("01_20secs.png", "02_20secs.png", "03_20secs.png", (0.50, 0.40), screen, screen_width, screen_height)    
    thirty_secs_button = Button("01_30secs.png", "02_30secs.png", "03_30secs.png", (0.50, 0.50), screen, screen_width, screen_height)
    forty_secs_button = Button("01_40secs.png", "02_40secs.png", "03_40secs.png", (0.50, 0.60), screen, screen_width, screen_height)
    custom_button = Button("01_custom.png", "02_custom.png", "03_custom.png", (0.50, 0.70), screen, screen_width, screen_height)

    while not timer_selected : 

        screen.blit(bkg, (0,0))
        if endgame_result != "lost" :
            screen.blit(kate_img[0], (kate_x, kate_y))

        if endgame_result != "lost" :
            if timer_prompt == True : 
                screen.blit(bkg, (0,0))
                screen.blit(kate_img[1], (kate_x, kate_y))
                screen.blit(kate_db, (db_x, db_y))
                pygame.display.flip()
                tts(screen, "Pick a time limit: 10, 20, 30 or 40 seconds?", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                timer_prompt = False
            
        if ten_secs_button.draw() : 
            countdown_secs = 10 
            timer_selected = True
        
        elif twenty_secs_button.draw() : 
            countdown_secs = 20
            timer_selected = True
        
        elif thirty_secs_button.draw() :
            countdown_secs = 30 
            timer_selected = True 

        elif forty_secs_button.draw() : 
            countdown_secs = 40 
            timer_selected = True

        if difficulty == "custom" :

            if custom_button.draw() :
                if endgame_result == "lost" : 
                    screen.blit(bkg, (0,0))
                    screen.blit(jokingo_db, (jokingo_db_x, jokingo_db_y))
                    pygame.display.flip()
                    tts(screen, "Select a timer.", int(screen_height*0.025), (0, 0, 0), (jokingo_db_x + jokingo_db_x*0.063 , jokingo_db_y + jokingo_db_y*0.09))
                
                countdown_secs = custom_input(screen, screen_width, screen_height, bkg, input_box, 
                                kate_img, kate_db, endgame_result, otherprompts.custom_timer_prompts())
                timer_selected = True 

        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                pygame.quit()
                sys.exit() 
        
        pygame.display.flip()
        clock.tick(fps)




    music_thread(audio.timebound_mode_music, "timebound_mode.wav")
    game_over = False 
    input_off = False
    kate = kate_img[0]
    guessNo = 0 


    last_cusor_toggle = pygame.time.get_ticks()
    CURSOR_DURATION = 500 # in ms
    cursor_visible = True 

    back_button = Button("01_back.png", "02_back.png", "03_back.png", (0.88, 0.865), screen, screen_width, screen_height)
    yes_button = Button("01_yes.png", "02_yes.png", "03_yes.png", (0.46, 0.70), screen, screen_width, screen_height)
    no_button = Button("01_no.png", "02_no.png", "03_no.png", (0.56, 0.70), screen, screen_width, screen_height)
    back_confirmation_font = pygame.font.Font(input_font_path, int(screen_height*0.028))

    shared_state = {'remaining_time' : countdown_secs, 'pause_timer' : False}
    timer_thread = threading.Thread(target=countdown, args=(shared_state, ), daemon=True)
    timer_thread.start() #can't put this in loop as threads can only be started once
    while not game_over : 
        current = pygame.time.get_ticks()
        
        try : 
            if shared_state["remaining_time"] <= 0 : 
                input_off = True
                raise Exception("Time_Out") #So it comes to hard stop no matter wht the player is doing at the time
        
        except Exception as e :

            if str(e) == "Time_Out" :  
                sound_effect_channel = pygame.mixer.Channel(1)
                timer_beep_path = os.path.join(tpg_5, "audio", "sound_effect", "timer_beep.mp3")
                timer_beep = pygame.mixer.Sound(timer_beep_path)
                lose_sound_effect_path = os.path.join(tpg_5, "audio", "sound_effect", "lose_sound_effect.mp3")
                lose_sound_effect = pygame.mixer.Sound(lose_sound_effect_path)
                sound_effect_channel.set_volume(1) # volume on 100%

                pygame.mixer.music.fadeout(1000)

                screen.blit(bkg, (0,0))
                screen.blit(input_box, (box_x, box_y))
                screen.blit(timer_box, (timer_x, timer_y))
                countdown_secs_text = countdown_secs_text_font.render(f"00:00", True, (136, 8, 8))
                if countdown_secs <= 60 : 
                    screen.blit(countdown_secs_text, (timer_x + (timer_x*0.19), timer_y + (timer_y*0.35)))
                else : 
                    screen.blit(custom_countdown_secs_text, (custom_countdown_x, custom_countdown_y))
                if endgame_result != "lost" :
                    screen.blit(kate_img[1], (kate_x, kate_y))
                pygame.display.flip()

                
                sound_effect_channel.play(timer_beep)
                while sound_effect_channel.get_busy() : 
                    pygame.time.wait(10)
                
                sound_effect_channel.play(lose_sound_effect)
                while sound_effect_channel.get_busy() : 
                    pygame.time.wait(10) #Checks every 10sec if channel is still busy
                                
                

                if endgame_result != "lost" and difficulty != "custom" :
                    screen.blit(kate_db, (db_x, db_y))
                    tts(screen, lose_prompts(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                
                elif endgame_result != "lost" and difficulty == "custom" :
                    screen.blit(kate_db, (db_x, db_y)) 
                    tts(screen, roasts.custom_lose_roasts(countdown_secs), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                
                music_thread(audio.menu_music, "menu_music.wav")
                game_over = True

        if shared_state["remaining_time"] >= 10 : 
            timer_padding = ""
        else : 
            timer_padding = "0"

        screen.blit(bkg, (0,0))
        screen.blit(input_box, (box_x, box_y))
        screen.blit(timer_box, (timer_x, timer_y))
        countdown_secs_text = countdown_secs_text_font.render(f"00:{timer_padding}{shared_state['remaining_time']}", True, (136, 8, 8))
        custom_countdown_secs_text = countdown_secs_text_font.render(f"{shared_state['remaining_time']}", True, (136, 8, 8))

        if countdown_secs <= 60 : 
            screen.blit(countdown_secs_text, (timer_x + (timer_x*0.19), timer_y + (timer_y*0.35)))
        else :
            custom_countdown_x = int(timer_x + (timer_w//2 - custom_countdown_secs_text.get_width()//2))
            custom_countdown_y = int(timer_y + (timer_h//2 - custom_countdown_secs_text.get_height()//2)) 
            screen.blit(custom_countdown_secs_text, (custom_countdown_x, custom_countdown_y))

        if back_button.draw() : 

            shared_state['pause_timer'] = True 
            input_off = True
            while True : 
                screen.blit(bkg, (0,0))
                screen.blit(input_box, (box_x, box_y))
                if endgame_result != "lost" :
                    screen.blit(kate_img[0], (kate_x, kate_y))
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
                    return # Exits game mode, instead of starting the score-board loop
                
                if no_button.draw() : 
                    shared_state['pause_timer'] = False
                    input_off = False
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
                                user_text = int(user_text)
                                
                                if user_text > n : 
                                    guessNo += 1
                                    
                                    if endgame_result != "lost" :
                                        screen.blit(bkg, (0,0))
                                        screen.blit(input_box, (box_x, box_y))
                                        screen.blit(timer_box, (timer_x, timer_y))
                                        if countdown_secs <= 60 : 
                                            screen.blit(countdown_secs_text, (timer_x + (timer_x*0.19), timer_y + (timer_y*0.35)))
                                        else : 
                                            screen.blit(custom_countdown_secs_text, (custom_countdown_x, custom_countdown_y))

                                        screen.blit(kate_img[1], (kate_x, kate_y))
                                        screen.blit(kate_db, (db_x, db_y))
                                        pygame.display.flip()
                                        tts(screen, "Guess a lower number!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                    else : 
                                        screen.blit(jokingo_db, (jokingo_db_x, jokingo_db_y))
                                        pygame.display.flip()
                                        tts(screen, "Guess a lower number!", int(screen_height*0.025), (0, 0, 0), (jokingo_db_x + jokingo_db_x*0.063 , jokingo_db_y + jokingo_db_y*0.09))

                                    

                                elif user_text < n : 
                                    guessNo += 1
                                    
                                    if endgame_result != "lost" :
                                        screen.blit(bkg, (0,0))
                                        screen.blit(input_box, (box_x, box_y))
                                        screen.blit(timer_box, (timer_x, timer_y))
                                        if countdown_secs <= 60 : 
                                            screen.blit(countdown_secs_text, (timer_x + (timer_x*0.19), timer_y + (timer_y*0.35)))
                                        else : 
                                            screen.blit(custom_countdown_secs_text, (custom_countdown_x, custom_countdown_y))

                                        screen.blit(kate_img[1], (kate_x, kate_y))
                                        screen.blit(kate_db, (db_x, db_y))
                                        pygame.display.flip()
                                        tts(screen, "Guess a higher number!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                    
                                    else : 
                                        screen.blit(jokingo_db, (jokingo_db_x, jokingo_db_y))
                                        pygame.display.flip()
                                        tts(screen, "Guess a higher number!", int(screen_height*0.025), (0, 0, 0), (jokingo_db_x + jokingo_db_x*0.063 , jokingo_db_y + jokingo_db_y*0.09))


                                elif user_text == n : 
                                    guessNo += 1

                                    shared_state["pause_timer"] = True
                                    sound_effect_channel = pygame.mixer.Channel(1)
                                    win_sound_effect_path = os.path.join(tpg_5, "audio", "sound_effect", "win_sound_effect.mp3")
                                    win_sound_effect = pygame.mixer.Sound(win_sound_effect_path)
                                    sound_effect_channel.set_volume(1) # volume on 100%
                                    
                                    pygame.mixer.music.fadeout(1000)
                                    
                                    if endgame_result != "lost" :
                                        screen.blit(bkg, (0,0))
                                        screen.blit(input_box, (box_x, box_y))
                                        screen.blit(timer_box, (timer_x, timer_y))
                                        if countdown_secs <= 60 : 
                                            screen.blit(countdown_secs_text, (timer_x + (timer_x*0.19), timer_y + (timer_y*0.35)))
                                        else : 
                                            screen.blit(custom_countdown_secs_text, (custom_countdown_x, custom_countdown_y))
                                        screen.blit(kate_img[1], (kate_x, kate_y)) 
                                    pygame.display.flip()
                                    
                                    sound_effect_channel.play(win_sound_effect)
                                    while sound_effect_channel.get_busy() : 
                                        pygame.time.wait(10) #Checks every 10sec if channel is still busy

                                    
                                    if endgame_result != "lost" :
                                        screen.blit(kate_db, (db_x, db_y))
                                        tts(screen, win_prompts(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                    
                                    music_thread(audio.menu_music, "menu_music.wav")
                                    game_over = True
                            
                            
                            except ValueError :
                                shared_state['pause_timer'] = True  

                                if endgame_result != "lost" :
                                    pygame.mixer.music.pause()

                                    screen.blit(bkg, (0,0))
                                    screen.blit(input_box, (box_x, box_y))
                                    screen.blit(timer_box, (timer_x, timer_y))
                                    if countdown_secs <= 60 : 
                                        screen.blit(countdown_secs_text, (timer_x + (timer_x*0.19), timer_y + (timer_y*0.35)))
                                    else : 
                                        screen.blit(custom_countdown_secs_text, (custom_countdown_x, custom_countdown_y))

                                    screen.blit(kate_img[1], (kate_x, kate_y))
                                    screen.blit(kate_db, (db_x, db_y))
                                    pygame.display.flip()
                                        
                                    tts(screen, invalid_input_roasts(), int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                    
                                    pygame.mixer.music.unpause()

                                shared_state['pause_timer'] = False 
                                continue
                        
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

    
    
        
        

    endgame_hinter_unlocker_path = os.path.join(tpg_5, "data", "endgame_hinter_unlocker.txt")
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
    line_spacing = int(scoreboard_font.get_height() + scoreboard_font.get_height()*0.60)

    scoreboard_exit = False 
    kate_rematch_prompt = True
    while not scoreboard_exit : 

        screen.blit(bkg, (0,0))
        if endgame_result != "lost" :
            screen.blit(kate_img[0], (kate_x, kate_y))
        screen.blit(input_box, (box_x, box_y))
        
        current_score = scoreboard_font.render(f"ATTEMPTS TAKEN : {guessNo}", True, (40, 209, 52, 255))
        if shared_state["remaining_time"] != 0 : 
            remaining_time = scoreboard_font.render(f"TIME REMAINING : {shared_state['remaining_time']+1}s", True, (40, 209, 52, 255))
        else : 
            remaining_time = scoreboard_font.render(f"TIME REMAINING : 0s", True, (40, 209, 52, 255))
        timer_text = scoreboard_font.render(f"TIMER : {countdown_secs}s", True, (40, 209, 52, 255))
        if difficulty == "custom" : 
            custom_range = scoreboard_font.render(f"RANGE : {n1} to {n2}", True, (40, 209, 52, 255))
        else : 
            difficulty_text = scoreboard_font.render(f"DIFFICULTY : {difficulty.upper()}", True, (40, 209, 52, 255))
        
        if difficulty == "custom" : 
            screen.blit(custom_range, (text_x, text_y))
            screen.blit(current_score, (text_x, text_y + line_spacing))
            screen.blit(timer_text, (text_x, text_y + 2*line_spacing))
            screen.blit(remaining_time, (text_x, text_y + 3*line_spacing))
        else : 
            screen.blit(difficulty_text, (text_x, text_y))
            screen.blit(current_score, (text_x, text_y + line_spacing))
            screen.blit(timer_text, (text_x, text_y + 2*line_spacing))
            screen.blit(remaining_time, (text_x, text_y + 3*line_spacing))
                


        if jokingo_hint_active == True : 
            screen.blit(bkg, (0,0))
            screen.blit(input_box, (box_x, box_y))
            screen.blit(voice_db, (voice_db_x, voice_db_y))
            
            if difficulty == "custom" : 
                screen.blit(custom_range, (text_x, text_y))
                screen.blit(current_score, (text_x, text_y + line_spacing))
                screen.blit(timer_text, (text_x, text_y + 2*line_spacing))
                screen.blit(remaining_time, (text_x, text_y + 3*line_spacing))
            else : 
                screen.blit(difficulty_text, (text_x, text_y))
                screen.blit(current_score, (text_x, text_y + line_spacing))
                screen.blit(timer_text, (text_x, text_y + 2*line_spacing))
                screen.blit(remaining_time, (text_x, text_y + 3*line_spacing))

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
                if difficulty == "custom" : 
                    screen.blit(custom_range, (text_x, text_y))
                    screen.blit(current_score, (text_x, text_y + line_spacing))
                    screen.blit(timer_text, (text_x, text_y + 2*line_spacing))
                    screen.blit(remaining_time, (text_x, text_y + 3*line_spacing))
                else : 
                    screen.blit(difficulty_text, (text_x, text_y))
                    screen.blit(current_score, (text_x, text_y + line_spacing))
                    screen.blit(timer_text, (text_x, text_y + 2*line_spacing))
                    screen.blit(remaining_time, (text_x, text_y + 3*line_spacing))

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