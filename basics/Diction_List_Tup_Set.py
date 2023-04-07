############################
# Dictionary  - Value Pair 
############################

#They do NOT have order ,so NOT to be Sorted..We can add tuple, list, dic inside
my_dict = {'pear':200,'apple':2.99,'stock':[127,280,0],'name':{'raphael':40000}} 

print(my_dict['pear'])

print(my_dict['stock'][1])
print(my_dict['name']['raphael'])

#easy to append
my_dict['job'] = 'DBA'

my_dict.keys() #show all keys
my_dict.values() # show all values
print(my_dict.items())




#################
####   Set   #### 
#################


# unique values, no repetition
myset = set()
myset.add(1)
myset.add(3)
myset.add(2)
myset.add(1)

print(myset)
myset.discard(2) # Discard the element, not index.
print(myset)
myset.clear() #Clear ALL elements
print(myset)




##################
## List
##################



# Accept string and numeric together
raphaellList = [ "July", 29 , 1981, 'Raphael', 'Brazil' ]
ivanList = [ "May", 10, 1975, 'Ivan', 'Bulgaria']
numList = [100, 200, 400, 1200, 2, 400, 200, 200, 8000]


#perform operation
sum = numList[0] + numList[3]
print(sum)
print(sum * 2)
print(numList[2:] * 2)

print(raphaellList[1]+ivanList[1]) # add specif items
print (raphaellList)	# Prints complete list

print (ivanList [0:3]) # Prints 3 elements FROM starting 0nd index element.
namesList = ivanList + raphaellList
print (namesList)

#update list
print(ivanList[0])
ivanList[0] = "December" #replace
print(ivanList)

#append List
ivanList.append(80000) # Append to the end of list (create a new last index)
print(ivanList)

#remove last item or specific index
ivanList.pop(0)

# Expression for list
len(numList) # len = length
min(numList) # minimum value of elements
max(numList) # maximum value of elements

# Function for list
numList.count(200) #count how many element is repeated.
numList.index(200) #Show location by index.

#function without arguments. Modify original sequnce and indexes.
print(numList)
numList.sort() # sort()
print (numList)
print(numList[0])
numList.reverse() # reverse()
print (numList)
print(numList[0])

# Convert From tuple
aTuple =(123, 'xyz', 'zara', 'abc')
newList = list(aTuple)
print(newList)



###################
## Tuples
###################



fullTuple = ('October', 2016, 21.5)

emptyTuple = ()
oneElementTuple = (50, )

print(emptyTuple)
print(oneElementTuple)

#substring procedures

### fullTuple[2] is same fullTuple.index(21.5)
partTuple = fullTuple[1:]
print(partTuple)
print(partTuple[0])

#Convert list TO Tuple
a = ['Luana', 29, 'Toronto']
convertedTuple = tuple(a)
print(convertedTuple)

# It is not allowed to ADD new elements in tuples, BUT concatenate yes.
newtuple = ()
newtuple = fullTuple + convertedTuple
print(newtuple)


