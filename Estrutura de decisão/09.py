# Faça um programa que leia três números e mostre-os em ordem decrescente:

n1 = n2 = n3 = 0

n1 = int(input('Digite um numero: \n'))
n2 = int(input('Digite um numero: \n'))
n3 = int(input('Digite um numero: \n'))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(f'{n1}>={n2}>={n3}')
    else:
        print(f'{n1}>={n3}>={n2}')
elif n2 >= n1  and n2 >= n3:
    if n1 >= n3:
        print(f'{n2}>={n1}>={n3}')
    else:
        print(f'{n2}>={n3}>={n1}')
else:
    if n1 >= n2 :
        print(f'{n3}>={n1}>={n2}')
    else:
        print(f'{n3}>={n2}>={n1}')




    



