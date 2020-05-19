# call random module random library and use Alias name
import random as r

x = r.randrange(3, 9) # include endpoint
print(x)
print(r.randint(1,50))

list1 = [1,2,3,4,5,6,7,8,9,0]
r.shuffle(list1)
print(list1)
print('------------')


#### to Generate several random numbers
def rand_num(low, high, n):
    for x in range(n):
        yield r.randint(low, high)
for n in rand_num(1,12,4):
    print(n)