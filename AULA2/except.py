#!/usr/bin/python3

try:

    nome=int(input('Entre com a busca: '))
'''
n =input('digie um numero')
n = int (n)
converte dps que estiver na memoria
...'''
except ValueError:
    print("TRatamento VAlue error")
except Exception:
    print ("Voce digitou errado")
