# string com quegra de linha pode ser incluída entre ''' or """
texto = '''Este texto tem mais de uma linha
e esta é a segunda linha do texto'''

print(texto)

# split a string

texto = 'esta é uma string em python, ela será utilizada para alguns exemplos de utilização de string'

parte_do_texto = texto[0:27]
print(parte_do_texto)

fatias_do_texto = texto.split(',')
print(fatias_do_texto)

s = 0
for letra in texto:
    if letra == 's':
        s += 1

print('A letra s aparece %d vezes no texto.' % s)

palavras = []
for p in fatias_do_texto:
    palavras += p.split(' ')

print(palavras)

p = 0
for palavra in palavras:
    if palavra == 'string':
        p += 1

print('A palavra string aparece %d vezes no texto.' % p)

# replace part of string
print(texto.replace("s","z"))
print(id(texto))

z = id(texto.replace("s","z"))
print(id(z))

print(id(texto.replace("s","m")))
