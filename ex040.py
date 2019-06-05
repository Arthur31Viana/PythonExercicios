'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

n1 = float(input('\033[1;30mPrimeira nota:\033[m '))
n2 = float(input('\033[1;30mSegunda nota:\033[m '))
média = (n1+n2) / 2

print('Tirando \033[1;30m{:.1f}\033[m e \033[1;30m{:.1f}\033[m, a média do aluno é \033[1;30m{:.1f}\033[m'.format(n1, n2, média))
if média >= 7.0:
    print('O aluno está \033[1;32mAPROVADO!\033[m')
elif média >= 5.0 or média <= 6.9:
    print('O aluno está em \033[1;33mRECUPERAÇÃO!\033[m')
else:
    print('O aluno está \033[1;31mREPROVADO!\033[m')
