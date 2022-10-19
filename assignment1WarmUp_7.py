def fruitful(x,y,z):
    if (z == 3 or z == x + y):
        return True
    return False

print(fruitful(int(input("x: ")), int(input("y: ")), int(input("z: "))))