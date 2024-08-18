#Essa aula foi focada em aprender diferentes tipos de Operações Aritméticas e algumas maneiras de tratar o output de cada entrada de dados 

#Operações Aritméticas

#Tipos de operadores aritméticos:

'''
# Para testar se uma coisa é igual a outra ou obter o resultado de uma operação se utiliza: ==

+: Adição         - 5+2 == 7           **: Potência         - 5**2 == 25
-: Subtração      - 5-2 == 5           //: Divisão inteira  - 5//2 == 2
*: Multiplicação  - 5*2 == 10           %: Resto da Divisão - 5%2  == 1
/: Divisão        - 5/2 == 2.5       

Ordem de Precedência:
1) ()
2) ** - Potência
3) *, /, // e % - Resolver por ordem de 'chegada'
4) + e -

Cálculo de Raíz:

Raíz Quadrada: **(1/2) - Ex: 81**(1/2) == 9
Raíz Cubica:   **(1/3) - Ex: 27**(1/3) == 3
'''

#Curiosidades
print('Oi'+'Olá')
print('João'*10)
print('O Rato Roeu a Roupa do Rei de Roma'*20)


#Exercícios de Operações Aritméticas 

num1  = int(input('Digite um número: '))
num2  = int(input('Digite outro número: '))

soma  = num1 + num2
multi = num1 * num2
d     = num1 / num2 # Para limitar o número de casas decimais resultantes da divisão, utilizar: :.2f - O número antecessor do 'f' dita o número de casas decimais depois da vírgula  
di    = num1 // num2
p     = num1 ** num2

print('A soma desses valores é: {}, a multiplicação desses valores é {}.\nA divisão desses valores é {:.3f}.'.format(soma, multi, d), end=(' ')) #end=() é usado para juntar linhas e \n para quebrar linhas
print('A divisão inteira desses valores é {} e a potênciação desses valore é {}.'.format(di, p))
print('A soma desses valores é: {}'.format(num1 + num2)) #Posso utilizar esse formato de programação  sem variável caso o resultado dessa soma não seja mais necessário em nenhum local do código ou seja só necessário para printar na tela

#DESAFIOS DA AULA 07 - DESAFIO 5
'Faça um progra,a que leia um número inteiro e mostre a tela o seu sucessor e antecessor.'

num = int(input('Digite um número: '))
print('O antecessor do número {} é {}, e seu sucessor respectivamente é o número {}.'.format(num, num - 1, num + 1) )

# DESAFIO 6
'Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada'

num = int(input('Digite um valor: '))
print('O dobro de {} é {}, o seu triplo é {}, e sua raíz quadrada é {:.2f}.'.format(num, num * 2, num* 3, num ** (1/2)))

#DESAFIO 7
'Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média'


nota1 = float(input('Digite uma nota de 0 a 10: '))
nota2 = float(input('Digite outra nota de 0 a 10: '))
media = (nota1 + nota2) / 2
print(f'Com base nas suas duas notas, respectivamente {nota1} e {nota2}, sua média é de: {media:.2f}') #É possível se utilizar esse tipo de impressão, colocando f na frente das '' e ordenando cada chave com uma váriavel


#DESAFIO 8 
'Escreva um programa que eia um valor em metros e o exiba convertido em centímetros e milímetros'

metros = int(input('Digite a quantidade de metros que você gostaria de percorrer: '))

km = metros / 1000
hm = metros / 100
decam = metros / 10
deci = metros * 10 
cent = metros * 100
mili = metros * 1000

print(f'\nSua distância percorrida de {metros} metro(s) é equivalente a:\n'
    f'\n{deci} Decímetro(s);'
    f'\n{cent} Centímetros(s);'
    f'\n{mili} Milímetro(s);'
    f'\n{decam} Decâmetro(s);'
    f'\n{hm} Hectômetro(s);'
    f'\n{km} Quilômetro(s);')
    
#DESAFIO 9
'Faça um programa que leia um número inteiro qualquer e mostre sua tabuada na tela'

num = int(input('Digite um número para obter sua tabuada: '))

