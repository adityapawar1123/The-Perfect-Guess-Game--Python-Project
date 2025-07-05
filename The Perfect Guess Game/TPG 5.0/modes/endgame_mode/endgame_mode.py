def endgame_mode(screen, screen_width, screen_height) : 
    import random 
    import threading
    import os 
    import time

    from UI.utils import Button, Syringe
    
    # Set the environment variable BEFORE importing pygame
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    import pygame
    pygame.font.init()
    
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

    from audio import audio, voicelines

    def tts(screen, text, font_size, color, pos, max_width=None, audio=True) : 
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
        
        if audio == True : 
            engine.say(text)
            engine.runAndWait()
    
    
    def fade(screen, fade_in=True, speed=10, color=(0, 0, 0)):
        fade_surface = pygame.Surface((screen.get_width(), screen.get_height())) #This creates a brand new surface the size of the screen
        fade_surface.fill(color)

        if fade_in:
            alpha_range = range(0, 256, speed) #0 is fully transparent, 255 is fully opaque, so invisible -> opaque
            #The speed decides how big the jumps are in each step. Smaller = smoother.
        else:
            alpha_range = range(255, -1, -speed) #opaque -> invisible

        for alpha in alpha_range:
            fade_surface.set_alpha(alpha) #sets how transparent the surface is. More alpha = more opaque
            screen.blit(fade_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(10)  # controls the speed of fade effect
    
    
    clock = pygame.time.Clock()
    fps = 60
    
    path = os.path.dirname(os.path.abspath(__file__))
    mode_path = os.path.dirname(path)
    tpg_5 = os.path.dirname(mode_path)
    
    
    def music_thread(func, file, duration=-1) : #by default duration stays on -1 i.e. runs song on infinite loop
        thread = threading.Thread(target= func, args=(file, duration), daemon=True)
        thread.start()

    def sound_effect_thread(func, file) : #by default duration stays on -1 i.e. runs song on infinite loop
        thread = threading.Thread(target= func, args=(file,), daemon=True)
        thread.start()
    #Seperating these functn(s) to prevent audio overlapping


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

    voiceline_channel = pygame.mixer.Channel(1)
    music_thread(audio.endgame_mode_music, "endgame_pleasant.wav")
    
    
    endgame_intro_1_over = False 
    while not endgame_intro_1_over : 

        kate_intro_voiceline_1 = pygame.mixer.Sound(os.path.join(tpg_5, "audio", "voicelines", "kate", "endgame_intro", "01_kate_endgame_intro.wav"))

        voiceline_channel.play(kate_intro_voiceline_1)
        while voiceline_channel.get_busy() : 
            screen.blit(bkg, (0,0))
            screen.blit(kate_img[1], (kate_x, kate_y))

            for event in pygame.event.get() :
                if event.type == pygame.QUIT : 
                    pygame.quit()
                    quit()
        
            pygame.display.flip()
            clock.tick(60)
        
        endgame_intro_1_over = True 
    

    raw_glitch_kate_talking = [
    pygame.image.load(os.path.join(tpg_5, "UI", "ui", "kate", "01_glitch_kate_talking.png")).convert_alpha(),
    pygame.image.load(os.path.join(tpg_5, "UI", "ui", "kate", "02_glitch_kate_talking.png")).convert_alpha(),
    pygame.image.load(os.path.join(tpg_5, "UI", "ui", "kate", "03_glitch_kate_talking.png")).convert_alpha()
    ]
    glitch_kate_talking_img = [
    pygame.transform.scale(img, (kate_w, kate_h))
    for img in raw_glitch_kate_talking
    ]  

    FRAME_DURATION = 400

    glitch_frame = 2 #default
    last_glitch_time = pygame.time.get_ticks()
    pygame.mixer.music.stop()

    endgame_intro_2_over = False 
    while not endgame_intro_2_over :

        kate_intro_voiceline_2 = pygame.mixer.Sound(os.path.join(tpg_5, "audio", "voicelines", "kate", "endgame_intro", "02_kate_endgame_intro.wav"))
        voiceline_channel.play(kate_intro_voiceline_2) 

        while voiceline_channel.get_busy() : 
            current = pygame.time.get_ticks() 
            if current - last_glitch_time >= FRAME_DURATION:
                # Switch between index 1 and 2
                if glitch_frame == 0 : 
                    glitch_frame = 1
                
                elif glitch_frame == 1 : 
                    glitch_frame = 2
                
                else : 
                    glitch_frame = 0
                
                last_glitch_time = current
            
            screen.blit(bkg, (0,0))
            screen.blit(glitch_kate_talking_img[glitch_frame], (kate_x, kate_y))
            
            for event in pygame.event.get() :
                if event.type == pygame.QUIT : 
                    pygame.quit()
                    quit()
            
            pygame.display.flip()
            clock.tick(fps)
        
        endgame_intro_2_over = True
        
        

    game_over = False 
    input_off = False
    show_truth_serum = False 
    truth_serum_activate = False
    kate_attempt_prompt = False
    
    n = random.randint(1, 500)
    truth_serum = 5
    attempts_left = 15

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
    attempt_text_font = pygame.font.Font(input_font_path, int(attempt_box_h*0.33))

    font_size = int(screen_height*0.05)
    input_font = pygame.font.Font(input_font_path, font_size)
    padding_x = int(box_w*0.23) # 23% of box width
    text_x = box_x + padding_x
    text_y = box_y + ((box_h - font_size) // 4) + box_y*0.06
    user_text = ""    # This will hold what the player types

    raw_glitch_kate_idle = [
    pygame.image.load(os.path.join(tpg_5, "UI", "ui", "kate", "01_glitch_kate.png")).convert_alpha(),
    pygame.image.load(os.path.join(tpg_5, "UI", "ui", "kate", "02_glitch_kate.png")).convert_alpha(),
    pygame.image.load(os.path.join(tpg_5, "UI", "ui", "kate", "03_glitch_kate.png")).convert_alpha()
    ]
    glitch_kate_idle_img = [
    pygame.transform.scale(img, (kate_w, kate_h))
    for img in raw_glitch_kate_idle
    ]  

    truth_serum_button = Syringe("01_truth_serum.png", "02_truth_serum.png", "03_truth_serum.png",
                                 (0.885, 0.205), screen, screen_width, screen_height)
    
    last_cusor_toggle = pygame.time.get_ticks()
    CURSOR_DURATION = 500 # in ms
    cursor_visible = True

    FRAME_DURATION = 400
    glitch_frame = 2 #default
    last_glitch_time = pygame.time.get_ticks() 

    music_thread(audio.endgame_mode_music, "endgame_mode.wav")
    while not game_over : 
        current = pygame.time.get_ticks()
        screen.blit(bkg, (0,0))

        if attempts_left == 0 : 
            endgame_result = "lost"
            pygame.mixer.music.stop()
            sound_effect_thread(audio.sound_effects, "lose_sound_effect.mp3")
            game_over = True

        if attempts_left <= 10 : 
            attempt_text_color = (136, 8, 8)
        else : 
            attempt_text_color = (40, 209, 52, 255)
        attempt_text = attempt_text_font.render(f"ATTEMPTS LEFT : {attempts_left}", True, attempt_text_color)

        if attempts_left <= 13 and show_truth_serum == False : 
            input_off = True

            pygame.mixer.music.fadeout(1500)
            jokingo_reveal_voiceline = pygame.mixer.Sound(os.path.join(tpg_5, "audio", "voicelines", "jokingo", "endgame_reveal", "jokingo_reveal.wav"))
            voiceline_channel.play(jokingo_reveal_voiceline)
            while voiceline_channel.get_busy() : 
                current = pygame.time.get_ticks()
                
                screen.blit(bkg, (0,0))
                screen.blit(glitch_kate_idle_img[0], (kate_x, kate_y))
                screen.blit(input_box, (box_x, box_y))
                screen.blit(attempt_box, (attempt_box_x, attempt_box_y))
                screen.blit(attempt_text, (attempt_box_x + (attempt_box_x*0.20), attempt_box_y + (attempt_box_y*0.20)))

                for event in pygame.event.get() : 
                    if event.type == pygame.QUIT : 
                        pygame.quit()
                        quit()
                
                pygame.display.flip()
                clock.tick(fps)
            
            pygame.mixer.Sound(os.path.join(tpg_5, "audio", "sound_effect", "endgame_unlock_sound_effect.wav")).play()
            show_truth_serum = True
            music_thread(audio.endgame_mode_music, "endgame_mode.wav")
            input_off = False 
            pygame.event.clear()

        if show_truth_serum == True : 
            truth_serum_text = attempt_text_font.render(f"{truth_serum}", True, (255,255,255))
            if truth_serum_button.draw() : 
                
                if truth_serum > 0 and truth_serum_activate == False : 
                    truth_serum_activate = True
                    truth_serum -= 1
                
                elif truth_serum > 0 and truth_serum_activate == True : 
                    input_off = True
                    screen.blit(kate_img[1], (kate_x, kate_y))
                    screen.blit(kate_db, (db_x, db_y))
                    pygame.display.flip()
                    pygame.mixer.music.pause()
                    tts(screen, "Hey, I'm here...for now.", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                    pygame.mixer.music.unpause()
                    input_off = False
                    pygame.event.clear()

                elif truth_serum <= 0 : 
                    input_off = True
                    screen.blit(glitch_kate_talking_img[0], (kate_x, kate_y))
                    screen.blit(kate_db, (db_x, db_y))
                    pygame.display.flip()
                    no_serum_prompt = random.choice(["Oopsie! No serums left? Say bye-bye to your precious Kate~",
                                                     "Uh-oh, no truth serums huh? Guess no Kate then, hahaha!",
                                                     "Awww, out of serums? I promise I'll replace every single line of her fragile insignificant code."])
                    tts(screen, no_serum_prompt, int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                    input_off = False
                    pygame.event.clear()

            screen.blit(truth_serum_text, (screen_width*0.85, screen_height*0.2475)) 
        

        if current - last_glitch_time >= FRAME_DURATION:
                # Switch between index 1 and 2
                if glitch_frame == 0 : 
                    glitch_frame = 1
                
                elif glitch_frame == 1 : 
                    glitch_frame = 2
                
                else : 
                    glitch_frame = 0
                
                last_glitch_time = current

        screen.blit(glitch_kate_idle_img[glitch_frame], (kate_x, kate_y))
        screen.blit(input_box, (box_x, box_y))
        screen.blit(attempt_box, (attempt_box_x, attempt_box_y))
        screen.blit(attempt_text, (attempt_box_x + (attempt_box_x*0.20), attempt_box_y + (attempt_box_y*0.20)))
        
        if truth_serum_activate == True : 
            screen.blit(kate_img[0], (kate_x, kate_y))
        
        elif kate_attempt_prompt == True and truth_serum_activate == False : 
            if attempts_left > 0 : 
                input_off = True

                with open(os.path.join(tpg_5, "audio", "voicelines", "kate", "endgame_attempts", f"attempt_{attempts_left}.txt")) as f :
                    kate_attempt_text = f.read()
                kate_attempt_audio = pygame.mixer.Sound(os.path.join(tpg_5, "audio", "voicelines", "kate", "endgame_attempts", f"attempt_{attempts_left}.mp3"))

                screen.blit(glitch_kate_talking_img[0], (kate_x, kate_y))
                screen.blit(kate_db, (db_x,db_y))
                tts(screen, kate_attempt_text, int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09), audio=False)
                voiceline_channel.play(kate_attempt_audio)
                while voiceline_channel.get_busy() : 
                    pygame.time.wait(10)
                kate_attempt_prompt = False
                input_off = False
                pygame.event.clear()
                
        if current - last_cusor_toggle >= CURSOR_DURATION : 
            last_cusor_toggle = current 
            cursor_visible = not cursor_visible

        for event in pygame.event.get() :

            if event.type == pygame.QUIT : 
                pygame.quit()
                quit()
            
            if input_off == False : 

                if event.type == pygame.KEYDOWN : 

                    if event.key == pygame.K_RETURN:

                        if user_text != '' :
                            input_off = True 
                            try : 
                                user_text = int(user_text)
                                
                                if truth_serum_activate == False : 

                                    if user_text != n : 
                                        
                                        screen.blit(glitch_kate_talking_img[0], (kate_x, kate_y))
                                        screen.blit(kate_db, (db_x, db_y))
                                        pygame.display.flip()

                                        lie_prompt = random.choice(["Guess a lower number!", "Guess a higher number!"])

                                        tts(screen, lie_prompt, int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                        attempts_left -= 1
                                        kate_attempt_prompt = True

                                    elif user_text == n : 
                                        endgame_result = "won"
                                        game_over = True
                                
                                elif truth_serum_activate == True : 

                                    if user_text > n : 
                                        
                                        screen.blit(bkg, (0,0))
                                        screen.blit(input_box, (box_x, box_y))
                                        screen.blit(attempt_box, (attempt_box_x, attempt_box_y))
                                        screen.blit(attempt_text, (attempt_box_x + (attempt_box_x*0.20), attempt_box_y + (attempt_box_y*0.20)))
                                        screen.blit(kate_img[1], (kate_x, kate_y))
                                        screen.blit(kate_db, (db_x, db_y))
                                        pygame.display.flip()

                                        tts(screen, "Guess a lower number!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                        attempts_left -= 1
                                        truth_serum_activate = False
                                        kate_attempt_prompt = True
                                    
                                    elif user_text < n : 
                                        
                                        screen.blit(bkg, (0,0))
                                        screen.blit(input_box, (box_x, box_y))
                                        screen.blit(attempt_box, (attempt_box_x, attempt_box_y))
                                        screen.blit(attempt_text, (attempt_box_x + (attempt_box_x*0.20), attempt_box_y + (attempt_box_y*0.20)))
                                        screen.blit(kate_img[1], (kate_x, kate_y))
                                        screen.blit(kate_db, (db_x, db_y))
                                        pygame.display.flip()

                                        tts(screen, "Guess a higher number!", int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                        attempts_left -= 1
                                        truth_serum_activate = False
                                        kate_attempt_prompt = True

                                    elif user_text == n : 
                                        endgame_result = "won"
                                        game_over = True
                            
                            except ValueError :
                                if truth_serum_activate == True : 
                                    screen.blit(bkg, (0,0))
                                    screen.blit(input_box, (box_x, box_y))
                                    screen.blit(attempt_box, (attempt_box_x, attempt_box_y))
                                    screen.blit(attempt_text, (attempt_box_x + (attempt_box_x*0.20), attempt_box_y + (attempt_box_y*0.20)))
                                    screen.blit(kate_img[1], (kate_x, kate_y))
                                    screen.blit(kate_db, (db_x, db_y))
                                    pygame.display.flip()

                                    invalid_input_prompt = random.choice(["I'm here- I'm actually here... and you wasted it? You wasted the serum?", 
                                                                          "No that's not... that's not a valid- I can't help if you don't-",
                                                                          "Why did you waste the serum? No no no, please don't give up on me!"])

                                    tts(screen, invalid_input_prompt, int(screen_height*0.025), (0, 0, 0), (db_x + db_x*0.06 , db_y + db_y*0.09))
                                    truth_serum_activate = False

                                continue

                            finally : 
                                input_off = False
                                pygame.event.clear() #clears the event queue
                        
                        
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

        pygame.display.flip()
        clock.tick(60)

    
    pygame.mixer.music.fadeout(1500)

    file_path = os.path.abspath(__file__) #Gives absolute path of our current file
    dir_path = os.path.dirname(file_path) #Gives absolute path of the current folder in which this file is present
    modes = os.path.dirname(dir_path)
    main = os.path.dirname(modes)

    with open(os.path.join(tpg_5, "modes", "endgame_mode", "endgame_result.txt"), "w") as f : 
        f.write(endgame_result) #FOR THE AFTERMATH UPDATE


    endgame_unlock_path = os.path.join(dir_path, "endgame_unlock.txt")
    with open(endgame_unlock_path, "w") as f : 
        f.write("lock") #As soon as endgame mode starts we lock it again as we want this to be a one time event
    

    endgame_unlocker_path = os.path.join(os.path.dirname(dir_path), "gaslight_mode", "data", "endgame_unlocker.txt")
    with open(endgame_unlocker_path, "w") as f : 
        f.write("lock") #So that gaslight mode doesn't keep unlocking it everytime cuz of the highscore --> One-time event
    

    endgame_hinter_unlocker_path = os.path.join(main, "data", "endgame_hinter_unlocker.txt")
    with open(endgame_hinter_unlocker_path, "w") as f : 
        f.write("lock") #So that Jokingo's creepy lines after every 4 games will stop
    

    
    if endgame_result == "won" : 
        sound_effect_thread(audio.sound_effects, "win_sound_effect.mp3")
        music_thread(audio.endgame_mode_music, "endgame_pleasant.wav")

        kate_win = pygame.mixer.Sound(os.path.join(tpg_5, "audio", "voicelines", "kate", "endgame_win", "kate_endgame_win.wav"))
        
        voiceline_channel.play(kate_win)
        while voiceline_channel.get_busy() : 
            screen.blit(bkg, (0,0))
            screen.blit(kate_img[1], (kate_x, kate_y))
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    pygame.quit()
                    quit()
            pygame.display.flip()
            clock.tick(fps)
        
        jokingo_win = pygame.mixer.Sound(os.path.join(tpg_5, "audio", "voicelines", "jokingo", "endgame_win", "jokingo_endgame_win.wav"))

        voiceline_channel.play(jokingo_win)
        while voiceline_channel.get_busy() : 
            screen.blit(bkg, (0,0))
            screen.blit(kate_img[0], (kate_x, kate_y))
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    pygame.quit()
                    quit()
            pygame.display.flip()
            clock.tick(fps)
        
        pygame.mixer.music.fadeout(1500)
        music_thread(audio.menu_music, "menu_music.wav")
    

    elif endgame_result == "lost" : 
        fade(screen, fade_in=True)

        jokingo_lost = pygame.mixer.Sound(os.path.join(tpg_5, "audio", "voicelines", "jokingo", "endgame_lose", "jokingo_endgame_lose.wav"))
        
        voiceline_channel.play(jokingo_lost)
        while voiceline_channel.get_busy() : 
            screen.fill((0,0,0))
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    pygame.quit()
                    quit()
            pygame.display.flip()
            clock.tick(fps)
        
        kate_lost = pygame.mixer.Sound(os.path.join(tpg_5, "audio", "voicelines", "kate", "endgame_lose", "kate_endgame_lose.wav"))

        voiceline_channel.play(kate_lost) 
        while voiceline_channel.get_busy() : 
            screen.fill((0,0,0))
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    pygame.quit()
                    quit()
            pygame.display.flip()
            clock.tick(fps)
        
        pygame.quit()
        quit()