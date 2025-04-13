import random 
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

import os 

BASE_DIR = os.path.abspath(__file__)
# Turns a relative file path (like TPG 3.03_day22.py) into a full, 
# absolute path (like E:\Python programming\Mini Projects\Day 17 - The Perfect Guess Game\TPG 3.03_day22.py).

# __file__: A built-in variable that holds the filename of the current Python file.
# BASE_DIR is a variable, u can change it to anything u want

directory_path = os.path.dirname(BASE_DIR)
# os.path.abspath(__file__) gives you something like: "C:/Users/Pookie/Desktop/JokingoSR/main.py"
# os.path.dirname(...) strips the file name, giving you: "C:/Users/Pookie/Desktop/JokingoSR"

# We did this to find the folder your script is in, 
# so we can access stuff like highscore/normal_mode/... relative to that folder.

def tts(text) : 
   engine.say(text)
   print(text)
   engine.runAndWait()

def only_tts(text) :
   engine.say(text)
   engine.runAndWait() 


intro_prompts = [
    "Welcome to The Perfect Guess! Ready to test your luck and brainpower?",
    "Yo, welcome! Think you can crack the code? Let's see if you got the skills!",
    "Guess the number… if you dare. Let's see if you're a true mastermind!",
    "Welcome challenger! Can you outsmart my number? Let's find out!",
    "Ayy, glad you showed up! Let's see how fast you can crack this mystery number.",
    "The game is simple. The challenge? Not so much. Think you can handle it?",
    "Alright let's do this, I've got a number in mind—can you guess it?",
    "Yo genius! Time to prove yourself. Guess the number before I roast you.",
    "New challenger detected! Only legends can guess my number. Are you one?",
    "Ready set GUESS! The clock is ticking, let's see what you got."]
tts(random.choice(intro_prompts))


tts("\nThe rules are simple. I choose a number and you guess it. \nLet's see how many attempts you need before you guess the right number.")

