#aqui na função print estou enviando argumentos não nomeados.
print(12 ,34)

# o argumento nomeado sep vem de separador e ele define
# o separador no resultado dos argumentos não nomeados que
# por padrão é o espaço
print(56, 78, sep="-")

# \r\n -> CRLF são caracteres que não vemos mas realizam a função de quebra de linha.
# \n -> LF


# o argumento end que significa ao final do print,
# definimos o comportamento no final da função se
# será uma quebra de linha com o padrão windows \r\n
# ou com o padrão unix \n ou se colocaremos algum
# outro caractere como nos exemplos abaixo.
print(10, 11, sep='-', end='\r\n')

print(10, 11, sep='-', end='##')

# ainda podemos adicionar o caractere mais a 
# querbra de linha. onde que com os windows mais
# modernos como 10 e 11 o padrão unix também funciona.
print(10, 11, sep='-', end='##\n')

# podemos usar a quebra de linha tanto antes como depois dos caracteres colocados ao final.
print(10, 11, sep='-', end='\n##')

print(' Vim para a próxima linha.')