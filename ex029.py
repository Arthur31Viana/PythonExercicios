#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velo = float(input('Qual é a velocidade atual do carro? '))
if velo <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é 80Km/h \nVocê deve pagar uma multa de R${:.2f}!'.format((velo - 80) * 7))
