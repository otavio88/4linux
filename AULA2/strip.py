#!/usr/bin/python3
 
ling = input('qual a melhor linguagem')

ling = ling.strip().lower()
 #strip = tira os espacos - lower - coloca em minusculo
if ling == 'python':
     print('ok')
elif ling =='html' or ling == 'css':
    raise ValueError('isso nao e linguagem de programacao')
else:
    print('mude para python!')

#codyanywhere