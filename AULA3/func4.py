#!/usr/bin/python3

def ler_arquivo(nome:str)-> list:
    with open (nome, 'r') as arq:
        return arq.readlines()
    

def escrever_arquivo(nome, conteudo):
    with open(nome, 'a') as arq:
        arq.write(conteudo + '\n')

if __name__ =='__main__':
    print('hello')