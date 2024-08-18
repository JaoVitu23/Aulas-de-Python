#Nesta aula aprenderemos sobre Condições Aninhadas

#Estrutura de código:

'''
if carro.esquerda():
    Bloco 1
elif carro.direita():
    Bloco 2
elif carro.ré():
    Bloco 3
else:
    Bloco 4
''' # É possível utilizar quantos 'elif' forem necessários, porém nunca será possível utilizar uma estrutura de repetição -
    # Sem começar com um 'if'.

#Exemplos da Aula:

nome = str(input("Qual o seu nome? ")).strip().lower()
if nome == 'joao':
    print("Que nome lindo você tem!")

elif nome == 'pedro' or nome == 'maria' or nome == 'caio':
    print("Seu nome é bem popular.")

elif nome == 'maria antonieta':
    print("Belo feminino nome você tem!")

else:
    print("Seu nome é bem normal.")
print(f"Tenha um bom dia, {nome}!")