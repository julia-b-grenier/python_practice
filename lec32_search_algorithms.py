# Search algoritgms

def linear_search(sequence, item_to_search):
    for i, item in enumerate(sequence):
        if item == item_to_search:
            return i
        
    return None


import time, random
lst = random.sample(range(10**9), k=10**7)

time_start = time.time()
index_found = linear_search(lst, -1)
time_end = time.time()
delta_time = time_end - time_start
print("The linear search took", delta_time, "seconds.")