while True :
 
 no_loop_roasts = [
    "Aww, quitting already? Guess you were never really up for the challenge.",
    "No more guesses? Guess you couldn't handle the heat!",
    "You're bailing out? Weak, my friend. Weak.",
    "What's the matter, scared of losing? You were doing great... sorta.",
    "Quitting already? You had one job!",
    "Wow, really? Giving up just like that? I guess it's not for everyone.",
    "That's it? You're done? Guess I was too good for you.",
    "C'mon, you can't quit now! I was just starting to have fun roasting you.",
    "Giving up? Pfft, no guts, no glory.",
    "Alright, alright, you win... at quitting.",
    "I see how it is... You had your chance and bailed. Classic."]
 no_loop_roasts_random = random.choice(no_loop_roasts)

 first_guess_prompts = [
    "Wait, WHAT? First guess?! You're a straight-up mind reader!",
    "First try? Are you secretly a wizard or something?",
    "You guessed it on the first try? That's not luck, that's talent!",
    "One guess? I'm convinced you're using some kind of game hack!",
    "You've got the eyes of an eagle and the brain of a genius! First guess?!",
    "First guess? Whoa, you're on fire! Keep that up and I'm quitting the game.",
    "I think we've got a future champion here! One guess, no sweat.",
    "Did you just guess it first try? Are you secretly my creator or something?",
    "Okay, now you're just showing off! One guess? That's pure skill right there.",
    "First guess?! That's legendary status right there. Are you for real?"]
 first_guess_prompts_random = random.choice(first_guess_prompts)


 under4_guess_prompts = [
    "Wow, you cracked it fast! Did you hack the game or are you just that good?",
    "Speedy! You guessed it in under 4 tries. Are you sure you're not a psychic?",
    "You're a natural! Guessing that fast is no easy feat!",
    "Did you just predict the future? That was lightning speed!",
    "Impressive! Under 4 guesses? You must have a secret superpower.",
    "Whoa! That was fast. You might just be a number-guessing champion!",
    "Alright, alright, I see you! 4 guesses or less, you're on fire!",
    "How did you do that? You guessed it faster than a cheetah on a caffeine rush!",
    "Under 4 guesses? That's some next-level genius stuff right there.",
    "Okay, I'm impressed. You crushed that in record time. Can you teach me your ways?"]
 under4_guess_prompts_random = random.choice(under4_guess_prompts)

 mid_guess_prompts = [
    "Not bad, not bad! Took you a few tries, but you got there in the end!",
    "Solid effort! You didn't take too long, but you definitely worked for it.",
    "A respectable performance! Took some thinking, but you cracked the code.",
    "Okay, okay, not the fastest, but you still made it! That's what counts!",
    "Not too shabby! A few stumbles, but hey, you got the number in the end!",
    "You took your time, but the win is yours! That's what matters.",
    "A little back and forth, but you found the right path. Well played!",
    "You were circling around the answer for a while, but you got there!",
    "You played it safe, took your shots, and boom—victory is yours!",
    "Decent job! Took a few extra tries, but hey, a win's a win!"]
 mid_guess_prompts_random = random.choice(mid_guess_prompts)

 slow_guess_roasts = [
    "FINALLY! I was starting to think you'd never get it.",
    "Took you long enough! I almost fell asleep waiting for you to guess.",
    "Bro, were you trying every number one by one? Took you ages!",
    "You got there… eventually. I was about to send out a search party for your brain.",
    "That took longer than my last software update. But hey, at least you made it!",
    "Wow, that was painful to watch. But congrats, I guess?",
    "I was about to start dropping hints out of pity. But you got there… barely.",
    "Man, you really took the scenic route to get to that answer, huh?",
    "If guessing numbers was a marathon, you just finished in last place.",
    "You made it, but at what cost? Time? Dignity? Either way, GG I guess."]
 slow_guess_roasts_random = random.choice(slow_guess_roasts)

 invalid_input_roasts = [
    "Bro, this is a number guessing game, not a spelling bee. Try again.",
    "What was that? Morse code? Ancient hieroglyphics? Enter a NUMBER.",
    "I said guess a number, not summon a demon. Try again, genius.",
    "Oh wow, an advanced strategy: guessing absolute nonsense. Revolutionary.",
    "Are you trying to hack the game? 'Cause all you're hacking is my patience.",
    "If this was a test for IQ, let's just say... you wouldn't pass.",
    "You had one job: enter a number. And somehow, you fumbled it.",
    "That wasn't even close to a number. Like, not even in the same galaxy.",
    "This ain't Mad Libs, buddy. Enter a legit number before I start charging you per mistake.",
    "At this point, even my random number generator has more logic than you."]
 invalid_input_roasts_random = random.choice(invalid_input_roasts)

 
 tts("\nChoose the difficulty")

 print("Easy : Guess between 1 and 100\nMedium : Guess between 1 and 500\nHard : Guess between 1 and 1000")
 difficulty = input("Enter(e/m/h) : ")

 guessNo= 0

 def normal_mode_highscore() : 
     global guessNo
     global difficulty 
     #This tells python that we directly wanna change the global variable named difficulty 
     #and we're not creating a functn variable, this is wht global functn does

     # os.path.join Safely combines folder names and file names into a complete path. 
     # No need to worry about slashes (/, \), it works across all OS (windows/linux/mac).
     
     if difficulty in ["e", "ez", "easy"] : 
         difficulty = "easy"
     
     elif difficulty in ["mid", "m", "medium", "normal"] : 
         difficulty = "medium"

     elif difficulty in ["h", "hard", "difficult", "diff", "dif"] : 
         difficulty = "hard"

     normal_mode_highscore_path = os.path.join(directory_path, "highscore", "normal_mode", f"{difficulty}_highscore.txt")
     
     with open(normal_mode_highscore_path) as f : 
         highscore = f.read().strip()

         if highscore!="" : 
             highscore = int(highscore)
         else :
             highscore = 100
      
         if guessNo>highscore : 
             print(f"Highscore guess number : {highscore}")
         else : 
            with open(normal_mode_highscore_path, "w") as f1 :
                f1.write(str(guessNo))
                tts("\nNew highscore unlocked!")
                print(f"Highscore guess number : {guessNo}")


 def game_win_prompts(n) :
    global guessNo
    if guessNo==1 : 
        print(f"\nYou won! The answer is {n}\nNumber of guesses = {guessNo}")
        only_tts(first_guess_prompts_random)

    elif 2 <= guessNo < 4 :
        print(f"\nYou won! The answer is {n}\nNumber of guesses = {guessNo}")
        only_tts(under4_guess_prompts_random)  

    elif 4 <= guessNo <= 6 :
        print(f"\nYou won! The answer is {n}\nNumber of guesses = {guessNo}")
        only_tts(mid_guess_prompts_random)  

    else : 
        print(f"\nYou won! The answer is {n}\nNumber of guesses = {guessNo}")
        only_tts(slow_guess_roasts_random)  

 def normal_mode_game(diffNo) : 
     global easyNo
     global mediumNo
     global hardNo
     global guessNo

     if diffNo in ["e"] : 
         diffNo = easyNo
     elif diffNo in ["m"] : 
         diffNo = mediumNo
     elif diffNo in ["h"] : 
         diffNo = hardNo
     
     while True : 
        n1 = input("Guess the number : ")

        if n1.isdigit() == True : 
            n = int(n1)
            if  diffNo==n : 
                guessNo += 1
                game_win_prompts(n)
                normal_mode_highscore()
                break     
                    
            elif n<diffNo : 
                only_tts("Guess a higher number")
                print(f"\nWrong guess\nPick a higher number than {n}")
                guessNo+=1

            elif n>diffNo : 
                only_tts("Guess a lower number")
                print(f"\nWrong guess\nPick a lower number than {n}")
                guessNo+=1

        else : 
            only_tts(invalid_input_roasts_random)
            print("\nEnter an integer DUMBASS")
     

 if difficulty.lower().strip() in ["e", "easy", "ez"] : 
    easyNo = random.randint(1, 100)
    
    tts("You have to guess a number between 1 and 100")
    normal_mode_game("e")

    loop_question = input(("\nWanna play one more game?(yes/no) : "))

    if loop_question.lower().strip() not in ["yes", "y"] : 
        tts(no_loop_roasts_random)
        print("\nHope you enjoyed! Re-run the programme to play again")
        break
 
 
 elif difficulty.lower().strip() in ["mid", "m", "medium", "normal"] :
    mediumNo = random.randint(1, 500)

    tts("You have to guess a number between 1 and 500")
    normal_mode_game("m")

    loop_question = input(("\nWanna play one more game?(yes/no) : "))

    if loop_question.lower().strip() not in ["yes", "y"] : 
        tts(no_loop_roasts_random)
        print("\nHope you enjoyed! Re-run the programme to play again")
        break

 elif difficulty.lower().strip() in ["h", "hard", "difficult", "diff", "dif"] : 
     hardNo = random.randint(1, 1000)
     
     tts("You have to guess a number between 1 and 1000")
     normal_mode_game("h")

     loop_question = input(("\nWanna play one more game?(yes/no) : "))

     if loop_question.lower().strip() not in ["yes", "y"] : 
        tts(no_loop_roasts_random)
        print("\nHope you enjoyed! Re-run the programme to play again")
        break
 else : 
     tts("\nInvalid difficulty level! Choose again")

