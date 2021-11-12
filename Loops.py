####### LOOPS ########

# If, elif, else
a = 16
b = 10

if a > b:  # finish with colon!!!
    print("A is bigger")  # indentation
elif a == b:
    print('A is equal B')
else:
    print("B is Bigger")

##### For
mylist = (1, 2, 3, 4)
for num in mylist:
    print(num)

for n in mylist:
    if n % 2 == 0:
        print(f'the number is {n}')

astring = 'Raph'
for l in astring:
    print(l)

# WHILE
x = 0
while x < 10:
    if x == 8:
        # break
        pass
        # continue
        # continue(next loop), pass(not empty) or break
    print(x)
    x += 1

    ##################
#### LOOPS STATEMENTS #####
##################

s = 'geeksforgeeks'

# Break -> Break statement ++ bring the CONTROL OUT of the loop
# when some external condition is triggered.
for letter in s:
    if letter == 'e' or letter == 's':
        break
    print(letter, end=' ')
print()  # print out only "g " and stop.

# Continue -> do NOT terminating the loop, it forces to execute the next iteration
#  of the loop.
for letter in s:
    if letter == 'e' or letter == 's':
        continue
    print(letter, end=" ")
print()  # print out only " g k f o r g k" .. Jump any 'e' or 's'.

# Pass -> used to write empty loops.
for letter in s:
    if letter == 'e' or letter == 's':
        pass
    print(letter, end=" ")

#####################
# NESTED LOOP
#####################

myNested = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        myNested.append(x * y)
print(myNested)

st = 'Print every word in this sentence that has an even number of letters'
# my_listst = []
my_listst = st.split()

for n in my_listst:
    if len(n) % 2 == 0:
        print(f'word:\t{n} - even')
    else:
        print(f'word:\t{n} - odd')

#######################
# LIST COMPREHENSION
#######################

myS = 'HELLO'
my_list = []

for stx in myS:
    my_list.append(stx)
print(my_list)
print()

# DONT do it ! === [ {expression} for OneItems in ThisSequence ]

myListLetters = [letter for letter in myS]
# print out [H, E, L, L, O]
print(myListLetters)
print()

myListNum = [num ** 2 for num in range(0, 11)]
print(myListNum)
print()

myPerfectSquare = [num for num in range(0, 11) if num % 2 == 0]
print(myPerfectSquare)
print()

myLC = [x[0] for x in st.split()]  # Get first letter of each word in the sentence.
print(myLC)
print()

# TUPLE UNPACKING
coord = [(1, 2), (3, 4), (5, 6), ('a', 'b')]
len(coord)  # Output: 4

for a in coord:
    print(f'tuples cords: {a}')
print()

for (a, b) in coord:
    print(f'first elem {a}')
    print(f'second elem {b}')
print()

for a, b in coord:
    print(a)
print()

# In dict, only iterate in keys, not values.
dicionario = {'k1': 100, 'k2': 200, 'k3': 500}

# this code does not work, it not a list
# for k, v in d:
#   print(f' keys are {k} and values {v}')

for key_name in dicionario:
    print(key_name)
print()

for n in dicionario.values():  # values() or keys()
    print(n)
print()

for key, value in dicionario.items():  # d.items() - pair
    print(key)
    print(value)
print()

# a > b ? print('A') : print('B')
