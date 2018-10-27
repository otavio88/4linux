#!/usr/bin/python3
    
arq = input('Entre com o nome do arquivo :')
shebang = '#!/usr/bin/python3' 
try:
    with open (arq, 'x') as uv:         
        arq.write(shebang)
except FileExistsError:
    print('O arquivo ja existe')
    with open(arq, 'r') as uv:
        conteudo = uv.readlines()
    if conteudo:
        if conteudo[0] != shebang:
            conteudo.insert(0,shebang)
        with open(arq, 'w') as uv:
            arq.writelines(conteudo)
    else:
        with open(arq, 'a') as uv:
            arq.write(shebang)

    