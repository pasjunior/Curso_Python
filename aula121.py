# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get obtém uma chave
# pop - apaga um item com a chave especializada (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro
import copy

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900
}

# print(len(pessoa))
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())
# pessoa.setdefault('idade', 30)
# print(pessoa['idade'])
'''
d1 = {
    'c1': 1,
    'c2': 2,
}

d2 = d1.copy()

d2['c1'] = 1000

print(d1)
'''

p1 = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
}

# print(p1.get('nome', 'Não existe'))
# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
p1.update(nome= 'Paulo Alves', idade= 30)
print(p1)