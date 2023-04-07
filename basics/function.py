#
# HELP and details about function
#
''' help(print) '''


##############     SCOPE   ########################
### Assings value to variable
## order and location where matter.

# Local > enclosing function > global >  built-In

# To OVERRIDE global variable -> use global

##################################################

# Create function
def add_function(num1, num2):  # def is define
    # name in lowercase and underscore
    # ()
    # arguments order matters, optional in end.
    # a colon : to indent.
    print('hello')
    return num1 + num2


add_function(2, 3)


## Arguments can be optional value by default.
# No return type as default


def fnamed(name='John Doe'):
    print(name)


fnamed()

''' If not return type, can not send the value to variable.'''


def fnamereturned(name='Mary Doe'):
    return name


result = fnamereturned()
print(result)

st = 'The dog is on the table.'


def old_fanimal(st):
    if 'dog' in st.lower():
        return True
    else:
        return False


''' or '''


def fanimal(st):
    return 'dog' in st.lower()


print(fanimal(st))


## Arbitary arguments and keyword arguments##
### If wanna pass multiple parameters inside argument, must be more than one *args and order matters ###

def myArgs(*args):  ## ArgumentS = *args ##
    return sum(args)  # Must be use *(asterisk) + args -> pass Tuple


print(myArgs(2, 5, 10, 20))


def keyArgs(**kwargs):  # keywords arguments = **kwargs - USE two astericks
    print(kwargs)  # Pass many parameters to dictionary as keyword.
    if 'fruit' in kwargs:
        print('My fruit is {}.'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit')


keyArgs(fruit='apple', veggie='pepper')

#######################
####      MAP      ####
#######################

numbers = [1, 2, 3, 4, 5]


def square(num):
    return num ** 2


for i in map(square, numbers):  # pass function as argument.
    print(i)

##    map(square, numbers) -> only save in memory
''' OR'''
print(list(map(square, numbers)))

stList = ['Andy', 'is', 'bore']


def splicer(st):
    if len(st) % 2 == 0:
        return 'EVEN'


##    map(splicer, stList) -> only save in memory
''' OR'''
print(list(map(splicer, stList)))

#######################
####    FILTER     ####
#######################

# Return boolean. ONLY elements which pass as TRUE will be Saved at memory. 
numbers = [1, 2, 3, 4, 5, 6, 7]


def check(num):
    return num % 2 == 0


##    filter(check, numbers) -> only save in memory

print(list(filter(check, numbers)))

#######################
####    LAMBDA     ####
#######################

# used only once! 
# NO def 
# NO name, name is lambda.
# num is argument.
# Always return

square = lambda num: num ** 2  # assigned lambda function as square, to use more than only once.
print(square(9))
print(square(5))

# usually, it uses lambda in map or filter.

map(lambda num: num ** 2, numbers)  # Show all numbers and return saving in memory
filter(lambda num: num % 2 == 0, numbers)  # Show ONLY numbers TRUE in filter function
#    and return only those to save in memory

# To Save items in List -> list(map(...)) or list(filter(...))

names = ['Andy', 'Suzy', 'John']
print(list(map(lambda x: x[0], names)))
print(list(map(lambda x: x[::-1], names)))
