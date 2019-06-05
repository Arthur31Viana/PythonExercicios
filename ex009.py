# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

cores = {'limpa': '\033[m',
         'branco': '\033[7;30m',
         'verde': '\033[7;32m',
         'letrabranca': '\033[1;30m'}

n = int(input('\033[1;30mDigite um número para ver a sua tabuada:\033[m '))

print('{}{:=^12}{} \n{}{}{} X 1 = {}{}{} \n{}{}{} X 2 = {}{}{} \n{}{}{} X 3 = {}{}{} \n{}{}{} X 4 = {}{}{} \n{}{}{} X 5 = {}{}{} \n{}{}{} X 6 = {}{}{} \n{}{}{} X 7 = {}{}{} \n{}{}{} X 8 = {}{}{} \n{}{}{} X 9 = {}{}{} \n{}{}{} X 10 = {}{}{} \n{}{:=^12}{}'.format(cores['letrabranca'], '', cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], n * 1, cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], n * 2, cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], n * 3, cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], n * 4, cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], n * 5, cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], n * 6, cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], n * 7, cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], n * 8, cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], n * 9, cores['limpa'], cores['branco'], n, cores['limpa'], cores['verde'], n * 10, cores['limpa'], cores['letrabranca'], '', cores['limpa']))
