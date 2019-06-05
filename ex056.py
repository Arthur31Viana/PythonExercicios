#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idade = 0
totid = 0
maior = 0
nmaior = ''
mulher = 0
from datetime import date
ano = date.today().year
for pess in range(1, 5):
    print('{} {}ª PESSOA {}'.format('-' * 5, pess, '-' * 5))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    totid += idade / 4
    if pess == 1 and sexo == 'M':
        maior = idade
        nmaior = nome
    if sexo == 'M' and idade > maior:
        maior = idade
        nmaior = nome
    if sexo == 'F' and idade < 20:
        mulher += 1
print(f'A média de idade do grupo é de {totid} anos')
print(f'O homem mais velho tem {maior} anos e se chama {nmaior}')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos')
