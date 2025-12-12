# Faça um programa que leia três números e mostre o maior deles:

n1 = n2 = n3 = 0

n1 = int(input('Digite um numero: \n'))
n2 = int(input('Digite um numero: \n'))
n3 = int(input('Digite um numero: \n'))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)


