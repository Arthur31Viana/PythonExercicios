#Escreva um programa que pergunte a quantidade de KM pecorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.calcule o preço a pagar. Sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.

al = int(input('\033[1;30mQuantos dias alugado?\033[m '))
km = float(input('\033[1;30mQuanto KM rodados:\033[m '))
print('Total a pagar é de R$\033[1;32m{:.2f}\033[m'.format((al*60)+(km*0.15)))
