frase = 'Curso em video Python'

print(frase[3]) #Mostraria a quarta letra, indice começa em 0

print(frase[3:13]) #para fatiar da quarta letra até a décima quarta

print(frase[:13]) #se eu não indicar o inicio, começa do 0, valido para o final, irá até o fim

print(frase[3:2:13]) #para ir da quarta até a decima quarta pulando de 2 em 2

print("""Utilize aspas para 
        escrever textos pulando linhas""")

print(frase.count('o')) #mostrara quantas vezes aparece o 'O' dentro da frase

print((len(frase)))# para mostrar qual o tamanho da string

print((len(frase.strip()))) #strip para remover espaços

frase.replace('Python', 'Android') #para substituir as palavras, porém não altera na string direto, para isso é necessário que a variavel receba

print(frase.find('Curso'))# para indicar a posiçao que está a palavra

print(frase.split()) #para dividir a frase

dividido = print(frase.split()) #para criar uma lista com cada palavra da string

print(dividido[2][3]) #para mostrar o divido 2 ('video) e mostrar a letra 3 ('E')













