import random 

def slow_guess_roasts(guessNo) : 
    slow_guess_roasts = [
    f"Took you over {guessNo} guesses? Babe, I *lived* in your brain rent free.",
    "I had you dancing like a puppet. That was delicious.",
    f"{guessNo} guesses? Nah, you weren't playing the game... *I* was playing you.",
    "By guess number three, you were already lost. By number eight, you were mine.",
    "You trusted me? That's on you. I gaslit you so good, even *I* forgot the number.",
    "You guessed it… eventually. But let's be real — I owned your thought process the whole time.",
    "You finally got it? Congrats, but I just psychologically finessed the hell outta you.",
    f"More than {guessNo} guesses? I straight-up rewired your brain. That's talent.",
    "You were so off, I had to stop gaslighting just to let you *catch up*.",
    "You really let me gaslight you for that long? I deserve an Oscar for that performance.",
    "Your brain? Hijacked. Your logic? Twisted. Me? Thriving.",
    "Not you falling for every bait I threw. This wasn't a guessing game, it was a *mind maze* and you flopped."
]
    return random.choice(slow_guess_roasts)

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
