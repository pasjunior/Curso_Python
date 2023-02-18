nome = 'Paulo Junior'
tamano_nome = len(nome)
print(nome)
print(tamano_nome)

indice = 0
novo_nome = '*'
while indice < tamano_nome:
    letra = nome[indice]
    novo_nome += f'{letra}*'
    indice += 1
print(novo_nome)