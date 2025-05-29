import random

def invalid_input_roasts() : 
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
    return random.choice(invalid_input_roasts)

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