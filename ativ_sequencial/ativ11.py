#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   salário bruto.
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.
#   calcule os descontos e o salário líquido, conforme a tabela abaixo

salario = float(input('digite o quanto voce ganha por hora: '))
horas_trabalhdas = int(input('quantas horas voce trabalhou?: '))

salario_total = salario * horas_trabalhdas
ir = salario_total * 0.11
inss = salario_total * 0.08
sindicato = salario_total * 0.05

print ('+ Salário Bruto : R$ %.2f' %salario_total)
print('- IR: R$ %.2f' %ir )
print('- INSS: R$ %.2f' %inss)
print('- sindicado: R$ %.2f' %sindicato)
print ('= Salário Liquido : R$ %.2f' %(salario_total - ir - inss -sindicato ))


