import random 

def slow_guess_roasts() : 
    slow_guess_roasts = [
    "FINALLY! I was starting to think you'd never get it.",
    "Took you long enough! I almost fell asleep waiting for you to guess.",
    "Bro, were you trying every number one by one? Took you ages!",
    "You got there, eventually. I was about to send out a search party for your brain.",
    "That took longer than my last software update. But hey, at least you made it!",
    "Wow, that was painful to watch. But congrats, I guess?",
    "I was about to start dropping hints out of pity. But you got there, barely.",
    "Man, you really took the scenic route to get to that answer, huh?",
    "If guessing numbers was a marathon, you just finished in last place.",
    "You made it, but at what cost? Time? Dignity? Either way, GG I guess."]
    return random.choice(slow_guess_roasts)

def invalid_input_roasts() : 
    invalid_input_roasts = [
    "Bro, this is a number guessing game, not a spelling bee. Try again.",
    "What was that? Morse code? Ancient hieroglyphics? Enter a NUMBER.",
    "I said guess a number, not summon a demon. Try again, genius.",
    "Oh wow, an advanced strategy: guessing absolute nonsense. Revolutionary.",
    "Are you trying to hack the game? 'Cause all you're hacking is my patience.",
    "If this was a test for IQ, let's just say, you wouldn't pass.",
    "You had one job: enter a number. And somehow, you fumbled it.",
    "That wasn't even close to a number. Like, not even in the same galaxy.",
    "This ain't Mad Libs, buddy. Enter a legit number before I start charging you per mistake.",
    "You do understand what a number is, right?",
    "At this point, even my random number generator has more logic than you."]
    return random.choice(invalid_input_roasts)

def game_quit() :  
    game_quit = [
    "Aww, quitting already? Guess you were never really up for the challenge.",
    "No more guesses? Guess you couldn't handle the heat!",
    "You're bailing out? Weak, my friend. Weak.",
    "What's the matter, scared of losing? You were doing great, sorta.",
    "Quitting already? You had one job!",
    "Wow, really? Giving up just like that? I guess it's not for everyone.",
    "That's it? You're done? Guess I was too good for you.",
    "C'mon, you can't quit now! I was just starting to have fun roasting you.",
    "Giving up? Pfft, no guts, no glory.",
    "Alright, alright, you win... at quitting.",
    "I see how it is. You had your chance and bailed. Classic."]
    return  random.choice(game_quit)
