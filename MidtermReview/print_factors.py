def print_factors(number):
    if number == 0 or number == 1:
        return number
    factors = ""
    factor = 1
    while factor < number:
        if number % factor == 0:
            factors = factors + " " + str(factor) + ", "
        factor += 1
        
    factors = factors + " " + str(number) + "."
    
    print(factors)
    
def show_number(val1, val2, val3):
    if val1 >= 12 or val2 < 30:
        if val3 > 40 or val2 > val1 and val1 < val3:
            print("A ")
        else:
            if not (val2 > 8 or val3 == 24):
                print("B ")
            else:
                print("C ")
    else:
        print("D ")
def main():
 show_number(24, 11, 33)