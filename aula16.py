# if /   elfi    / else
# se / se não se / se não

entrada = input('Você quer entrar no sistema ? ')

if entrada == 'entrar':
    print('Você entrou no sistema.')

    print(123)
elif entrada == 'sair':
    print('você saiu do sistema')
else:
    print('você não digitou nem entrar e nem sair.')

print('fora dos blocos if')
