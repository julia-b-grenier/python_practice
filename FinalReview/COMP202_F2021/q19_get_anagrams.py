def get_anagrams(l, target_word):
    result = []
    for word in l:
        anagram = True
        for letter in word:
            if letter not in target_word:
                anagram = False
        
        if anagram:
            result.append(word)
            
    return result