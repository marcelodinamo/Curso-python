import os
os.system('clear')

cpf = [1,6,8,9,9,5,3,5,0]
cont = 10
soma = 0
for i in cpf:
    soma = (i * cont) + soma
    cont -= 1
digito1 = (11 - (soma % 11))
if digito1 > 9:
    digito1 = 0
cpf.append(digito1)   
cont = 11
soma = 0
for i in cpf:
    soma = (i * cont) + soma 
    cont -= 1
digito2 = 11 -(soma % 11)
cpf.append(digito2)
cpf = str(cpf)
print(cpf)