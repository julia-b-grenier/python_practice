def mystery1(x):
    for i in range(x):
        print(x)
        
def mystery2(x):
    i = 1
    for x in range(i):
        mystery1(i)
        
y = int(input("y: "))
mystery1(y)
mystery2(y)