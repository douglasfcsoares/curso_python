"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
# string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
# lista = [123, True, 'Douglas Soares',  1.2, []]
lista = [10, 20, 30, 40, 50, 60]
# print(lista[2].upper())
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))

lista.append(70)
print(lista)
lista.pop()
print(lista)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)
