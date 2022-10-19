def average_odd_digits(s):
    total = 0
    
    num_odd = 0
    
    # looping by value
    for char in s:
        if int(char) % 2 == 1:
            total += int(char)
            num_odd += 1
        
    """
    # looping by index
    for i in range(len(s)):
        if int(s[i]) % 2 == 1:
            total += int(s[i])
            num_odd += 1
    """
    
    return total / num_odd


def print_greater_number(s):
    """ (s) -> NoneType
    Prints out all the characters in the string s that are greater than the character immediately following them.
    >>> print_greater_number('3819')
    8
    >>> print_greater_number('123')
    >>> print_greater_number('321')
    3
    2
    """
    
    for i in range(len(s)-1):
        if (s[i] > s[i+1]):
            print(s[i])

def is_prime(n):
    if n<2:
        return False
    
    prime = True
    
    for multiple in range (2, n):
        if n % multiple == 0:
            prime = False
            
    return prime

def first_n_primes(n):
    """ int -> list<int>
    Returns the first n prime numbers.
    >>> first_n_primes(1)
    [2]
    >>> first_n_primes(2)
    [2, 3]
    """
    prime_numbers = []
    i = 2
    while len(prime_numbers) < n:
        if is_prime(i):
            prime_numbers.append(i)
        i += 1
    
    return prime_numbers
    
    
    