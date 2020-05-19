wholeLine = "molinaro"

#Subtring
subLine_1char = wholeLine[1] #string index 1 = 2nd letter = o
subLine_4charfromStart = wholeLine[0:4] #string index 0,1,2,3 [start = 0 : stop= position (or index - 1) : skip) = moli

subLine_jumping2 = wholeLine[3:11:2] #starts on index 3(=i), get index 5 and index 7 (11 dont give error).
subLine_4charToEnd = wholeLine[4:] #index 4 to the end (= naro)

print(subLine_4charToEnd)

print(subLine_1char * 3) # print 3 times
print (wholeLine[0:6] + " is Powerfull") # Prints concatenated string
print (wholeLine + " is split in" , subLine_4charfromStart , "and" , subLine_4charToEnd)

name = "molinaro"
print ("Updated String :", name[:6] + ' elements')

#To invert the string  

# From the end index = -1, -2, -3,...
print(name[-1::]) # prints O

print(name[::-1])  # To inverted name, use -1  to backward one. -2 go backward two elements
print(name[::-2]) # inverted and jumping 1 letter backward.
print(name[-1:-9:-1]) # same as above


# Split method and Join method (by defaut () = space)
name = "Raphael is Cute"
name.split('is')
name.join('=')


# Format String methods. 
### It makes substitutions into places enclosed in braces.

student = input('Enter your name: ')
greeting='Hello, {}!' .format(student)
print(greeting)

instructor = input("Enter the prof's name: ")
subject = input("Enter the subject name: ")
term = input("Enter the term: ")

# uses concatenation
print ('{} will teach {} in {}'.format (instructor, subject, term))
print ('{1} will teach {1} with {0}'.format (instructor, subject, term))
print("My class is",subject,", and name is",student)
print("My class is "+ subject +" , and name is",student) 
print("my prof is {1} and my name is {0}" .format(student,instructor))


#	Sep operator = Combine any statement betweem comma defined by sep (default space or any elements).

num1 = input("Enter a number: ")
num2 = input("Enter a second number:")

print('The sum of ', num1, ' and ', num2, ' is ', num1+num2, '.', sep=';')
print(instructor, "willteach", subject, "in", term, sep='')
print(instructor, "willteach", subject, "in", term, sep='/')
print('The sum of ', num1 ,' and ', num2, ' is ', num1+num2, '.', sep=' is ')

#F-string 

print(f'The number 01 is {num1}')


#String Formatting Operator

# %s - String
# %d or %i - Integers
# %f - Float numbers
# %.<number of digits>f - float with a fixed amount of decimal digits

print ("My name is %s and I am %d years old!" % ('Jacky', 33)) # prints out
print("name = %s\nage = %.2f" %('Raphael',38))