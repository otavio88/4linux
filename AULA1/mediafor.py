#!/usr/bin/python3

qtd = int(input("Qtd de notas: "))
soma = 0 
for x in range(qtd):
    nota = float (input('DIgite n{}: '.format(x+1)))
    soma += nota
media = soma / qtd 
if media >= 7:
    print("Aprovado, sua media foi {}" .format(media))
elif media >3:   
    print("REcuperacao, sua media foi {}" .format(media))
else:
    print("reprovado, sua media foi {}" .format(media))