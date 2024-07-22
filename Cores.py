#Aula bonus sobre como utilizar cores no Python 

'''Pesquisar sobre colorrise para mais diversidade de dados'''

#CONFIGURAÇÃO DE CORES PYTHON
'''
STYLE:          | Text:            | Background:
0 - Nada        | 30 - Branco      | 40 - Branco
1 - Negrito     | 31 - Vermelho    | 41 - Vermelho
4 - Sublinhado  | 32 - Verde       | 42 - Verde
7 - Inversão    | 33 - Amarelo     | 43 - Amarelo
                | 34 - Azul        | 44 - Azul
                | 35 - Magenta     | 45 - Magenta
                | 36 - Ciano       | 46 - Ciano
                | 37 - Cinza       | 47 - Cinza

Estrutura de código para cor - \033[0;33;44m #A primeira casa é Style, a segunda Text e a terceria é Background

'''
#METODO PARA UTILIZAÇÃO DE CORES E TESTE DE CORES

print("\033[31m Olá Mundo!") #Vermelho
print("\033[31;43m Olá Mundo!\033[m") #Vermelho com fundo Amarelo - Atenção ao detalhe que se usarmos \033[m no final da frase que escrevemos, a formatação acaba onde é demarcado o final do print.
print("\033[4;30;45m Olá Mundo!\033[m") #Letra Branca, sublinhada com fundo lilás
print("\033[7;30m Olá Mundo!") #Letra Branca fundo preto
print("\033[0;33;44m Olá Mundo!") #Letra Amarela e fundo azul
print("\033[7;33;44m Olá Mundo!\033[m") #Letra Azul e fundo amarelo
a = 5
b = 4
print(f"Os valores são \033[32m{a}\033[m e \033[33m{b}\033[m") # A verde e B amarelo

#Melhor método para utilização de cores

nome = "João Vitor"
cores = {"limpa":"\033[m", #Lista de cores para utilização
        "Azul":"\033[34m",
         "Vermelho":"\033[31m",
         "Verde":"\033[32m"}

print(f"Olá! Tudo bem? Meu nome é{cores['Vermelho']} {nome} {cores['limpa']}")


  