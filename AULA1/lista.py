#!/usr/bin/python3

lista = ['mateus' , 'eduardo' , 'leandro']
nome=str(input('Entre com a busca: '))
for x in lista:
    if nome==lista:
        print('ESta na lista')
        break
else:
    print('nao esta na lista')

letras = []
for x in range (97, 97+26):
    letras.append(chr(x))
print(letras)