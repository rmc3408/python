
########################
####   Decorators   ####
########################

# to switch on and Off codes inside function.
# Use @ operator

def hello(name='John'):
        
    def welcome():
        return "WELCOME inside Hello Function"
    def bye():
        return 'Say BYE to inside hello function'
    
    print('! Function executed !')
    if name == 'Jess':
        return welcome  # function without parameter
                        # will not be execute!
    else:
        return bye
    #  print(welcome())  # Only inside Hello function scope
    #  print(bye())      # order matters

''' variable my_function === function. '''

my_new_function = hello('Jess')
my_other_function = hello('Susan')

print(my_new_function()) # Choose function by name


# Explanation and EXAMPLE!
def congrats():
    return 'HBD, Jose'
def printable(sample):      # Decorator around sample. 
    print('--------------') # Wrap code
    print(sample())
    print('--------------') # wrap code

printable(congrats) 
''' They get CONGRATS function and wrap with codes
around this function as function to decorate !!! '''

@printable  # @ THIS IS SHORTCUT  #
def func_gift_to_be_decorated(): # Assign to sample
    return 'Any text is to be beautiful'
    # assign txt to SAMPLE variable






########################
####   Generators   ####
########################


''' Generator is like for loops. However, they 
compute ONE value PER TIME in a sequence 
and WAIT until next value is called for.

Saves function, NOT all data in memory '''

'''
###### OLD METHOD #######
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(n**3)
    return result
print(create_cubes(6))
########################'''

def create_cubes(n):
    for x in range(n):
        yield x ** 3
print(create_cubes(5)) # on memory only
a = tuple(create_cubes(5)) #save from memory in list, tuples
print(a)

''' Iteration object is like iteraction loops(for)
they analyze one by one ''' 

def simple_generator(): # Generator Function
    for x in range(5):
        yield x         # what will be on memory
for num in simple_generator(): ### Just to visualize
    print(num)
###### Create a generate object ######
g = simple_generator() # Function saved in object

print(next(g))    ######## next function
print(next(g))    ######## next function

############ iter function instead for
st = 'Raphael'
#for l in st:
#    print(l)

st_iterated = iter(st)
print(next(st_iterated)) ######## iter function
print(next(st_iterated)) ######## iter function
