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

def game_quit() :  
    game_quit = [
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
    "I see how it is... You had your chance and bailed. Classic.", 
    "Awwww you quitting already? Could've sworn you had some braincells left."]
    return  random.choice(game_quit)

def custom_lose_roasts(timer) : 
    custom_lose_roasts = [
        f"You picked the range, gave yourself {timer} seconds...and STILL lost? That's talent.",
        f"{timer} seconds. Your timer. Your rules. Your flop. Poetry, really.",
        f"{timer} seconds? Chosen by you. Failure? Also you.",
        f"{timer} seconds of self-confidence. Followed by a lifetime of roastable shame.",
        f"*Player selects {timer} seconds*. *Player loses*. Even netflix couldn't write better comedy.",
        f"{timer} seconds. From self-belief to self-defeat in one smooth move.",
        "Bro cooked up his own rules and still got served. How do you fumble *your* game?",
        "Imagine setting your own timer and STILL running out of time. Self-sabotage legend.",
        "I gave you the steering wheel and you drove straight into a wall.",
        "Self-made range, self-chosen time, self-destruction. Iconic.",
        "That was YOUR timer. YOUR range. And yet...you said 'nah'.",
        "You had one job. Actually, *you created* that job. And still failed it.",
        "You basically cheated by setting your own rules... and still got cooked.",
        "Custom mode, custom failure. You're built different- just not in a good way.",
        "Did you *try* to lose, or are you just naturally gifted at it?",
        "Bro set the microwave timer and still burned the popcorn.",
        "You were given creative freedom... and created a disaster.",
        "Picked your own challenge. Got challenged by your own pick. How poetic."
    ]
    return random.choice(custom_lose_roasts)