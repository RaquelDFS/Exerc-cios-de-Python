# Faça um programa que verifique se uma letra digitada é vogal ou consoante.
vogais = ('a','A','e','E','i','I','o','O','u','U')
d = input('Digite uma letra: \n')

if d in vogais:
    print(f'{d} é vogal')
else:
    print(f'{d} é consoante')
