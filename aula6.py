import os
os.system('clear')

def func1():
    return 'Marcelo Luiz'

def func2(func3):
    return func3()

var = func2(func1)
print(var)       