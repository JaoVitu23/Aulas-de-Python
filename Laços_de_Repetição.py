#Nessa aula, aprenderemos sobre estruturas de laços de repetição

#EXEMPLOS

for c in range(0, 3): #Estrutura para laço de repetição, os números detro do parenteses delimitam quantas repetições serão realizadas.
    print(c)          #Lembrando que o Python não conta de 0 a 3, como mostrado, mas sim 0 - 1 - 2, desconsiderando o último número da contagem
print("Tchau!")

for j in range(5, 0, -1): #Contagem regressiva
    print(j)
print("Programa encerrado!")

for k in range(0, 11, 2): #De 0 a 10, mas pulando de 2 em 2
    print(k)
print("Isso ai!")


contagem = int(input("Digite um número: ")) #Criando uma contagem de números baseada em uma opção do usuário

for contagem in range(0, contagem+1):
    print(contagem)
print("Acabou")


i = int(input("Inicio: ")) #Definindo Começo da contagem
f = int(input("Fim: "))    #Definindo Fim da contagem
p = int(input("Passo: "))  #Definindo Passo da contagem
for c in range(i, f+1, p):
    print(c)
print("Fim")


soma = 0 #Inicializar a variável com 0 garante que você tenha um ponto de partida para a soma. Isso evita erros e garante que a soma seja calculada corretamente.
for c in range(0, 4,):
    num = int(input("Digite um valor: "))
    soma += num #Isso é igual a soma = soma + num, porém de forma reduzida e simplificada
print(f"A soma dos valores é {soma}")