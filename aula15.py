# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

# aqui eu já poderia fazer a conversão de tipo, porém isso pode gerar um trantorno
# no futuro, pois o meu programa poderia quebrar caso o usuário digite um caractere
# que não seja um número e eu não teria como checar o valor que foi digitado.
n1 = input('Digite um número: ') 
n2 = input('Digite outro número: ')

# a melhor prática é atribuir a conversão em outra variável.

int_n1 = int(n1)
int_n2 = int(n2)

print(f'A soma dos números é: {int_n1 + int_n2}')