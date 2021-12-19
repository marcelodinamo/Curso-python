import os
os.system('clear')


"""
Função (def) em python - *args  **kwargs 
"""

def funcao(*args, **kwargs):
    print(args)

    idade = kwargs.get("idade")

    if idade is not None:
        print(idade)
    else:
        print('Argumento não existe')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
funcao(*lista, lista2, nome = 'Marcelo', sobrenome = 'Luiz', idade = 48)            
