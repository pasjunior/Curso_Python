def executa(funcao, *args):
    return funcao(*args)


print(
    executa(
        lambda x, y: x + y, 2, 3
    )
)

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = executa( lambda m: lambda n: n * m, 8)
print(duplica(4))

print(
    executa(
    lambda *args: sum(args)
    , 1, 2, 3, 4, 5
    )
)