
#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input('insira sua altura'))

print('seu peso ideal é', 72.7 * altura - 58)



# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas

#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = int(input('Escolha: 1- homem / 2- mulher'))
h = float(input('Digite sua altura'))
if sexo == 1:
    print('seu peso ideal é',72.7* h - 58 )
elif sexo == 2:
        print('seu peso ideal é',62.1*h -  44.7 )