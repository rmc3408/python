# Error handling avoid stop running rest of your code.
''''''''''''''''''
#  try:      except:       else:      finally:
''''''''''''''''''


def add(n1, n2):
    print(n1 + n2)


''' add(10,'5') - int and str is impossible'''

######
##### To no finish, use WHILE loop

end = False
while not end:
    try:

        number1 = 7
        number2 = int(input('number 2?'))  # if str =error
        result = number1 + number2

    except ValueError:
        print('PLEASE, Enter number only')
        continue  # re-start while loops.

    else:
        print('Input was entered well')
        print(result)
        end = True  # or BREAK

    finally:  # With error or not WILL RUN
        print('Lets ask again')

print('\n' * 3)

try:
    f = open('basic.txt', 'r')
    f.write('Test line')

### code you find which type of error and handle.

except TypeError:
    print('TypeError')
except OSError:
    print('You have IO/OS error!')
except:
    print('All other errors!!!')
finally:
    print('I always run')
