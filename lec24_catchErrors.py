
while True:
    s = input("Enter a number: ")
    try:
        number = int(s)
        break
    except ValueError:
        print("Invalid input!")
    except (IndexError, ZeroDivision):
        print("Example")
    except: # Catch all, but its better to have a precise
        print("Other errors")
    # finally block will always execute even if there is a break statement or error
    # for example close the file opened
    finally:
        print("This will always be printed.")
        
print("Valid number entered: " + str(number))