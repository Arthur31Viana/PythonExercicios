#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

from math import hypot
co = float(input('\033[1;30mComprimento do cateto oposto:\033[m '))
ca = float(input('\033[1;30mComprimento do cateto adjacente:\033[m '))
print('A hipotenusa vai medir \033[1;31m{:.2f}\033[m'.format(hypot(co, ca)))
