import pickle

x = [1,3,1001,5,'a', [7]]

f = open("data.pkl", "wb") #using wb mode write in binary
pickle.dump(x,f)
f.close()


f = open("data.pkl", "rb")
saved_object = pickle.load(f)
f.close()

print(saved_object)

# Useful for big lists => no string conversion needed
# Compression

"""
If you are writing data to a file and you want other
programs/people to be able to open the file and read it,
then write directly to the file using open/write/close.
• Everything you write to the file must be string type.
• If you are writing data to a file that only your program
will use, then use Pickle. Note that only Python will be
able to read/write to the file. You will not be able to open it
by regular means (from the Finder, Explorer, etc.)
• You can write any single Python object (e.g. a single list) to the file.

"""