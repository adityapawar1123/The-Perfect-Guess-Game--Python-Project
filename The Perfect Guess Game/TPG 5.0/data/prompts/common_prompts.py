import random 

def intro_prompts() : 
    intro_prompts = [
    "\nWelcome to The Perfect Guess! Ready to test your luck and brainpower?",
    "\nYo, welcome! Think you can crack the code? Let's see if you got the skills!",
    "\nGuess the number… if you dare. Let's see if you're a true mastermind!",
    "\nWelcome challenger! Can you outsmart my number? Let's find out!",
    "\nAyy, glad you showed up! Let's see how fast you can crack this mystery number.",
    "\nThe game is simple. The challenge? Not so much. Think you can handle it?",
    "\nAlright let's do this, I've got a number in mind—can you guess it?",
    "\nYo genius! Time to prove yourself. Guess the number before I roast you.",
    "\nNew challenger detected! Only legends can guess my number. Are you one?",
    "\nReady set GUESS! The clock is ticking, let's see what you got."]
    return random.choice(intro_prompts)

def no_loop_roasts() :  
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
    return  random.choice(no_loop_roasts)

def rematch_prompts() : 
    rematch_prompts = [
    "You up for another game?",
    "Wanna run it back?",
    "Up for round two?",
    "Let's do this again, yeah?",
    "One more for the road?",
    "Fancy another go?",
    "Should we go again or nah?",
    "Rematch vibes?",
    "The grind never stops. You in?",
    "That XP ain't gonna earn itself. Another game?",
    "Queue up again?",
    "Another run for glory?",
    "Let's speedrun that rematch!",
    "You blinked. Wanna try with eyes open this time?",
    "That was cute. Wanna go for real now?",
    "One more? I promise I'll go easy, maybe",
    "The game calls to you… will you answer?",
    "The story isn't over yet. Continue?",
    "Destiny isn't done with you. Play again?"]
    return random.choice(rematch_prompts)
