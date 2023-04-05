#### Class Syntax ####

'''
class CamelCase():
    
    ### Construtor - instanciate objects
    def _ _ init _ _(SELF, arg1, arg2):
        super()._ _ init_ _ (SELF, arg1, arg2)
        self.arg1 = arg1
        self.arg2 = arg2

      ####  attribute = argument ###
      #### Assign using self.attribute_name


    def lowercase():
        return num + 2
'''

a = [1,2,3,4,5]
# object.proprieties

class Dog():

    # 1
    specie = 'Animal'

    # 2
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        self.fullname = name+breed+Dog.specie

    # 3
    def speak(self, num):
        print('WOOF, '* num + f'name is {self.name}')

print('----- Class Definition------------')
mydog = Dog('lab','Rex')

print(type(mydog))
print(mydog.fullname)
print(mydog.name)
mydog.speak(3)












############################
#### Inheritance Syntax ####
############################

##  3 ##
#  Methods is function inside class
#  function for object
# must have self to connect to class Animal and cow.

## 2 ##
#  To instantiate user-defined object

## 1 ## 
# To create Class object attribute, 
#not connect to instance.
#General Attribute for all instance.


# Inheritance methods and attributes.

class Animal():

    def __init__(self, name):
        self.name = name
        print("Animal Created")
    
    def whichAnimal(self):
        print("I am mammal")
    
    def eat(self):
        print("Milk")

    def speak(self):
        raise NotImplementedError("Something goes wrong") 


''' In Next class,
 super().__init__('Dog') = Animal.__init__(self, name)
 '''
class Cow(Animal):

    def __init__(self, name): #Inherit from animal constructor
        print("Cow created!") 
#        super().__init__(name)        # NO SELF required
                                      # (1) Get all arg from any Base class
                                      # super() method with NO self 
        Animal.__init__(self, name)   # (2) Named Base class Call
                                      # Class name + (self, argX, ...)
    
    def whichAnimal(self):
        print(f"I am a cow called {self.name}.")

class Horse(Animal):

    # Optional have constructor , use from BASE class

    def speak(self):
        return self.name + " is a magical horse animal!!" 

print()
print('------     Inheritance    ---------')
pet1 = Cow('Victoria')
pet1.whichAnimal()
pet1.eat()
print()

pet2 = Horse('Unicorny')
pet2.whichAnimal()
print(pet2.speak())








############################
####    Polymorphism    ####
############################

class Bird():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Bruuu!")

class Tiger():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Roarr!")

print()
print('------   Polymorphism    --------')

mypet1 = Bird('Loro')
mypet2 = Tiger('Rei leao')

mypet1.speak()
mypet2.speak()

for animals in (mypet1, mypet2):
    print(animals.name)
    animals.speak()


############################
####    Abstract Class  ####
############################


''' 
LOOK AngryDog class
'''
# No content, never instaciate objects and 
# Serve as model as base class


class Scary():

    def __init__(self, name):
        self.name = name
        print("Horror Animal Created")
        
    def speak(self): # This is abstract method
        raise NotImplementedError("Something goes wrong") 

class AngryDog(Scary):

    def speak(self): # override
        return self.name + " is a bitten dog!!" 

print()
print('------   Abstract Class Method    --------')
monster = AngryDog('Cujo')
print(monster.speak())








############################################
####  Dunder, Magic or Special methods  ####
############################################

# use two underscores
## Override method from Main Object Class

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print('# BOOK #')

    def __str__(self): #Override from Object class.
        return f'{self.title}\nAuthor: {self.author}.'
    
    def __len__(self):
        return self.pages

class Magazine(Book):
    
    def __init__(self, category):
        super().__init__('scyFi', 'doctorWho', '50 to 100')
        print('@ MAGAZINE @')
        self.category = category

    def __str__(self):
        return 'Magazine: ' + self.category + '\nTitle: '+ Book.__str__(self)
            


print()
print('------   Dunder Method    --------')
b = Book('Python', 'Raph', 200)
# If not override show <__main__.Book object at 0x049438>
print(str(b))
print(len(b))
print()

d = Magazine('Fitness')
print(str(d))
