# Dictionaries keep track of associations for you

# elements/items = association of pair
    # elmt1 in pair = key		(immutable,unique in dict)
    # elmt2 in pair = value		(any type)
    

# dict (mapping type) maps key objects to value objects


# CREATING A DICT

an_empty_dictionary = dict()

another_empty_dictionary = {}

heights = {'Sasha' : 182, 'Rohan' : 168, 'Kate' : 177}


# ACCESSING A VALUE => Lookup
# With dictionaries, we can access a value stored in a dict through the key associated with it

heights = {"Julia": 145, "Olivia": 162, "Isa": 155}

print(heights["Julia"])


# ADDING ITEM

heights["Momo"] = "16 pouces"

print(heights)

# if the key already exist, its value is replaced

heights["Momo"] = 100

print(heights)


# REMOVING AN ITEM

del heights["Momo"]
print(heights)

# KeyError is raised whenever we try to access/delete an item using a key that does not exist.

my_dict = {'x' : 0, 'y' : 1, 'z' : 2}
#x = my_dict[0]
#print(x)


# USEFUL METHODS

# Returns the value in the dictionary d associated to the specified key. If the key is not in the dictionary it returns None. 
print(my_dict.get("x"))
print(my_dict.get(0))


# Removes the key-value pair contained in the dictionary d and returns the value. A KeyError is raised if key is not in d.
my_dict.pop("x")
print(my_dict)

# Returns a list-like object with the keys contained in the dictionary d. 
print(my_dict.keys())

# Returns the number of key-value pairs in the dictionary d.
print(len(my_dict))

# Creates a new dictionary with keys from iterable and values set to value.
# dict.fromkeys(iterable, value = None)
iterable_object = "Julia"
print(dict.fromkeys(iterable_object, None))
