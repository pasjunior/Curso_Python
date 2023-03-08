"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores po uma contagem regressiva començando de 10.
Somar todos os resultados: 70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado por 10: 301*10 = 3010
Obter o resto da divisão da conta anterior por 11: 3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
Se não:
    resulta é o valor da conta
"""

cpf_enviado_usuario = '746.824.890-70' \
    .replace('.', '') \
    .replace('-', '') 
contador_regressivo_1 = 10
nove_digitos = cpf_enviado_usuario[0:9]

soma_1 = 0
for digito in nove_digitos:
    soma_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (soma_1 * 10) % 11

if digito_1 > 9:
    digito_1 = 0
else:
    digito_1


"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF mais o primeiro digito calculado em 'digito_1', multiplicando cada um dos valores po uma contagem regressiva començando de 11.
Somar todos os resultados: 77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado por 10: 363*10 = 3630
Obter o resto da divisão da conta anterior por 11: 3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
Se não:
    resulta é o valor da conta
"""

contador_regressivo_2 = 11
dez_digitos = cpf_enviado_usuario[0:10]

soma_2 = 0
for digito in dez_digitos:
    soma_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (soma_2 * 10) % 11

if digito_2 > 9:
    digito_2 = 0
else:
    digito_2

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado:
    print(f'O CPF {cpf_gerado} é válido')
else:
    print('O CPF invalido')

