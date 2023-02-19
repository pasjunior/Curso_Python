""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numero_validos = None
    num_1_float = None
    num_2_float = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = False
    
    if numero_validos is None:
        print('Digite um número válido')   
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 operador!1')
        continue
    
    print('Resolvendo sua conta, confira o resultado!')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '+':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui!!!')

    sair = input('Digite [s]im para sair: ').lower().startswith('s')

    if sair is True:
        break