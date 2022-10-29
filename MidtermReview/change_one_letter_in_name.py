import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
prompt = "Enter your name: "

name = input(prompt).lower()

rand_index = random.randint(0,len(name)-1)

char_to_replace = name[rand_index]


index_new_letter = alphabet.find(char_to_replace) + 1

if index_new_letter == 26:
    index_new_letter = 0
    
print("New name", name[:rand_index] + alphabet[index_new_letter] + name[rand_index+1:])