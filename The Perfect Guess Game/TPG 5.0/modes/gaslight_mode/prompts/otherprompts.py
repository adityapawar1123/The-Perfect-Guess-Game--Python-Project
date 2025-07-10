import random 


def gaslight_mode_explain() : 
    gaslight_mode_explain = [
    "The rules are simple. I pick a number, you guess, and I lie twice. You won't know when.",
    "This is gaslight mode. I'll mislead you, deceive you, and pretend I didn't. Classic behavior.",
    "I choose a number, you try to guess it, and I mess with your mind a little. Or a lot.",
    "You'll guess numbers and I'll guide you, except two times I won't. You'll never know which ones.",
    "Welcome to gaslight mode. I lie just enough to make you question every decision.",
    "Gaslight mode is basically trust issues the game. Good luck trusting my hints.",
    "I'll lie twice. Or maybe I already did. Are you sure this is real?",
    "You're in gaslight mode now. Nothing I say can be trusted. That's the fun part.",
    "Two lies, endless confusion, and me pretending I'm helping you. Let's go.",
    "Think you're good at guessing? Let's see how you do when I'm lying to you.",
    "Gaslight mode is where logic dies and the manipulation begins. Enjoy.",
    "I pick a number, you guess it, and I gaslight you along the way. Let's begin."    
]
    return random.choice(gaslight_mode_explain)

def first_guess_prompts() : 
    first_guess_prompts = [
    "Impossible... You must've cheated. I never said the answer was that.",
    "You got it in one? There's no way. I might have made a mistake.",
    "Well, congratulations... I guess? But that answer *definitely* wasn't right at first.",
    "Wait... was that really the right number? I'm second-guessing myself now.",
    "Huh, did you just guess? It couldn't have been that easy...",
    "Are you sure you guessed it? I could've sworn I said something else.",
    "Oh, you *think* you got it? Well, I might have changed the number halfway.",
    "First try, huh? Suspicious... Did you peek at the answer?",
    "Well, *technically* you guessed it, but I could've sworn I gave you a harder challenge.",
    "You know, that number seems a little too obvious. Are you trying to mess with me?",
    "Whoa, you really nailed it. Now I'm not sure if I even set the right number...",
    "Okay, I see how it is... You're just making me look bad now.",
    "That's *way* too quick. Are you sure you didn't cheat?",
    "Did you *really* get it, or am I just messing with you? Can't trust anything right now."
    ]
    return random.choice(first_guess_prompts)

def under_5_guess_prompts(guessNo) : 
    under_5_guess_prompts = [
    "Okay, sure, you got it... but I swear I was *way* sneakier than that.",
    f"In {guessNo} guesses? You're just lucky, aren't you?",
    "How are you even doing this? You must be cheating or something.",
    "Wow, I guess I made it too easy for you, huh? Maybe next time I'll try harder.",
    "You got it that fast? Are you sure you're not a mind reader?",
    "Impressive, but I'm starting to think you just guessed it and got lucky.",
    "A little quick there, don't you think? Something smells fishy.",
    "You're really flexing now, but are you *sure* that was the right number?",
    "That was too fast... what's going on here, you got a secret?",
    f"Hmm, in {guessNo} guesses? Are you *sure* you didn't peek at my notes?",
    "Okay, fine, you got it... but I'm not convinced it wasn't just pure guesswork.",
    "Alright, I see how it is. You get it in a few guesses, now you're acting like a genius?"
    ]
    return random.choice(under_5_guess_prompts)

def mid_guess_prompts(guessNo) : 
    mid_guess_prompts = [
    "Oh, you finally guessed it? Well, I was *totally* messing with you this whole time.",
    "Hmm, you got it... but I definitely had you second-guessing yourself. Classic gaslighting.",
    f"Took you {guessNo} tries, huh? I had you doubting everything. My work here is done.",
    "Okay, okay, you got it. But honestly? I made you question everything before this. No easy feat.",
    f"Took you {guessNo} guesses? I had you guessing, didn't I? My gaslighting game is on point.",
    "You figured it out, but don't act like I didn't make you doubt yourself every step of the way.",
    "So, you guessed it. But don't forget how much I made you question your choices. Gaslighting 101.",
    "Congrats, you got it. But, uh, I made you doubt everything before that. Classic move, right?",
    "You figured it out eventually. But my gaslighting? 10/10. You were totally lost.",
    "Yeah, you got it, but let's be real, I had you rethinking every guess you made. Gaslight level: expert.",
    "You got it. Took a little while, though. Bet I had you questioning everything before that, huh?",
    "Alright, alright, you got it, but I made you second-guess every decision you made. That's the magic of gaslighting."
]
    return random.choice(mid_guess_prompts)

