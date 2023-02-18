nome = input('Digite seu nome: ')
tamanho_nome = len(nome)


if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é muito curto')
    elif tamanho_nome > 4 and tamanho_nome <= 6:
        print('Se nome é normal')
    else:
        print('Seu nome é grande')

else:
    print('Digite mais de uma leta')
