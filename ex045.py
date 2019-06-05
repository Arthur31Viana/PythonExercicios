#Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep
print('''Suas opções:
- PEDRA
- PAPEL
- TESOURA''')
jogador = str(input('Digite a sua jogada? ')).upper().strip()
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(opcoes)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 20)
print('O computador jogou {}'.format(pc))
print('O jogador jogou {}'.format(jogador))
print('-=' * 20)

if pc == 'PEDRA' and jogador == 'PAPEL' or pc == 'TESOURA' and jogador == 'PEDRA' or pc == 'PAPEL' and jogador == 'TESOURA':
    print('\033[1;32mPARABÉNS, VOCÊ VENCEU!\033[m')

elif pc == 'PEDRA' and jogador == 'TESOURA' or pc == 'PAPEL' and jogador == 'PEDRA' or pc == 'TESOURA' and jogador == 'PAPEL':
    print('\033[1;31mO COMPUTADOR VENCEU!\033[m')

else:
    print('\033[1;33mESSA BATALHA ESTÁ ACIRRADA! TENTE NOVAMENTE!\033[m')
