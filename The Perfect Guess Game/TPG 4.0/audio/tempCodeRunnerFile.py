def script() :
    for i in range(1, 22) : 
        path = os.path.join("voicelines", "jokingo", "endgame_hints", f"line_{i}.txt")
        with open(path, "w") as f : 
            for line in voicelines : 
                f.write(line)
