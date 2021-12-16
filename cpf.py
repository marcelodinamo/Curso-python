import os
os.system('clear')
cpfe = input('Entre com seu CPF: ')
cpf = cpfe[:-2]  # escrui os dois ultimos digitos
if cpf.isdecimal():  # verifica se o que foi digitado é decimal 
    cpf = list(map(int, cpf)) # converte lista de string em lista de inteiros
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
    cpfg = "".join(map(str, cpf))
    print(cpfg)
    if cpfg == cpfe:
        print('CPF Valido!!')
    else:
        print('CPF invalido!!')    
else:
    print('Você digitou algo errado!!')     