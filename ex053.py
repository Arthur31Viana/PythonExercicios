#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
juntar = ''.join(palavra)
inverso = ''
for letra in range(len(juntar) - 1, -1, -1):
    inverso += juntar[letra]
if juntar == inverso:
    print('Ela é um PALINDROMO!')
else:
    print('Ela NÃO é um PALINDROMO!')
print('O inverso da palavra digita é {}'.format(inverso))
