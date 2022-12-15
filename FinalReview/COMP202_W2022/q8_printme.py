x = [1, 2, 3]
for i in range(len(x), 0, -1):
    try:
        print(1 / (x[i] - 2))
    except ZeroDivisionError:
        print("Bad math")
    except:
        print("Something went wrong")
    finally:
        print("PRINT ME!!")
