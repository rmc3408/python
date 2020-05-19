import one

print('top level in TWO.py')

one.func()

if __name__ == '__main__':
    print('this is TWO Py directly')
else:
    print('Two is imported!')