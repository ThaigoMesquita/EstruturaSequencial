#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   o produto do dobro do primeiro com metade do segundo .
#   a soma do triplo do primeiro com o terceiro.
#   o terceiro elevado ao cubo.
num1 = int(input('insira um numero inteiro: '))
num2 = int(input('insira um numero inteiro: '))
num3 = float(input('insira um numero real: '))

print('soma:',((2*num1) * (num2/2)))
print('produto',(3*num1) + num3)
print('cubo', num3**3)