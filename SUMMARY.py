########################
#### USEFUL SUMMARY ####
########################


# Jump a Line
print

# Declaring Variables
a = 40
b = 10 + a

# Loops
if a > b:
    print("A is bigger")
else:
    print("B is Bigger")
print(a)
print(b)

# Multilines
sum = a +\
      b +\
    b
print(sum)

# List is similar to Arrays.

list = [200, "My name is ", 400, "Raphael"]

print(list[2], list[0])

sumNumber = list[0] + list[2]
print(sumNumber)

# Multiples Lines. ===  USE triple quotation #
greetings = """ This line is long enough
 to break. """
print(greetings)

print("A + B is equal to ", a+b)




# Variable

# different variables with ONE value;
state = letter = fedexCode = 4032
print(state)
print(fedexCode)

# different variable with 2 values.
tax = price = 3, 12
print(tax)
print(price)
print

# declare variables in one line.
price, tax, cost = 10, 2, 12

print(" The price is ", price)
print(" final cost is ", cost)





# Prompt input from user.
#input(PROMT)

name = input("please, What is your name? ")
ageYou = input("How old are you? ")
ageBrother = input("How old is your brother? ")
print()
print(" Your name is", name, "and your age is", ageYou, ".")
print(ageYou + ageBrother)

age1 = int(input("How old are you? "))
age2 = int(input("How old is your brother? "))
sumAges = age1 + age2
print("The sum of ages is equal to", sumAges)

# Using input to enter 2 numbers. Use .split()
a , b  = input("enter two numbers? ") .split()

print(a)
print(b)
print(a+b)
x, y = (float(a), float(b))
print(x)
print(y)
print(x+y)

# Convert string input to int or float
a = int(input("What is your age")) # age = 38
b = float(input("What is your age")) # age = 38.5




# Call math class library
import math
x = 8.7
print(math.ceil(x))
print(math.floor(x))
print(10>4)
print(4!=4)
print(min (11,2,34,-5,5))
print(max (11,2,34,-5,5))
print(math.exp(1)) # = e (natural number)

# Jump a Line
print

# Declaring Variables
a = 40
b = 10 + a


# Multilines
sum = a +\
      b +\
    b
print(sum)

# List is similar to Arrays.

list = [200, "My name is ", 400, "Raphael"]

print(list[2], list[0])

sumNumber = list[0] + list[2]
print(sumNumber)

# Multiples Lines. ===  USE triple quotation #
greetings = """ This line is long enough
 to break. """
print(greetings)

print("A + B is equal to ", a+b)

# Variable

# different variables with ONE value;
state = letter = fedexCode = 4032
print(state)
print(fedexCode)

# different variable with 2 values.
tax = price = 3, 12
print(tax)
print(price)
print

# declare variables in one line.
price, tax, cost = 10, 2, 12

print(" The price is ", price)
print(" final cost is ", cost)

# Prompt input from user.
#input("PROMT")


# Convert string input to int or float
a = int(input("What is your age?")) # age = 38
b = float(input("What is your age?")) # age = 38.5


# Substring [index number, numberOfCharacters]
wholeLine = "PythonString"

subLine_1char = wholeLine[1]
subLine_4char = wholeLine[0:4]
subLine_jumping2 = wholeLine[3:11:2]
subLine_4charToEnd = wholeLine[4:]

# Print wild cards

print(subLine_1char * 3) # print 3 times
print (wholeLine[0:6] + " is Powerfull") # Prints concatenated string
print (wholeLine + " is split in" , subLine_4char , "and" , subLine_4charToEnd)

#Replace substring.
# We can not replace or modify Strings... only list.
slice1 = wholeLine[0:3]
print(slice1)
slice2 = wholeLine[4:]
new = "H"
newWholeLine = slice1 + new + slice2
print(newWholeLine)


#List
raphaellList = [ "July", 29 , 1981, 'Raphael', 'Brazil' ]
ivanList = [ "May", 10, 1975, 'Ivan', 'Bulgaria']

#perform operation
print(raphaellList[1]+ivanList[1])

print (raphaellList)	# Prints complete list
print (ivanList [0:3]) # Prints 3 elements FROM starting 0nd element.
namesList = ivanList + raphaellList
print (namesList)

#update list
print(ivanList[0])
ivanList[0] = "July" #replace
print(ivanList)

#append List
ivanList.append(80000)
print(ivanList)

# call random module random library and use Alias name
import random as r
x = r.randrange(3, 9)
print(x)
print(r.randint(1,50))



###Range
for num in range(10): # Start=index 0, stop= not include 10, skip: 2    print(num)
    print(num)

for num in range(0,11,2): # Start=index 0, stop= 11 -1, skip: 2    print(num)
    print(num)

l1 = list(range(0,11,2)) # make a list
print(l1)

#Enumerate
word = 'abcde' # Enumerate each letter to a number.
for index,letter in enumerate(word):
    print(f'index\t{index} - letter\t{letter}')

#ZIP
list1 = [1,2,3,4] #ZIP according small size.
list2 = [10,20,30] # ZIP makes packing tuple pairs.
for a,b in zip(list1,list2):
    print(a,b)

#IN
'25' in list2 # IN checks presence or not. Return boolean.




