'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>> Qual é sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'O resultado de {n1} + {n2} é {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'O resultado de {n1} x {n2} é {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior é {n1}')
        elif n1 < n2:
            print(f'Entre {n1} e {n2}, o maior é {n2}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao > 5:
        print('Opção inválida. Tente de novo!')
    print('=-=' * 10)
    sleep(1.5)
print('Finalizando...')
sleep(1.5)
print('Fim do programa. Volte sempre!')
