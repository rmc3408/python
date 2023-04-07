# Call math class library
import math
x = 8.73
y = 2
print(math.ceil(x))
print(math.floor(x))
print(10>4)
print(4!=4)
print(min (11,2,34,-5,5))
print(max (11,2,34,-5,5))
print(max ('ac','az', 'adiuz'))

# To Show remainder e whole number from the division.
print(x%y) # remainder
print(x//y) # floor division

print(y**3) # or print(pow(y,3))
print(abs(x))
print(math.exp(1)) # = e (natural number)

#Round numbers

num = 32.1992
print(round(num,1))
print("my age is {}" .format(round(num,1)))

# Format Number 
# 
# define decimal cases. (.Format) or f-string(string interpolation)
# 10 number of total numbers 
# .2f  two decimal places floats. DONT forget add dot(period)

print("the number is {:10.2f}".format(num))
print(f'the number is {num:.2f}')