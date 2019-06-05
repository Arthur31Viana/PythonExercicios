#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sa = float(input('\033[1;30mDigite o salário: R$\033[m'))
au = sa + (sa*15/100)
print('O salário do funcionário com \033[1;32m15%\033[m de aumento é: R$\033[1;32m{:.2f}\033[m'.format(au))
