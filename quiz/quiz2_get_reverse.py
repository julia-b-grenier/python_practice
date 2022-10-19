def get_reverse(n):
    m = 0
    
    while len(str(n)):
        m += int(str(n)[-1])*10**(len(str(n))-1)
        n = str(n)[0:-1]
        
    return m

print(get_reverse(452))