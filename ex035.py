#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from time import sleep
print('-=-' * 10)
print('\033[1;30;44mAnalisador de Triângulos\033[m')
print('-=-' * 10)

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
print('ANALISANDO...')
sleep(2)
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('\033[1;32mOs segmentos a cima PODEM FORMAR um Triângulo!\033[m')
else:
    print('\033[1;31mOs segmentos a cima NÃO PODEM FORMAR um Triângulo\033[m')
