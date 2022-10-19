def hello_by(number):
    """ int ->
    display "Hello everyone" is the number the user entered is 1, else print "Bye bye"
    
    """
    
    if number == 1:
        print("Hello everyone")
    else:
        print("Bye bye.")
        

#hello_by(int(input("enter a number: ")))
        
def hello(text):
    print("Hello " + text)

hello("Julia")