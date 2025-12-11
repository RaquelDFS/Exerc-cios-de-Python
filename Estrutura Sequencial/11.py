# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

# O produto do dobro do primeiro com metade do segundo .
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

n1 = n2 = 0
n3 = 0.0

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))

print('O produto do dobro do primeiro com metade do segundo:', (n1*2)*(n2/2))
print('A soma do triplo do primeiro com o terceiro', (n1*3)+n3)
print('O terceiro elevado ao cubo:', n3**3)
