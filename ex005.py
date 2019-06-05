#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('\033[1;30mDigite um número:\033[m '))
print('O Sucessor de \033[1;30;41m{}\033[m é \033[1;30;44m{}\033[m e o antecessor é \033[1;30;42m{}\033[m'.format(n, (n+1), (n-1)))
