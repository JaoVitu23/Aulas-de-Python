"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

v1 = float(input("Digite um Valor: "))
v2 = float(input("Digite outro Valor: "))


opcao = 0
while opcao != 5:
    opcao = int(input('O que deseja realizar a seguir?\n'
                  "[ 1 ] Somar\n"
                  "[ 2 ] Subtrair\n"
                  "[ 3 ] Multiplicar\n"
                  "[ 4 ] Divisão\n"
                  "[ 5 ] Maior\n"
                  "[ 6 ] Novos Números\n"
                  "[ 7 ] Sair do Pograma\n"
                  "O que deseja? "))
    
    if opcao == 1:
        soma = v1 + v2
        print(f'A soma dos dois números é {soma}')
        sleep(2)

    elif opcao == 2:
        subtrair = v1 - v2
        print(f'O resultado da subtração entre {v1} e {v2} é de {subtrair}')
        sleep(2)


    elif opcao == 3:
        multi = v1 * v2
        print(f'A multiplicação dos valores é igual a {multi}')
        sleep(2)
    
    elif opcao == 4:
        divisao = v1 / v2
        print(f'A divisã de {v1} por {v2} é igual {divisao}')
        sleep(2)

    elif opcao == 5:
        if v1 > v2: print(f'O Valor {v1} é o maior, e o valor {v2} é o menor')
        if v2 > v1: print(f'O Valor {v2} é o maior, e o valor {v1} é o menor')
        sleep(2)

    elif opcao == 6:
        v1 = float(input("Digite um novo número: "))
        v2 = float(input("Digite outro novo número: "))
        sleep(2)

    elif opcao == 7:
        print('Obrigado por utilizar o programa!')
        break

    else:
        print('Opção Inválida!')
        sleep(2)