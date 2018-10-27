#!/usr/bin/python3

qtd = int(input("Qtd de notas: "))
semestre = {}
soma = 0
for y in range (2):
    print('Notas do semestre {}'.format(y+1))
    for x in range(qtd):
        nota = float (input('DIgite n{}: '.format(x+1)))
        soma += nota
    
    if soma / qtd >= 7:
        result = ("Aprovado, sua media foi {}" .format(soma / qtd))
    elif media >3:   
        result ("REcuperacao, sua media foi {}" .format(soma / qtd))
    else:
        result ("reprovado, sua media foi {}" .format(soma / qtd))
    soma = 0 
    semestre ['semestre{}'.format(y+1)] = result
print(semestre)