# Exercício 1

entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Ímpar'

    if par_impar:
        par_impar_texto = 'PAR'

    print(f'o número {entrada_int} é {par_impar_texto}')
else:
    print('Digite um número inteiro')