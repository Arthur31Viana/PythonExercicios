#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.

n = int(input('\033[1;30mDigite um número:\033[m '))
print('O dobro de \033[1;30m{}\033[m é \033[1;32m{}\033[m \nO triplo de \033[1;30m{}\033[m é \033[1;32m{}\033[m \nA raiz quadrada de \033[1;30m{}\033[m é \033[1;32m{:.2f}\033[m'.format(n, (n*2), n, (n*3), n, (n**(1/2))))