print(f'\n ***** Tabuada do {num}! *****\n')
print(f'{num} x {1:2} = {num * 1}')
print(f'{num} x {2:2} = {num * 2}')
print(f'{num} x {3:2} = {num * 3}')
print(f'{num} x {4:2} = {num * 4}')
print(f'{num} x {5:2} = {num * 5}')
print(f'{num} x {6:2} = {num * 6}')
print(f'{num} x {7:2} = {num * 7}')
print(f'{num} x {8:2} = {num * 8}')
print(f'{num} x {9:2} = {num * 9}')
print(f'{num} x {10:2} = {num * 10}')
print('\n***** Fim! *****')


#DESAFIO 10 
'Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27'

'Cotação do Dolar - Dia da Cotação: 02/07/2024'
Real = float(input("Quantos reais você possui? R$"))
Dolar = Real / 5.66
print(f"Com R${Real:.2f} você consegue comprar: US${Dolar:.2f}")

'Cotação do Euro - Dia da Cotação: 02/07/2024'
Real = float(input("Quantos reais você possui? R$"))
Euro = Real / 6.08
print(f"Com R${Real:.2f} você consegue comprar: EUR€{Euro:.2f}")

'Cotação do Iene Japonês - Dia da Cotação: 02/07/2024'
Real = float(input("Quantos reais você possui? R$"))
Iene = Real / 0.035
print(f"Com R${Real:.2f} você consegue comprar: JPY¥{Iene:.2f}")

'Cotação do Bitcoin - Dia da Cotação: 02/07/2024'
Real = float(input("Quantos reais você possui? R$"))
Bit = Real / 355.881
print(f"Com R${Real:.2f} você consegue comprar: BIT₿{Bit:.2f}")


#DESAFIO 11
'Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m².'

Alt = float(input("Qual a altura da parede? "))
Larg = float(input("Qual a largura da parede? "))
Area = Alt * Larg
Tinta = Area / 2
print(f"A sua parede tem largura de {Larg}m e altura de {Alt}m. \nA área total da parede é de: {Area:.2F}m². E a quantidade de tinta necessária para pintar essa parede é de {Tinta:.1f} Litros")


#DESAFIO 12 
'Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto, com o 8% e juros caso parcelado e 10% de desconto à vista.'

preço= float(input("Digite um valor imaginário de um produto imaginário: R$"))
desconto = preço - (preço * 5 /100)
print(f"O valor original do produto era de R${preço:.2f}, agora com o desconto de 5% passou a ser o valor de R${desconto:.2f}.")
produto = float(input("Digite o preço de um produto novamente: R$"))
parcelado = produto + (produto * 8 / 100)
a_vista = produto - (produto * 10 / 100)
print(f"Seu produto custa: R${produto:.2f} \nCaso queira pagá-lo em parcelas seu preço será reajustado com 8% de juros, chegando ao valor de R${parcelado:.2f} \nCaso queira pagá-lo à vista, seu preço será reajustado com 10% de desconto, chegando ao valor de R${a_vista:.2f} ")


#DESAFIO 13

'Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.'

salario = float(input("Digite seu atual salário: R$"))
aumento = salario + (salario * 15 / 100)
print(f"Seu antigo salário de R${salario:.2f}, com um aumento de 15%, foi para R${aumento:.2f}")


#DESAFIO 14
'Escreva um programa que converta uma temperatura digitada em graus Celsius para a sua temperatura equivalente em Fahrenheit, depois faça o inverso e logo após faça celsius para kelvin.'

cel = float(input("Quantos graus Celsius está fazendo na sua cidade hoje? "))
fah = cel * 1.8 + 32
print(f"Sua temperatura local de: {cel:.1f}°C, convertida para Fahrenheit é de: {fah:.1f}°F")
fah_p_cel = (fah - 32) / 1.8
cel_p_kelvin = cel + 273.15
fah_p_kelvin = (fah - 32) / 1.8 + 273.15
print(f"Por curiosidade, Fahrenheit para Celsius é {fah_p_cel:.1f}°C, de Celsius para Kelvin é {cel_p_kelvin:.1f}°K e de Fahrenheit para Kelvin é {fah_p_kelvin:.1f}°K.")

#DESAFIO 15
'Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.'

km = float(input("Quantos Km você percorreu com o carro? "))
dias = int(input("Por quantos dias você alugou o carro? "))
diária = dias * 60
rodagem = km * 0.15
total = diária + rodagem
print(f"Com esses resultados, a diária do veículo custará R${diária:.2f}, a sua rodagem custará R${rodagem:.2f} e somando todos os custos, o valor final será R${total:.2f}.")
