
def is_prime(n):
    if n<=2:
        return False
    
    prime = True
    
    
    for multiple in range (2, n):
        if n % multiple == 0:
            prime = False
            
            
    return prime


is_prime(5)