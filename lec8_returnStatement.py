
def same_parity(num1, num2):
    return num1 % 2 == num2 % 2
    
    
def side_of_street():
    house_num1 = int(input("Enter first street address: "))
    house_num2 = int(input("Enter second street address: "))
    
    if same_parity(house_num1, house_num2):
        print("Houses on the same side of the street.")
    else:
        print("Houses on different side of street.")
        

side_of_street()
    