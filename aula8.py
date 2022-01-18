import os
os.system('clear')

respostas = {
    'items' : {
    'item 1' : {'a' : '1', 'b' : '2', 'c' : '3'}
}
}

for i, n in respostas.items():
    for h, j in n['item 1'].items():
        print(f'({h}) : {j}')


