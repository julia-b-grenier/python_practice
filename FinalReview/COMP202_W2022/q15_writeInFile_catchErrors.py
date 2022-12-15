try:
    f = open("hello.txt", 'a')
    
except:
    print("couldn't open the file")
    
else:
    try:
        f.write("Sun")
    except:
        print("Couldn't write in the file")
        
    finally:
        f.close()