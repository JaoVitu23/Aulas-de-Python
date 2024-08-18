#Nesta aula continuaremos os aprendizados com laços de repetição, mas dessa vez utilizando o WHILE

#Estrutura Basica de um WHILE
'''
While not 'tal coisa':
    'Aqui dentro podem estar diversos tipos de outras estruturas'
'''

#Exemplos 

c = 1           #Podemos usar o WHILE para quando sabemos o limite de uma determinada situação, assim como o FOR
while c < 10:   
    print(c)
    c += 1
print('Fim')

r = 's'
while r == 's': #Mas quando desconheços o limite, ai que entra o WHILE
    valor = int(input("Digite um Valor: "))
    r = str(input("Deseja continuar? (S/N): ")).lower()
print("Fim!")


num = 1
impar = par = 0 #Podemos fazer programas com perguntas infinitas utilizando o WHILE
while num != 0: #Que so terminam quando o usuário determinar o fim
    num = int(input("Digite um número qualquer: "))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1

print(f"Você digitou {par} números pares, e também digitou {impar} números ímpares.") 