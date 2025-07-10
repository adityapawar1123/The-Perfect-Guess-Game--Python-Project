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
    "The game calls to you... will you answer?",
    "The story isn't over yet. Continue?",
    "Destiny isn't done with you. Play again?"]
    return random.choice(rematch_prompts)

def custom_no_range_roasts(n1, n2) : 
    no_range_roasts = [
    "What's next? Guessing between Monday and Monday?",
    "Wow. So intense. So mysterious. So...one possibility.",
    "I'm not mad. I'm just disappointed. Okay no wait-I'm mad AND disappointed.",
    "Wow no range but I bet you still had to think before guessing.",
    "Wow a range of...ONE? Well atleast that's still higher than your IQ.",
    "Custom range? More like custom shame.",
    f"What? You thought I'd get the confetti for guessing between {n1} and {n2}?",
    "The only mystery here is how you have the audacity to call this a game.",
    "Next time just write the number on your forehead and clap for yourself.",
    "You beat the odds- oh wait, there weren't any. My bad I guess."] 
    return random.choice(no_range_roasts)

def custom_low_range_win(n1, n2) : 
    low_range_win = [
    "Meh the range was so low, anybody could do that.",
    "What? You thought I'm gonna fangirl over such low range?",
    "Don't tell me you're proud of yourself with range like that.",
    "I'm not even impressed, that range was more tiny than your brain.",
    "Your IQ is so low that I bet you're proud of yourself even with that range.",
    "Wow, you guessed it... in a baby-sized range. Should I call the press?",
    "Nice guess. Now do it with a real range, champ.",
    "The range was so low. And yet you're grinning like it was Dark Souls.",
    f"You flexin' on a {n1} to {n2} range like it's a speedrun? Sit down junior."
    ]
    return random.choice(low_range_win)

def custom_low_range_lose(n1,n2) : 
    low_range_lose = [
    f"It was literally between {n1} and {n2}. And you still took your sweet time? Bruh.",
    f"Not even gonna sugarcoat it- how are you this slow in a {n1} to {n2} number range?",
    f"Guessing {n1} to {n2} should not take strategy. Yet... here we are.",
    "A toddler could've brute-forced this faster.",
    "Small range. Big shame.",
    "You made a baby-level range look like quantum physics.",
    "Bro missed in a range that could fit inside a sticky note. How."                                              
    ]
    return random.choice(low_range_lose)

def custom_reversed_range_roasts(n1, n2) : 
    reversed_range_roasts = [
        f"So you think {n1} to {n2} is a valid range? Bold of you to challenge basic math.",
        f"You entered {n1} to {n2}. What is this, reverse psychology?",
        f"Forget the game, you gotta go to elementary school first and learn ascending order.",
        "Putting the bigger number first? What are you, a time traveler?",
        f"From {n1} to {n2}? Are we counting backwards or just your brain cells?",
        f"At this point are you just rage-baiting me? Range {n1} to {n2}, seriously?",
        "Your range is backwards. Just like your sense of progress.",
        "Next time, try entering numbers in order. Like a functioning adult.",
        "This isn't a riddle. Just put the smaller number first, Einstein."
    ]
    return random.choice(reversed_range_roasts)