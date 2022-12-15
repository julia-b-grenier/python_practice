def initialisms(phrases, initial):
    result = []
    
    for i in range(len(phrases)):
        words = phrases[i].split()
        first_letters = []
        for word in words:
            first_letters.append(word[0])
        
        if "".join(first_letters) == initial:
            result.append(i)
    
    return result