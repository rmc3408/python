import one

print('top level in TWO.py')


def func_two():
    print('Func in Two Py file ')


one.func_one()

if __name__ == '__main__':
    print('this is TWO Py directly')
else:
    print('Two is imported!')
