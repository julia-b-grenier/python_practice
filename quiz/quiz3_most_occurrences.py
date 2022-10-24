def most_occurrences(words, letter):
    
    s = words[0]
    
    for i in range(1, len(words)):
        if words[i].count(letter) > s.count(letter):
            s = words[i]
            
    if s.count(letter) == 0:
        return ""
    
    return s

#	w = ["big", "bubbly", "rabbit", "runs"]
