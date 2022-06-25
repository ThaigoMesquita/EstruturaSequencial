#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
temp = float(input('digite a temperatura atual em Fahrenheit: '))
print('a temperatura em Celsius %.2f' %(9* temp /5 + 32))

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit

tc = float(input('Informe a temperatura em ºC: '))

tf = ((tc*(9/5))+32)

print('A temperatura de {} ºC corresponde a {} ºF!'.format(tc, tf))
