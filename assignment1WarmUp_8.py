def fruitful(x,y,op):
    if (op == "+"):
        return x + y
    elif op == "*":
        return x * y
    else:
        return 0
    
print(fruitful(int(input()), int(input()), input()))