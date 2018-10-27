#!/usr/bin/python3


carrinho = []
produto1 = {"nome":"Tenis","valor":21.70}
produto2 = {"nome":"Meia","valor":10}
produto3 = {"nome":"Camiseta","valor":17.30}
produto4 = {"nome":"Calca","valor":100.00}
carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
carrinho.append(produto4)
def totalCarrinho(carrinho):
    return sum(produto["valor"] for produto in carrinho)

def cupomDesconto(cupom=""):
    if cupom == "xyzgratis":
        return 0.50
    else:
        return 1
print("o total da sua compra e: ",(totalCarrinho(carrinho)*cupomDesconto()))
print("utilizando o cupom xyzgratis o valor sera de ",(totalCarrinho(carrinho)*cupomDesconto("xyzgratis")))


'''convidados = []

def adicionar(nome):
    função para adicionar convidados na lista
    global convidados
    convidados.append(nome)

while True:
    nome = input('digite um nome ou sair: ')
    if nome.strip().lower() =='sair':
        break
    adicionar(nome)
print(convidados)    '''


'''nome = input ("Digite seu nome: ") 
idade = int(input("Digite sua idade: "))
def adicionar():
    convidados = (nome,idade)
    if idade <18:
        print("Voce nao pode participar da festa")
    else:
        print("boa festa") 
        print(convidados)

adicionar() '''
'''o comentario da funcao fica na especificacao dela  - adicionar.__doc__'''

# var = 10

# def escopo():
#     var = 5
#     print(var)

# escopo()
# print(var)

# def escopo():
#     global var
#     var = 5
#     print(var)

# escopo()


'''def somar(x, y=5):
    return x + y
as variaves são locais dentro da funcão e fora são globais
somar(2)
print(somar)

def teste()

    for x in range()

    pass'''



'''def somar(x, y):
    return x + y 
    
    
somar(3,5)

print(somar(somar(3,5),somar(2,2)))'''



'''def funcao():
    print('hello world')

funcao()
funcao()

print(funcao)'''