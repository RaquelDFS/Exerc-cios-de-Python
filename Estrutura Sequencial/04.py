#Faça um programa que peça as 4 notas bimestrais e mostre a média.

media = n1 = n2 = n3 = n4 = 0.0
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1+n2+n3+n4)/4
print(f'Sua média foi de {media}')
