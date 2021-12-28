import os
os.system('clear')

def func_mestre(func, *args, **kwargs):
    return func(*args, **kwargs)
 

def func1(nome):
    return f'oi {nome}'

def func2(nome, saudacao):
    return f'{saudacao} {nome}'

var1 = func_mestre(func1, 'Marcelo')
var2 = func_mestre(func2, 'Marcelo', saudacao = 'Bom dia')
print(var1)
print(var2)
