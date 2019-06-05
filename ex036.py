#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}.'.format(casa, anos, prestação))

if prestação <= minimo:
    print('\033[1;32mEmpréstimo ACEITO!\033[m')

else:
    print('\033[1;31mEmpréstimo NEGADO!\033[m')
