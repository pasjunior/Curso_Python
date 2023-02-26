"""
Faça uma lista de compras com listas, o usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista,
não permita que o programa quebre com erros de índices inexistentes na lista.
"""

lista_compras = []
produto = []
opcao = ''

while opcao != 's':
    opcao = input('Selecione uma opção: \n'
      '[i]nserir | [a]pagar | [l]istar | [s]air: ')
    
    if opcao == 'i':
        produto = input('Digite um produto: ')
        lista_compras.append(produto)
    elif opcao == 'a':
        indice_str = input('Digite um índice: ')
        try:
            indice = int(indice_str)
            del lista_compras[indice]
        except ValueError:
            print(f'Por favor digite um número inteiro, o índice {indice} não é um número inteiro!')
        except IndexError:
            print(f'O índice {indice} não existe na lista')
        except Exception:
            print('Erro desconhecido!')
    elif opcao == 'l':
        if len(lista_compras) == 0:
            print('A lista não contém produtos, insira algum produto!')
        for i, valor in enumerate(lista_compras):
            print(i, valor)
    else:
        print('Digite uma opção válida!')
    