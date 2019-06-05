#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('\033[1;30mDigite a nota 01:\033[m '))
n2 = float(input('\033[1;30mDigite a nota 02:\033[m '))
média = (n1+n2) / 2
print('A nota final do aluno é: \033[1;32m{}\033[m'.format(média))
