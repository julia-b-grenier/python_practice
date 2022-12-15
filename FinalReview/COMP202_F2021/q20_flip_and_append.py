def flip_and_append(fname):
    f = open(fname, 'r+')
    
    content = f.read().strip().split('\n')
    
    new_content = []
    for i, line in enumerate(content):
        line = line.split(',') # dont forget all lines are strings
        new_content.insert(0, line[::-1])
    
    for line in new_content:
        f.write("\n" + ','.join(line)) # Dont forget add a line
    
    f.close()