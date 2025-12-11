#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
f = float(input('Digite a temperatura em Fahrenheit:'))
c = 5*((f-32) / 9)
print(f'{f} graus Fahrenheit é igual a {c} graus Celsius')