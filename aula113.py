# Exercícios com funções

'''
Exercício 1 - Crie uma função que multuplica todos os argumentos não nomeados recebidos e 
retorne o total para uma variável e mostro o valor da variável.
'''

'''
Exercício 2 - Crie uma função que retorna se o número é par ou ímpar.
'''

# Exercício 1

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplica(1, 2, 3, 4, 5)
print(multiplicacao)
valor_correto = print(1*2*3*4*5)

# Exercício 2
def parimpar(x):
    if x % 2 == 0:
        return 'O valor é PAR'
    else:
        return 'O valor é IMPAR'

valor = parimpar(9)
print(valor)