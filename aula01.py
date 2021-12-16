import os
os.system('clear')
valor = float(input())
if valor >= 0 and valor <= 2000.00:
    print('Isento')
if valor > 2000.00 and valor <= 3000.00:
    imposto = (valor - 2000.00) * 0.08 
    print(f'R$ {imposto:.2f}') 
if valor > 3000.00 and valor <= 4500.00:
    imposto = (valor - 3000.00) * 0.18 + 80.00
    print(f'R$ {imposto:.2f}')
if valor > 4500.00:
    imposto = (valor - 4500.00) * 0.28 + 350.00
    print(f'R$ {imposto:.2f}')   
