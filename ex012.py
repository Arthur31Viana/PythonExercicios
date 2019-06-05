#Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

pro = float(input('\033[1;30mDigite o valor do produto: R$\033[m'))
desc = pro - (pro * 5 / 100)
print('O preço do produto com \033[1;31m5%\033[m de desconto é: R$\033[1;32m{:.2f}\033[m'.format(desc))
