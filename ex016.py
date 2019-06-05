''''#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
EX: Digite um valor: 6.127
O número digitado foi 6.127 e a sua porção intera é 6.'''

'''from math import trunc
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, trunc(n)))'''

n = float(input('\033[1;30mDigite um valor:\033[m '))
print('O valor digitado foi \033[1;31m{}\033[m e a sua porção inteira é \033[1;32m{}\033[m'.format(n, int(n)))
