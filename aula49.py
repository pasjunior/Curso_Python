numero_str = input('Vou dobrar o número: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso Não é um número')