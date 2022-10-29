s = ""

letters = "abcd"

for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
                for letter4 in letters:
                    s = letter1 + letter2 + letter3 + letter4
                    if s.count(letter1) < 2 and s.count(letter2) < 2 and s.count(letter3) < 2 and s.count(letter4) < 2:
                        print(s)
                    s = ""                    
    