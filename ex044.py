'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

print('\033[1;30m{:=^40}\033[m'.format(' LOJAS VIANA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] Em 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preço - (preço*10/100)

elif opcao == 2:
    total = preço - (preço*5/100)

elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))

elif opcao == 4:
    quant = int(input('Quantas parcelas? '))
    total = preço + (preço*20/100)
    parcela = total / quant
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(quant, parcela))

else:
    total = 0
    print('\033[1;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
