palavra = 'banana'

def pega_pos(letra):
    return palavra.find(letra)

while True:
    for n in range(len(palavra)):
        print('_', end =' ')
    print()

    letra = input('Entre com uma letra: ')


# somente para teste

