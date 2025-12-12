# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

ganho = float(input('Quanto você ganha por hora?: '))
horas = float(input('Quantas horas você ytabalhou este mês?: '))

salario_bruto = ganho * horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato
print(f'Seu salário Bruto é de: R${round(salario_bruto,2)}')
print(f'Seu IR é de: R${round(ir,2)}')
print(f'Seu INSS é de: R${round(inss,2)}')
print(f'Seu Sindicato é de: R${round(sindicato,2)}')
print(f'O que faz seu salário líquido ser de: R${round(salario_liquido,2)}')