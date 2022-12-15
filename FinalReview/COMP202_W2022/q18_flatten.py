import copy

def flatten(d):
    initial_d = copy.deepcopy(d)
    
    
    for i in initial_d.keys():
        del d[i]
        for k,v in initial_d[i].items():
            if k in d.keys():
                d[k] += v
            else:
                d[k] = v
                
                
a = {'Min': { 'a' : [1, 3], 'b' : [3, 6], 'c' : [6, 7, 8]}, 'Max': { 'a' : [7, 9], 'b' : [5, 3, 2], 'd' : [0, 1, 0]}}

print(a)

flatten(a)

print(a)