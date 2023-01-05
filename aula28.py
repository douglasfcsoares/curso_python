'''
Exercício
Peça ao usuário para digitar seu nome.
Peça ao usuário para digitar sua idade.
Se o nome e idade forem digitados:
    Exiba:
        seu nome é:
        seu nome invertido é:
        se nome contem (ou não) espaços
        seu nome tem{n} letras
        a primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba:
        "Desculpe, você deixou campos vazios."
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f' seu nome é {nome}')
    print(f' seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('seu nome contem espaços')
    else:
        print('seu nome não contem espaços')

    print(f' seu nome tem {len(nome)} letras')
    print(f' a primeira letra do seu nome é {nome[0]}')
    print(f' a ultima letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')
