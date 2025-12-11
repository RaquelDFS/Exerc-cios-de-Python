#Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula: Megabytes = Gigabytes * 1024

gb = float(input('Digite o valor em Gigabytes: '))
print(f'{gb} Gigabytes é {gb*1024} Megabytes')