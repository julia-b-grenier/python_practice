

input_dict = {'cat': 3, 'tiger': 5, 'lion': 4, 'hippo': 4}

output_dict = {}

for k, v in input_dict.items():
    print(k,v)
    
    if v in output_dict:
        output_dict[v] = output_dict[v]+[k]
    else:
        output_dict[v] = [k]
        
print(output_dict)
    