#!/usr/bin/python3


def parametros(**kwargs):
    print(kwargs)
'''*kwargs - transforma o parametro em um dicionario tem que definir os parametros com ='''

parametros(nome ='daniel', idade=24)



def parametros(*args):
    print(args)
'''*args - transforma o parametro em uma tupla'''

parametros('daniel', 'maria', 5, [], {})

