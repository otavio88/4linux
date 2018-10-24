#!/usr/bin/python3

qtd = 1
for qtd in range (1,2):
    while qtd <=40:
        emp=int(input("Qual a sua idade? "))
        if emp >= 18:
            print("Liberado, bom filme!")
        else:
            emp1=str(input("Voce esta acompanhando de algum maior: "))
            if emp1 == "sim":
                print("LIBERADO, bom filme")
            else:
                print("Go home")
qtd = + 1
