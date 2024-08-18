#Nesta aula aprenderemos sobre estrutura de comandos baseadas em possibilidades e condições.

#CONDIÇÃO -> É feito por duas estruturas de blocos de códigos, nas quais existe apenas uma possibilidade para utilização. Nunca serão executados dois blocos ao mesmo tempo

#Estrutura básica de uma condição: 

'''
entrade de dados = xxxxx

if condição1:            -> Quando a estrutura condicional so conter um if, ela se torna uma estrutura condicional simples 
    
    bloco de código

else:                    -> Quando um if possuir um else, a estrutura condicional se torna uma estrutura condicional composta

    bloco de código

                         -> Códigos alinhados a esquerda sempre serão executados, códigos identados, podem ou não ser exceutados
'''

#Exemplo de código utilizando condição

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
#O código também poderia ser feito com uma condição simplificada: 
#print("Você foi bem!" if media >= 6 else "Estude um pouco mais!")
if media >= 6:
    print(f"Sua média foi: {media}, você foi bem!")
else:
    print(f"Sua media foi: {media}, estude um pouco mais!")


#DESAFIOS DA AULA 10

#DESAFIO 28
'Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'

from random import randint
from time import sleep
numero_pensado = randint(0,5) #Faz o computador 'pensar'

adivinha = int(input("Digite o número que você acha que o computador está pensando entre 0 e 5: ")) #Jogador tenta adivinhar o número

print("Processando Dados...")
sleep(4) #A função sleep faz o computador 'dormir' por um tempo determinado

if adivinha == numero_pensado:
    print(f"Parabéns, Você acertou! O número pensado foi: {numero_pensado}")

else:
    print(f"Você errou! O número pensado foi: {numero_pensado}")

print("Fim!")


#DESAFIO 29
'Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'

from time import sleep
print("Você foi viajar para uma cidade utilizando seu carro.")
vel = float(input("Não percebeu um radar a frente e passou em uma velocida de Km/h: "))

if vel > 80: 
    multa = (vel - 80) * 7
    print("Você ultrapassou o limite de 80km/h!")
    sleep(3)
    print("Processando a multa...")
    sleep(3)
    print(f"Você foi multado por excesso de velocidade, e terá que pagar: R${multa:.2f}")

else:
    print("Fique tranquilo! Você ão será multado.")

sleep(3)
print("Dirija sempre com segurança e tenha um Bom Dia!")


#DESAFIO 30
'Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'

from time import sleep

num = int(input("Digite um número: "))
teste = num % 2

print("Processando Dados...")
sleep(2)
if teste == 1:
    print(f"O número: {num} é ímpar!")

else:
    print(f"O número: {num} é par!")

sleep(2)
print("Fim!")


#DESAFIO 31
'Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'

print("Você saiu para uma viagem de férias com sua família")
km = float(input("Digite quantos quilometros você percorrerá nessa viagem: "))

if km <= 200:
    custo = km * 0.50
    print(f"O preço da passagem será de: R${custo:.2f}")

else:
    custo = km * 0.45
    print(f"O custo da passagem será de: R${custo:.2f} ")

print("Tenha uma Boa Viagem!")


#DESAFIO 32
'Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'

from datetime import date

ano = int(input("Digite um ano para saber se ele é bissexto ou não. Para analisar o ano configurado de sua máquina, digite 0: "))

if ano == 0:
    ano = date.today().year #Acessa a data anual configurada no computador executando o código

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #Tem que ser multiplo de 4 e não divisivel por 100 ou multiplo de 400
    print(f"O ano de {ano} é Bissexto!")

else:
    print(f"O ano de {ano} não é Bissexto!")
    

#DESAFIO 33
'Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

#Testando os menores valores
menor = num1
if num2 < num1 and num2 < num3: 
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3

#Testando os maiores valores
maior = num1 
if num2 > num3 and num2 > num1:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f"O número {maior} é o maior número.")
print(f"O número {menor} é o menor número.") 


#DESAFIO 33
'Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%'

from time import sleep

salario = float(input("Digite o valor de seu salário em R$: "))

print("Processando aumento salarial...")
sleep(2)

if salario <= 1250.00:

    aumento = (salario * 1.15) #1.15 significa uma parte inteira do salario mais 15% dele 
    print(f"Seu salário de R${salario:.2f} com um aumento de 15%, passou a ser de R${aumento:.2f}.")

else:

    aumento = (salario * 1.10) 
    print(f"Seu salário de R${salario:.2f} com um aumento de 10%, passou a ser de R${aumento:.2f}.")
    
print("Bom Trabalho!")


#DESAFIO 35
'Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'

seg1 = float(input("Digite o comprimento do primeiro segmento: "))
seg2 = float(input("Digite o comprimento do segundo segmento: "))
seg3 = float(input("Digite o comprimento do terceiro segmento: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print(f"Os comprimentos: {seg1}, {seg2}, {seg3} podem formar um triângulo.")

else:
    print(f"Os segmentos {seg1}, {seg2}, {seg3} não podem formar um triângulo.")

