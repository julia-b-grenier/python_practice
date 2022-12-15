import math

def is_prime(n):
    if n <= 2:
        return False
    
    prime = True
    
    for multiple in range(2,n):
        if n % multiple == 0:
            prime = False
    
    return prime

def prime_factors(n):
    p_factors = []
    
    for i in range(2,n):
        if is_prime(i):
            p_factors.append(i)
            
    return p_factors

def radical(n):
    product = 1
    for factor in prime_factors(n):
        product *= factor
    return product

def quality(a,b,c):
    r = radical(a*b*c)
    
    return math.log10(c)/math.log10(r)

def get_highest_rated_triple(triples):
    
    highest_index = 0
    a, b, c = triples[0]
    highest_quality = quality(a,b,c)
    
    for i, triple in enumerate(triples):
        a, b, c = triple
        q = quality(a,b,c)
        if q > highest_quality:
            highest_index = i
            highest_quality = q
            
    return highest_index
    
    
triples = [(1, 2**3, 3**2),
            (5, 3**3, 2**5),
            (1, 3*2**4, 7**2),
            (1, 7*3**2, 2**6),
            (1, 5*2**4, 3**4),
            (2**5, 7**2, 3**4)]
    
