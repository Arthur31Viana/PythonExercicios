#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

a = input('\033[1;30mDigite algo:\033[m ')
cores = {'limpa':'\033[m',
         'branca':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'verdeazulado':'\033[1;36m',
         'cinza':'\033[1;37m',
         'pretoebranco':'\033[7;30m'}

print('O tipo primitivo desse valor é {}{}{}'.format(cores['branca'], type(a), cores['limpa']))
print('É capitalizada? {}{}{}'.format(cores['vermelho'], a.istitle(), cores['limpa']))
print('Está em minúsculas? {}{}{}'.format(cores['verde'], a.islower(), cores['limpa']))
print('Está em maiúsculas? {}{}{}'.format(cores['amarelo'], a.isupper(), cores['limpa']))
print('É alfabético? {}{}{}'.format(cores['azul'], a.isalpha(), cores['limpa']))
print('É decimal? {}{}{}'.format(cores['roxo'], a.isdecimal(), cores['limpa']))
print('É alfanumérico? {}{}{}'.format(cores['verdeazulado'], a.isalnum(), cores['limpa']))
print('É um número? {}{}{}'.format(cores['cinza'], a.isnumeric(), cores['limpa']))
print('Só tem espaços? {}{}{}'.format(cores['pretoebranco'], a.isspace(), cores['limpa']))
print(a.isdigit())
print(a.isidentifier())
print('É impressa? {}{}{}'.format(cores['branca'], a.isprintable(), cores['limpa']))
