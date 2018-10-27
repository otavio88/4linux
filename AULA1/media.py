#!/usr/bin/python3
n1=float(input("Entre com a primeira nota: "))
n2=float(input("Entre com a segunda nota:  "))
n3=float(input("Entre com a terceira nota:  "))
n4=float(input("Entre com a quarta nota:  "))
media  = (n1+n2+n3+n4)/4
if media >= 7:
    print("Aprovado")
elif media >3:   
    print("REcuperacao")
else:
        print("reprovado")