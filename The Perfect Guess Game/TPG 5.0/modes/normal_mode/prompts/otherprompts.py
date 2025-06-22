import random 


def normal_mode_explain() : 
    normal_mode_explain = [
    "Rules are simple, I'll pick a number, and your job is to guess it. Let's see how fast you get it right!",
    "Rules are simple, I think of a number, and you try to guess what it is.",
    "Rules are simple, I've chosen a number. Can you figure out what it is, and how quickly?",
    "Rules are simple, guess the number I'm thinking of. That's it!",
    "Rules are simple, I pick a number, you guess. Let's see how many tries you need!",
    "Rules are simple, guess the number I've chosen. No tricks, just your brain versus my number.",
    "Rules are simple, I've got a number in mind. You have to guess it. How hard could it be?",
    "Rules are simple, it's a guessing game. I choose a number, and you try to find it!",
    "Rules are simple, I've locked in a number. Can you guess it before your guesses run out?",
    "Rules are simple, I picked a number. All you gotta do is guess it. Good luck!"
]
    return random.choice(normal_mode_explain)

def first_guess_prompts() : 
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
    return random.choice(first_guess_prompts)

def under4_guess_prompts() : 
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
    return random.choice(under4_guess_prompts)

def mid_guess_prompts() : 
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
    return random.choice(mid_guess_prompts)

