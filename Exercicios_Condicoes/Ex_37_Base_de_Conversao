'''
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

num = int(input("Escreva um número inteiro: "))
decisao = int(input("Digite '1' para conversão Binária,\n"
                    "Digite '2' para conversão octal,\n"
                    "Digite '3' para conversão hexadecimal.\n"
                    "O que deseja? "))

binario = bin(num)
octal = oct(num)
hexa = hex(num)

if decisao == 1:
    print(f"A representação de {num} em Binário é {binario[2:]}.")

elif decisao == 2:
    print(f"A representação de {num} em Octal é {octal[2:]}.")

elif decisao == 3:
    print(f"A representação de {num} em Hexadecimal é {hexa[2:]}.")

else:
    print("Opção Inválida.")
