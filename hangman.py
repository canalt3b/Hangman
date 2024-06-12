palavra = 'banana'

def pega_pos(letra):
    return palavra.find(letra)

while True:
    for n in range(len(palavra)):
        print('_', end =' ')
    print()

    letra = input('Entre com uma letra: ')
    if letra in palavra:
        pos = pega_pos(letra)
        print(f'SIM {pos}')
    else:
        print('NÃO')

