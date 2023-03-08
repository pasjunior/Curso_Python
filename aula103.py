import random

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))

contador_regressivo_1 = 10


soma_1 = 0
for digito in nove_digitos:
    soma_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (soma_1 * 10) % 11

if digito_1 > 9:
    digito_1 = 0
else:
    digito_1


contador_regressivo_2 = 11
dez_digitos = nove_digitos + str(digito_1)

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

print(cpf_gerado)
