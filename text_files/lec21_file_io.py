"""

open(filename, mode) is a built-in function.
It takes two arguments:
• filename: name of the file to read (if the file is in the
current directory) or full path to the file (if not).
• mode: 'r' for reading, 'w' for writing, amongst others
• It returns a file object we use to read from/write to the file

"""

filename = "file.txt"
fobj = open(filename, "r") # mode "r" for reading
file_content = fobj.read() # read whole file
print(file_content) # print the string


#Closing the file is important for several reasons (the OS may lock the file until it is closed; too many open files may cause your program/computer to slow down).
fobj.close()

"""
To write to a file in Python:
1. Open the file with open() using mode 'w' for "write."
If it does not exist, it will be created.
If it does exist, it will be deleted and replaced with an empty file.
2. Call write(s) method on the file object
to write the string s into the file.
3. Close the file

"""

filename = "quotes.txt"
fobj = open(filename, "w") # mode "w" for writing => delete content
fobj.write("My first line in a file!!") # write line to file also returns the number of character written (counts \\n as one)
fobj.write("This will appear on the second line(?)")

# read line by line

fobj = open(filename, "r")
for line in fobj: # file object is iterable
    print(line)
fobj.close()

# appending to a file => does not erase the file

filename = "quotes.txt" # assume it exists from last slide
fobj = open(filename, "a") # mode "a" for appending
fobj.write("\nA third line!! Will the madness ever stop?")
fobj.close()

# We can also add a + after the mode to indicate both reading and writing (e.g., "r+")

"""

r opens for reading only
w opens for writing only. Overwrites the file if it exists. Creates the file if it does not exist.
x opens for writing only. Creates the file if it does not exist. If it already exists, raises FileExistsError.
a opens for writing only. Creates the file if it does not exist. If it already exists, appends to the end of the file.

"""