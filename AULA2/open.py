#!/usr/bin/python3

#chmod = rwx(user)rw0(grupo)r--(outros)

'''arq = open('teste.txt' , 'r')
print(arq.read())
arq.close()'''

with open ('teste.txt', 'r') as arq:
    print(arq.read())

with open ('teste.txt', 'a') as arq:
    arq.write('oi\n')

with open ('teste.txt', 'r') as arq:
    print(arq.read())

lista = ['a' , 'b' , 'c']
with open('teste.txt', 'a') as arq:
    arq.writelines(lista)