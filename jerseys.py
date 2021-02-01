from random import seed
from random import random
i = 0
overlap = 0
total_overlap = 0
numbers = []
j = 0
while j<100000:
    while i<26:
        a = round(random()*100)
        if a != 100:
            if a in numbers:
                numbers.remove(a)
                #print("Doop")
                #print(a)
                if a in numbers:
                    if overlap == 0:
                        total_overlap += 1
                    overlap = 1
                else:
                    numbers.append(a)
            numbers.append(a)
            i += 1
    #print(numbers)
    #print(overlap)
    numbers = []
    i = 0
    j+=1
    overlap = 0
    #print("")
    #print("")
print(total_overlap/j)
