import random 

def timebound_mode_explain() : 
    timebound_mode_explain = [
        "The rules are simple, I choose a number and you have to guess it before the time runs out!",
        "Guess the number I picked... but be quick, the clock's ticking!",
        "It's a race against time — guess the number before the countdown hits zero!",
        "You vs. my secret number vs. the timer. Go!",
        "Pick a difficulty, set a timer, and let the chaos begin!",
        "You guess, the timer ticks, I laugh... let's go.",
        "Speed matters! Guess right before time explodes!",
        "Don't overthink it. Just guess. Fast.",
        "If you wait too long, you lose. Simple as that.",
        "Start guessing fast or lose, lol.",
        "Let's see how fast your brain really is... guess the number before the timer runs out!"
    ]
    return random.choice(timebound_mode_explain)

def win_prompts() : 
    win_prompts = [
        "Yeah yeah, you got it. Don't let it get to your head.",
        "Okay, you won. Relax, it's not the Olympics.",
        "Fine, you guessed it. Happy now?",
        "You beat the timer. Congrats, I guess.",
        "Alright genius, you got one right. Calm down.",
        "Ugh, I was kinda hoping you'd mess it up. Oh well.",
        "You won... but like, barely. Don't get cocky.",
        "Okay, Sherlock. You cracked the code. Whoop-dee-doo.",
        "Wow, a win. Should I throw you a parade or something?",
        "Hmph. Beginner's luck... probably.",
        "Guess that braincell pulled through just in time.",
        "Don't start acting like you're better than me now.",
        "Cool cool, you got it. Wanna medal?",
        "Yup, that's correct. But let's see you do it again.",
        "Okay, one win. You're still not special."
    ]

    return random.choice(win_prompts)

def lose_prompts() : 
    lose_prompts = [
    
    "Time's up! That brain lag really did you dirty, huh?",
    "You had one job... and the timer said nope.",
    "Guessing game? More like missing game.",
    "Tick tock, your guessing flopped.",
    "Oof. Timer roasted you harder than I ever could.",
    "You moved slower than Windows XP.",
    "Time ran out and so did your luck. Tragic.",
    "Bruh, the number was right there... in another timeline.",
    "You blinked and the timer said bye.",
    "Game over. And it wasn't even close.",
    "Well that was embarrassing. Wanna try not sucking next time?",
    "All that thinking and still no answer? Iconic.",
    "Timer: 0. You: -1. Brutal.",
    "You fumbled the bag... spectacularly.",
    "Honestly, I expected nothing and I'm still disappointed.",
    "Uh oh, time's up, grandma"
]

    return random.choice(lose_prompts)

def custom_timer_prompts() : 
    custom_timer_prompts = [
        "Tick tock, buddy. How long do you think you'll need?",
        "Set the timer. Or are you scared of the pressure already?",
        "Pick your poison: how fast do you wanna lose?",
        "Choose a time. The clock won't start itself, genius.",
        "You gotta pick a countdown, not just vibe in the void.",
        "C'mon now, pick a time limit. Or are you just here to waste mine?",
        "Want 10 seconds or 60? Either way, I hope you panic.",
        "No pressure... yet. Pick your timer and let the chaos begin.",
        "Your guess is against the clock. Choose wisely. Or don't. I like watching people fail.",
        "You're stalling. Set a timer before I do it for you.",
        "Wanna go easy on yourself or flex your 2 brain cells? Pick the countdown.",
        "Input a countdown like your dignity depends on it. Cuz it does."
    ]
    return random.choice(custom_timer_prompts)