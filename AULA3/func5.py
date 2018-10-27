#!/usr/bin/python3

import func4

#print(func4.ler_arquivo('teste.txt'))

func4.escrever_arquivo('teste.txt', 'conteudo')


##OU##

from func4 import escrever_arquivo

#print(func4.ler_arquivo('teste.txt'))

escrever_arquivo('teste.txt', 'conteudo')

##OU## 


from func4 import escrever_arquivo as escrever

#print(func4.ler_arquivo('teste.txt'))

escrever('teste.txt', 'conteudo')