#Nesta aula iremos aprender a manipular cadeias de texto/caracteres

frase = 'Curso em Vídeo Python' #O computador guarda as informações de String como se fossem microespaços na memória

#OPERAÇÃO COM FATIAMENTO - É a operação de conseguir pegar pedaços de uma string

print(frase[9]) #Pega a letra referente a posição numérica dela
print(frase[9:13]) #Mostra as letras referentes do 9 ao 13, porém o último valor não entra na contagem, na prática, será mostrado apenas os valores do 9 ao 12
print(frase[9:21:2]) #Vai do 9 ao 21 pulando de 2 em 2 caracteres
print(frase[:5]) #Nesse formato você não especifica o começo, mas delimita o fim
print(frase[15:]) #Delimita o começo, mas não delimita o fim
print(frase[9::3]) #Delimita o começo, não delimita o fim e pula os caracteres de 3 em 3

#OPERAÇÃO COM ANÁLISE - É saber algumas informações sobre a própria string

print(len(frase)) #Conta o comprimento da frase
print(frase.count('o')) #Conta quantas vezes a letra pedida se repete. Diferencia letras minusculas de maiusculas
print(frase.count('o',0,13)) #Faz uma contagem de letra com a fatiação incluida
print(frase.find('deo')) #Mostra onde começou o elemento requisitado
print(frase.find('Android')) #Quando requisitado um elemento que não existe na string, o programa retornará -1
print('Curso' in frase) #In retorna uma operação de True or False, se existe ou não os caracteres dentro da string


#OPERAÇÃO DE TRANSFORMAÇÃO - É a possibilidade de mudar uma string atraves de alguns metodos

print(frase.replace('Python', 'Android')) #Troca a palavra desejada por outra
print(frase.upper()) #Transforma todas as letras minusculas em maiusculas
print(frase.lower()) #Transorma todas as letras maiusculas em minusculas
print(frase.capitalize()) #Só primeiro caractere de uma string vai ser tranformado em letra maiuscula
print(frase.title()) #Analisa quantas palavras tem a string, e transformará cada começo de palavra em letra maiuscula

frase1 = '   Aprendendo Python    '
print(frase1.strip()) #Remove os espaços excedentes
print(frase1.rstrip()) #Remove os espaços excedentes na direita
print(frase1.lstrip()) #Remove os espaços excedentes na esquerda

#OPERAÇÃO COM DIVISÃO - É a possibilidade de dividir a string

print(frase.split()) #Divide a string considerando os espaços, criando uma lista com essa cadeia de caracteres

#OPERAÇÃO COM JUNÇÃO - A possibilidade de juntar a string

print('_'.join(frase.split())) #Para a função join não adicionar caracteres entre as letras, usar a função split juntamente


#CURIOSIDADE DE FUNCIONALIDES

#Para mostrar um texto longo na tela sem precisar digitar print em todas as linhas, basta utilizar aspas triplas """  """
print("""Python é uma linguagem de programação de alto nível, 
interpretada de script, imperativa, orientada a objetos, funcional, 
de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.""")


print(frase.upper().count('O')) #Utilizando a função Upper junto com count para contar o "O" Maiusculo na string

dividido = frase.split()
print(dividido[2][3]) #Mostra a terceira letra da string encontrada na lista determindada 

# O [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante.

#DESAFIOS DA AULA 9 

#DESAFIO 22
'Crie um programa que leia o nome de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas; Quantas letras ao todo (Sem considerar os espaços); Quantas letras tem o primeiro nome.'

nome = str(input("Digite seu nome: ")).strip()
maiuscula = nome.upper()
minuscula = nome.lower()
cont_sem_espaço = len(''.join(nome.split()))
primeiro_nome = nome.split()
print(f"Seu nome em letras maiúsculas é: {maiuscula}.")
print(f"Seu nome em letras minúsculas é: {minuscula}.")
print(f"A quantidade de caracteres em seu nome sem contar os espaços é de: {cont_sem_espaço}. ")
print(f"Seu primeiro nome é {primeiro_nome[0]} e tem {len(primeiro_nome[0])} letras")

#DESAFIO 23
'Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'

numero = int(input("Digite um número de 0 a 9999: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f"Analisando o número {numero}\n"
      f"Unidade: {u}\n"
      f"Dezena: {d}\n"
      f"Centena: {c}\n"
      f"Milhar: {m}")

#DESAFIO 24
'Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'

cidade = str(input("Digite o nome da cidade que você nasceu: ")).strip().title().split()
teste = "Santo" in cidade[0]
print(f"Sua cidade começa com Santo: {teste}")


#DESAFIO 25
'Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'

nome = str(input("Digite seu nome: ")).strip().upper()
teste = "SILVA" in nome
print(f"Seu nome possuí 'Silva': {teste}")


#DESAFIO 26
'Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'

frase = str(input("Digite uma frase: ")).strip().upper()
reps = frase.count('A')
primeira = frase.find('A') + 1
ultima = frase.rfind("A") + 1
comprimento = len(frase)
print(f"O comprimento da frase é de: {comprimento} caracteres;\n"
      f"Quantas vezes o 'A' se repete: {reps};\n"
      f"Qual posição aparece o primeiro 'A': {primeira};\n"
      f"Qual posição aparece o último 'A': {ultima};")

#DESAFIO 27
'Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'
nome = str(input("Digite seu nome: ")).strip().split()
print(f"{nome[0]}")
print(f"{nome[-1]}")
