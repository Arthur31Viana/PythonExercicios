#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

cores = {'limpa':'\033[m',
         'branco':'\033[1;40m',
         'vermelho':'\033[1;30;41m',
         'verde':'\033[1;30;42m',
         'amarelo':'\033[1;30;43m',
         'azul':'\033[1;30;44m',
         'roxo':'\033[1;30;45m',
         'verdeazulado':'\033[1;30;46m'}

m = float(input('\033[1;30mUma distância em métros:\033[m '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m * 0.1
hm = m * 0.01
km = m * 0.001

print('A medida de {}{}m{} corresponde a \n{}{}km{} \n{}{}hm{} \n{}{:.1f}dam{} \n{}{:.0f}dm{} \n{}{:.0f}cm{} \n{}{:.0f}mm{}'.format(cores['branco'], m, cores['limpa'], cores['vermelho'], km,cores['limpa'], cores['verde'], hm, cores['limpa'], cores['amarelo'], dam, cores['limpa'], cores['azul'], dm, cores['limpa'], cores['roxo'], cm, cores['limpa'], cores['verdeazulado'], mm, cores['limpa']))
