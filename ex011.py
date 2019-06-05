#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('\033[1;30mLargura da parede:\033[m '))
a = float(input('\033[1;30mAltura da parede:\033[m '))
cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'azul':'\033[1;34m'}

área = l * a
print('Sua parede tem a dimensão de {}{}{}X{}{}{} e sua área é de {}{}{}m². \nPara pintar essa parede, você precisará de {}{}{}L de tinta.'.format(cores['vermelho'], l, cores['limpa'], cores['vermelho'], a, cores['limpa'], cores['azul'], área, cores['limpa'], cores['verde'], área/2, cores['limpa']))
