
# We can pass as input to dict a list of tuples of length two to create a dictionary.
pairs = [("Montreal", 1.78), ("Rome", 2.87), ("Tokyo", 9.27)]
pair_dict = dict(pairs)
print(pair_dict)
#{'Montreal': 1.78, 'Rome': 2.87, 'Tokyo': 9.27}
print(pair_dict["Rome"])
#2.87


# Two ways to print a dictionary :
for term in pair_dict:
    print(term, pair_dict[term])
    
for city, num in pair_dict.items():
    print(city, num)
    

#If we want a copy of the items as a list of tuples, we can cast it to a list. 
d_items = pair_dict.items()
list_of_tuples = list(d_items)