# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_do_mb = float(input('qual o tamanho do arquivo? '))
velocidade = float(input('qual a velocidade da sua internet? '))
print('o tempo que levara é: %.0f minutos'%((tamanho_do_mb/velocidade)* 60))
