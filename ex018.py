#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
n = float(input('\033[1;30mDigite um ângulo:\033[m '))
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelha':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m'}
print('O seno do ângulo {}{}{} é {}{:.2f}{} \nO cosseno do ângulo {}{}{} é {}{:.2f}{} \nA tangente do ângulo {}{}{} é {}{:.2f}{}'.format(cores['branco'], n, cores['limpa'], cores['vermelha'], sin(radians(n)), cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], cos(radians(n)), cores['limpa'], cores['branco'], n, cores['limpa'], cores['amarelo'], tan(radians(n)), cores['limpa']))
