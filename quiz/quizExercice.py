"""

c = 10.5

print((type(c) == str) or (c >= 10))

"""


"""
import math

x = int(input())
y = int(input())

if math.sqrt(x) == math.sqrt(y)-1 :
    print((math.sqrt(y)+1)**2)
else:
    print("fail")
"""

time_24hrs = int(input("Enter the time: ")) #A0

hours = time_24hrs // 100 #C0
minutes = time_24hrs % 100 #C0

#K0
if minutes < 10: 
    min_str = "0" + str(minutes)
else:
    min_str = str(minutes)
#K0
    

am_pm = "am" #D0

if hours % 12 == 0: #J0
    if hours == 12: #H1
        am_pm = "pm" #E2
    hours = 12 #G1
    
elif hours % 12 != hours: #I0
    am_pm = "pm" #E1
    hours = hours % 12 #F1
    
#B0
time_12hrs = str(hours) + ":" + min_str + am_pm
print("The current time is: " + time_12hrs)
#B0

# A0 C0 K0 D0 J0 H1 E2 G1 I0 E1 F1 B0

"""

last question

x = float(input())
y = float(input())

print(str(x+y) + str(x) + str(y) + str(x+y))

"""