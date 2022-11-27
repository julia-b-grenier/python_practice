
f = open("animals.txt", 'r')

for x in f:
    print(x.strip().split(','))