#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
anoatual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = anoatual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, anoatual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!.')

elif idade < 18:
    saldo = 18 - idade
    ano = anoatual + saldo
    print('''Ainda faltam {} anos para o alistamento. 
Seu alistamento será em {}.'''.format(saldo, ano))

elif idade - 18 == 1:
    saldo = idade - 18
    ano = anoatual - saldo
    print('''Você já deveria ter se alistado há {} ano.
Seu alistamento foi em {}.'''.format(saldo, ano))

else:
    saldo = idade - 18
    ano = anoatual - saldo
    print('''Você já deveria ter se alistado há {} anos.
Seu alistamento foi em {}.'''.format(saldo, ano))
