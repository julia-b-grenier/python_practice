
def increase_by_two(x):
    return x + 2


def apply_to_list(f, input_list):
    result = []
    
    for element in input_list:
        result.append(f(element))
    return result


old_list = [0,3,1,7]
my_list = apply_to_list(increase_by_two, old_list)

print(my_list)