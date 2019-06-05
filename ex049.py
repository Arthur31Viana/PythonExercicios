#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('{:=^42}'.format(' TABUADA V2.0 '))
n = int(input('Digite um número para saber a sua tabuada: '))
p = str(input('Quer Adição, Subtração, Multiplicação ou Divisão? ')).strip().upper()
opcões = ['ADIÇÃO', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO', 'DIVISÃO']
for tabuada in range(1, 11):
    soma = n + tabuada
    subt = n - tabuada
    mult = n * tabuada
    div = n / tabuada
    if p == 'ADIÇÃO':
        adic = '+'
        print('{} {} {} = {}'.format(n, adic, tabuada, soma))
    elif p == 'SUBTRAÇÃO':
        sub = '-'
        print('{} {} {} = {}'.format(n, sub, tabuada, subt))
    elif p == 'MULTIPLICAÇÃO':
        mul = 'X'
        print('{} {} {} = {}'.format(n, mul, tabuada, mult))
    elif p == 'DIVISÃO':
        divi = '/'
        print('{} {} {} = {:.2f}'.format(n, divi, tabuada, div))
    else:
        print('Escolha incorreta, tente novamente!')
