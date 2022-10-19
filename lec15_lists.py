
a = [1, 2]
b = [3, 4, 5]
c = a + b # [1, 2, 3, 4, 5]

a = [1, 2]
c = a * 3 # [1, 2, 1, 2, 1, 2]


# range : [-len(a), len(a) - 1]
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
print(days[::-1]) # get the reverse of the list


#instead of writting
#if x == 5 or x == 7 or x == 10 or x == 15:

x = 5
if x in [5,7,10,15]:
    print(x)


my_list = ["banana", 3.75, 5]
my_list[1:2] = ["cat", "dog", "ferret"]
print(my_list) # ['banana', 'cat', 'dog', 'ferret', 5]


a.append(x) # adds the element x to the end of the list a. Does not return a value.

a.insert(i, x) #adds the element x to the list a in position i.

a.remove(x) #removes the first occurrence of the element x in the list a. A ValueError is raised if there is no such element.