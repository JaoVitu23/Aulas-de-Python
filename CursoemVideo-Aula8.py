#Esta aula será focada em aprender a trabalhar com Módulos e importações


#IMPORTAÇÕES E BIBLIOTECAS
'''Para saber quais as bibliotecas de importações que eu posso fazer, só acessar o site oficial de Python, o Python.org e clicar em Library Reference'''

##import math -> Esse tipo de importação faz uma importação geral das funções dessa pasta dentro da pasata em que o código está localizado

from math import sqrt, floor #Já esse tipo de importação, faz uma importação específica para a pasta, permitindo usar uma função diretamente, sem precisar fazer nenhuma referência. 
#Ex: 
num = int(input("Digite um número: "))
raiz = sqrt(num)
print(f"A raiz de {num}, é igual a {floor(raiz)}.") #Caso seja necessário arredondamentos, utilizar as funções: 'math.ceil' para fazer um arredondamento para cima, e para arredindar para baixo basta utilizar 'math.floor'

import random
num = random.randint(1, 100) #Se eu utilizar random.random, está função ra gera um núm aleatório entre 0 e 1.
#random.randint gera um núm inteiro entre os números que você delimitar
print(num)

#Curiosidade 
import emoji
print(emoji.emojize("Sou maneiro :smiling_face_with_sunglasses:"))


#DESAFIOS DA AULA 8

#DESAFIO 16
'Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira'

from math import trunc #Podemos usar a função floor também.

num = float(input("Digite um valor: "))
int = trunc(num)
print(f"A parte inteira de {num} é {int}.")


#DESAFIO 17
'Faça um programa que leia o comprimento do cateto oposto e do cateto adjcaente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa'

from math import hypot

co = float(input("Digite o comprimento do Cateto Oposto: "))
ca = float(input("Digite o comprimento do Cateto Adjacente: "))
hipo = hypot(co, ca)
print(f"A hipotenusa do triângulo retângulo é: {hipo:.2f}")


#DESAFIO 18
'Faça um programa que leia um ângulo qualquer e mostre o valor na tela o valor do seno, cosseno e tangente desse ângulo'

import math #Posso apenas importar as funções que estou utilizando, como: 'radians', 'sin,' 'cos' e 'tan'
ang = int(input("Digite o valor de um ângulo: "))
seno = math.sin(math.radians(ang))
print(f"O seno do ângulo de {ang}, é: {seno:.2f}.")
cos = math.cos(math.radians(ang))
print(f"O cosseno do ângulo de {ang}, é: {cos:.2f}.")
tang = math.tan(math.radians(ang))
print(f"A tangente do ângulo de {ang}, é: {tang:.2f}")


#DESAFIO 19 
'Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'

from random import choice

n1 = str(input("Escreva o nome do primeiro aluno: "))
n2 = str(input("Escreva o nome do segundo aluno: "))
n3 = str(input("Escreva o nome do terceiro aluno: "))
n4 = str(input("Escreva o nome do quarto aluno: "))
aluno = [n1, n2 , n3, n4] #No python, uma lista fica entre colchetes
escolhido = choice(aluno)
input(f"O aluno escolhido escolhido foi: {escolhido}")

#DESAFIO 20
'O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'


from random import shuffle

nome1 = str(input("Escreva o nome do primeiro aluno: "))
nome2 = str(input("Escreva o nome do segundo aluno: "))
nome3 = str(input("Escreva o nome do terceiro aluno: "))
nome4 = str(input("Escreva o nome do quarto aluno: "))
lista_nomes = [nome1, nome2, nome3, nome4]
shuffle(lista_nomes)
print(lista_nomes)


#DESAFIO 21
'Faça um programa em Python que abra e reproduza o aúdio de um arquivo mp3'

import pygame 

pygame.init()
pygame.mixer.music.load('musica_teste.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()