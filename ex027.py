#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é: {} \nO seu último nome é: {}'.format(nome[0], nome[len(nome)-1]))
