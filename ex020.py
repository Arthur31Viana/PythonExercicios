#O mesmo professor anterior quer sortear a ordem de apresentação de trabalho dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('Aluno 01: '))
n2 = str(input('Aluno 02: '))
n3 = str(input('Aluno 03: '))
n4 = str(input('Aluno 04: '))
lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
