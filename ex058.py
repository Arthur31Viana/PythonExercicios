#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 19)

pc = randint(0, 10)
acertou = False
cont = 0
while not acertou:
    n = int(input('Em que número eu pensei? '))
    cont += 1
    print('PROCESSANDO...')
    sleep(2)
    if pc == n:
        acertou = True
    else:
        if n < pc:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez')

print(f'Acertou com {cont} tentativas. Parabéns!')
