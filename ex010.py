#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27

d = float(input('Quanto dinheiro você tem na carteira? R$ '))
print(' Com R$\033[1;31m{:.2f}\033[m você pode comprar US$\033[1;32m{:.2f}\033[m'.format(d, d/3.27))
