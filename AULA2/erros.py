#!/usr/bin/python3
letras = ['a' , 'b']
ling = {'daniel' : 'python'}

try:
    print(letras[2])
except IndexError:
    print('a lista contem apenas {} elementos'.format(len(letras)))

print(ling.get('erro'))

nome = 'python'
isinstance (nome,str)
