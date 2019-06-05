#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

c = float(input('\033[1;30mInforme a temperatura em ºC:\033[m '))
f = ((9*c)/5) + 32
print('A temperatura de \033[1;31m{}ºC\033[m corresponde a \033[1;34m{}ºF\033[m!'.format(c, f))
