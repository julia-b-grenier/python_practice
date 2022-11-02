def deep_copy(x):
    y = []
    for e in x:
        new_e = []
        for n in e:
            new_e.append(n)
        y.append(new_e)
    return y
        
    
a = [[1,2],[3,4],[5]]

b = deep_copy(a)

print(b)