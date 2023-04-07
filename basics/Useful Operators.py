### del    - to delete variable or object from memory
list2 = [10,20,30]
a = 29
del a
del list2


#### IN - return boolean from one sequence
list1 = [1,25,3,4] 
list2 = [10,20,30] 
x = 25 in list1 # checks presence or not. Return boolean.
print(list2, list1)

# TUPLE UNPACKING
coord = [(1,2),(3,4),(5,6),('a','b')]
len(coord) # 4

for a in coord:
    print(a)

for (a,b) in coord:
    print(a)
    print(b)

for a,b in coord:
    print(a)

#ZIP - PACKING LIST in TUPLES
list1 = [1,2,3,4] #ZIP according small size.
list2 = [10,20,30] # ZIP makes packing tuple pairs.
for a,b in zip(list1,list2):
    print(a,b)


# In dict, only iterate in keys, not values.
d = {'k1':100,'k2':200,'k3':500}

for n in d:
    print(n)
    
for n in d.values(): # values() or keys() 
    print(n)

for key,value in d.items(): #d.items() - pair
    print(key)
    print(value)



### range
import math 
for num in range(10): # Start=index 0, stop= not include 10, skip: 2    print(num)
    print(num)
for num in range(0,11,2): # Start=index 0, stop= 11 -1, skip: 2    print(num)
    print(num)
mylist = set(range(0,11,2)) # make a list
print(mylist)

#ENUMERATE
word = 'abcde' # Enumerate each letter to a number.
for index,letter in enumerate(word):
    print(f'index\t{index} - letter\t{letter}')


