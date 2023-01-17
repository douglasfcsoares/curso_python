# Exemplos de uso dos Set

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if len(letra) > 1:
        print('Digite somente uma letra!')
        letras.discard(letra)
        continue
    elif 'l' in letras:
        print('PARABÉNS!')
        break

    print(letras)
