import os
os.system('clear')

def funcao(saudacao, nome):
    print(saudacao, nome)
funcao('ola', 'marcelo') 

def funcao1(n1, n2, n3):
    soma = n1 + n2 + n3
    print(soma)
funcao1(2, 3, 5)   

def funcao2(n1 , n2):
    return (n1 * n2/100) + n1
print(funcao2(50, 10))    

def fizzbuzz(n1):
    if n1 % 5 == 0 and n1 % 3 == 0:
        return 'FizzBuzz'

    if n1 % 3 == 0:
        return 'Fizz'
        
    if n1 % 5 == 0:
        return 'Buzz'    
    return n1
print(fizzbuzz(10))
print(fizzbuzz(15))
print(fizzbuzz(9))
print(fizzbuzz(7))