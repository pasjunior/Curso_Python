# insinstance -> para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome':'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print(item.upper())

    elif isinstance(item, (int, float)):
        print(item, item * 2)
    
    else:
        print('outro')
        print(item)