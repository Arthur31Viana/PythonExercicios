#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('\033[1;30mDigite seu nome:\033[m ')
print('Bem-Vindo, \033[4;36m{}\033[m, è um prazer te conhecer!'.format(nome))
