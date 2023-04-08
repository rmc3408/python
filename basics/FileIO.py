#### FILE IO ####

# CREATE
f = open('basic.txt', 'w+') # Create using w = write and + (plus) to read and write.

# With statement - verify if is created before.
with open('basic.txt') as newf:
    content = f.read()
print(content)
f.close()

# WRITE
for i in range(10):
    f.write("This is line %d\n" %(i+1)) # write inside text file.
f.write('Last line, and close')
f.close() #then close

#READ
f = open('basic.txt', 'r') 
read = f.readlines()
print(read)
f.seek (40) # move cursor to position 40 (middle of file)
read = f.readlines()
print(read)
f.close()

# APPEND
f = open('basic.txt', 'a+') 
f.writelines('\n\nThis appended Line\n\n')

f = open('basic.txt', 'r') 
read = f.readlines()
f.close()
print(read)
