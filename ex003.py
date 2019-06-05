#Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('\033[1;30mDigite um número:\033[m '))
n2 = int(input('\033[1;30mDigite outro número:\033[m '))
s = n1+n2

print('A some entre \033[1;32m{}\033[m e \033[1;34m{}\033[m é: \033[1;31m{}\033[m'.format(n1, n2, s))
