def is_palindrome(n): #G0
    """ (str) -> bool
    Returns true if the word is the same reversed

    >>> is_palindrome("racecar")
    True
    
    >>> is_palindrome("mom")
    True
    
    >>> is_palindrome("a nut for a jar of tuna")
    True
    
    >>> is_palindrome("apple")
    False
    """
    s = str(n) #A1
    i = 0 #D1
    while i < len(s): #B1
        if s[i] != s[-i-1]: #H2
            return False #C3
        i += 1 #I2
        
    return True #J1


def count_common_letters(word1, word2):
    """ (str, str) -> int
    Returns how many letters the two strings have in common (it is case-insensitive)
    
    >>> count_common_letters("banana", "cat")
    1
    >>> count_common_letters("Silent", "listen")
    6
    """
    common_letters = 0
    
    unique_letters = ""
    
    small_word = word1
    long_word = word2
    
    if (len(word1) > len(word2)):
        small_word = word2
        long_word = word1
        
    for char in small_word:
        if (char.lower() in long_word.lower() and char.lower() not in unique_letters):
            common_letters += 1
            unique_letters = unique_letters + char.lower()

    return common_letters


def average(numbers):
    ''' (str) -> int # style:
    Takes a string of digits as argument, and returns the average of the digits.
    If there are any non-integer elements in the list, return -1 instead.
    >>> average('48')
    6
    >>> average('abc33')
    -1
    '''
    if (not numbers.isdecimal() or len(numbers) == 0): # logical error missing part
        return -1
    
    summation = 0 # Name error => runtime error : avg == 0
    for i in range(len(numbers)):
        summation += int(numbers[i]) # logical error
        
    return int(summation / len(numbers))

if __name__ == '__main__':
    nums = input("Enter the digits: ")
    print(average(nums)) #syntax missing )
