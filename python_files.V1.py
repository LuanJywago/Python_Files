nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))

soma = nota1 + nota2

notatotal2 = print(f" o valor da nota 1 foi: {nota1} e da nota 2 foi: {nota2}, logo, a soma das duas notas é: {soma}")



# C = 5*(F-32)/9
f = float(input("Digite a temperatura em Fahrenheit:"))
celcius = (5*(f - 32))/9
print(f" o valor, em graus é: {celcius:.1f}")

#calculando área do circulo
pi = 3.14
r = float(input("Digite o valor do raio:"))
area = pi * r**2
print(area)




# Inicializa a variável para armazenar a soma
soma = 0

print("Digite números para somar. Digite um número negativo para encerrar.")

# Loop para receber números do usuário
while True:
    # Solicita ao usuário um número
    numero = float(input("Digite um número: "))

    # Verifica se o número é negativo
    if numero < 0:
        break  # Sai do loop se o número for negativo

    # Adiciona o número à soma
    soma += numero

# Exibe o resultado da soma
print(f"A soma dos números digitados é: {soma}")



contador = 0
soma = 0
media = 0

print("Digite um numero positivo para continuar ou digite [-1] negativo para parar!")

while True:
    numeros = float(input("Digite um número: "))

    if numeros == -1:
        break
    contador = contador + 1
    soma += numeros
media = soma / contador

print(f"A quantidade de numeros digitados foi: {contador}\nA média da turma é: {media:.2f} e a soma é {soma}")



numero = float(input("Digite um numero:"))
if numero == 0:
    print(f"O seu número {numero} é nulo")
elif numero <0:
    print(f"O seu número {numero} é Negativo")
else:
    print(f"O seu número {numero} é Positivo")
    print("O dobro deste número positivo é:", numero * 2)


numero1 = float(input("Digite o valor da venda:"))
numero2 = float(input("Digite o valor da compra:"))
prejuizo = numero2-numero1
lucro = numero1-numero2
if numero1 > numero2:
    print(f"O comprador comprou por R$ {numero2} e vendeu por R$ {numero1}, tendo lucro de R$ {lucro}")
elif numero1 < numero2:
    print(f"O comprador comprou por R$ {numero2} e vendeu por R$ {numero1}, tendo prejuízo de R$ {prejuizo}")
else:
    print("Os números são iguais")



numero = float(input("Digite um número de 0 à 200:"))
if numero >= 100:
    print("Valor maior que cem")
else:
    print("Valor menor que cem")


op = int(input("Digite um número:"))
if op % 2 == 0:
    print(f"Seu número é par: {op}")
else:
    print(f"Seu número é impar: {op}")



ano_do_nascimento = int(input("Digite o ano em que você nasceu: "))
ano_atual = 2024
idade = ano_atual - ano_do_nascimento

if idade == 16:
    print("VAI VOTAR NO BOLSONARO 22! SEM LULA AQUI. sua idade é:", idade)
elif idade == 17:
    print("VAI VOTAR NO BOLSONARO 22! SEM LULA AQUI. sua idade é:", idade, "Já já você tira a CNH")
elif idade > 18:
    print("VAI VOTAR NO BOLSONARO 22! SEM LULA AQUI. sua idade é:", idade, "Já aproveita pra tirar a carteira")
else:
    print("Vai descansar que aqui é papo de adulto, criança maldita. sua idade ainda é:", idade)



import math


def calcular_raizes(a, b, c):
    # Calcula o valor de delta
    delta = b ** 2 - 4 * a * c

    # Verifica a existência das raízes
    if delta < 0:
        return "Delta menor que 0. Não existem raízes reais."
    elif delta == 0:
        raiz = -b / (2 * a)
        return f"Delta igual a 0. Existe uma raiz real: {raiz}"
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Delta maior que 0. Existem duas raízes reais: {raiz1} e {raiz2}"


# Solicita os coeficientes ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Verifica se é uma equação do segundo grau
if a == 0:
    print("Se a = 0, não é uma equação do segundo grau.")
else:
    resultado = calcular_raizes(a, b, c)
    print(resultado)




print ("Digite qualquer valor para a soma dos numeros pares e digite [0] para parar.")
contador = 0
soma = 0
media = 0
total = 0
contador2 = 0
while True:
    valor = float(input("Digite o numero:"))
    if valor == 0:
        break
    if valor % 2 == 0:
        total += valor
        contador += 1
    contador2 += 1
media = total/contador
print(f"Todos numeros pares somados {total}\nA media deles:  {media:.4f}\n no total de numeros pares {contador}\n A quantidade de numeros foi: {contador2}")



#calcular área de um triangulo
base = float(input("Base:"))
altura = float(input("Altura:"))
area = base * altura/2

print(f"o valor da base é: {base} e da altura é: {altura}, com isso, a area é: {area:.5f}")



massa = float(input("Digite o seu peso, em quilos: "))
consumo_agua = massa * 0.03
print(consumo_agua)



senha_correta = 123
senha_usuario = int(input("Digite sua senha: "))
if senha_usuario == senha_correta:
    print("Acesso liberado")
else:
    print("Acesso negado")



nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))

soma = (nota1 + nota2 + nota3)
nota_final = soma/3
print(f"A nota 1 foi: {nota1} a nota 2 foi: {nota2}, a nota 3 foi {nota3}, a média final foi {nota_final:.2f}")

if nota_final >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")



ano_do_nascimento = int(input("Digite o ano em que você nasceu: "))
ano_atual = 2024
idade = ano_atual - ano_do_nascimento

if idade >= 16 and idade < 18:
    print("Ja pode votar e não tirar a CNH. voce tem", idade, "anos de idade")
elif idade >= 16 and idade >= 18:
    print("Ja pode votar, toma a CNH pra você", idade)
else:
   print("não pode votar e nem tirar a CNH", idade)



contador = 0
soma = 0

print("Digite um numero positivo para continuar ou  digite um numero negativo para parar!")

while True:
    numeros = float(input("Digite um número: "))

    if numeros == 0.123456789:
        break
    contador = contador + 1
    soma += numeros
print(f"A quantidade de numeros digitados foi: {contador}\nA soma dos numeros é: {soma}")



maior = 0
menor = 9999999999999
contador = 0
while True:
    numero = float(input("Digite um numero: "))

    if numero == 0:
        break
    if numero < menor:
        menor = numero
    if numero > maior:
        menor = numero

    contador += 1

print(f"Menor valor é {menor}\n o maior valor é {maior}\n O contador é {contador}")

#Tamanho e idade para a montanha russa:
tamanho = float(input("Insira seu tamanho em centimetros: "))
ingresso = 0
foto = 0
if tamanho < 120:
    print("Infelizmente você não pode ir")
elif tamanho >= 160 and tamanho <=200:
    print("Você está permitido a ir na montanha russa!")
    idade = int(input("Digite sua idade: "))
    if idade <16:
        print("Você tem a altura correta, mas a idade não. por favor, saia da fila!")
    elif idade >=17 and idade <=65:
        print("Você está permitido a ir na montanha russa. O ingresso custa: R$ 12.00")
        ingresso += 12
        print(ingresso)
    elif idade >=66:
        print("Você pode ir na montanha russa, mas devido a idade e cuidados a sua vida, o ingresso custa R$15.00")
        ingresso += 15
        print(ingresso)
    else:
        print("Digite uma idade válida!")
else:
    print("Você não pode ir na montanha Russa por excesso de tamanho. Risco a vida!")

#Acrescimo de preço de foto
foto = input("Você deseja pagar pela a foto divertida ao final do trageto? (Sim/Não)")
if foto == "Sim":
    print("A foto custa mais 5 reais")
    ingresso += 5
    print(f"O valor total foi de R${ingresso} reais. Agradecemos a visita!")
if foto == "Não":
    print("Obrigado por andar na montanha russa!")

#Solicita o valor final para o usuário
valor_final = int(input("Digite o valor que deseja ir ate o final em ordem crescente: "))
contador = 0

for i in range (1,valor_final,1):
    contador +=1
    print(i)
print(f"Foram gerados {contador} numeros no contador")


# soma do dobro dos numeros
soma = 0
contagem = 0

for i in range(1, 6):
    dobro = i * 2
    print(dobro)
    soma += dobro
    contagem += 1
media = soma / contagem

print(f"Soma: {soma}")
print(f"Média: {media}")


#Media da turma com FOR
quantidade_alunos = 50
soma = 0

for i in range(0, quantidade_alunos):
    nota = float(input("Digite a media dos alunos: "))
    soma += nota

media_turma = soma / quantidade_alunos

print(f"Soma das notas: {soma}")
print(f"Média da turma: {media_turma}")


#Fahrenheit para Celcius em
print(f" {'Fahrenheit'} | {'Celsius'}")
for fahrenheit in range(45, 81):
    celcius = 5 * (fahrenheit - 32) / 9
    print(f"{fahrenheit:.1f} ºF | {celcius:.3f} ºC")


#Numeros aleatorios com import random
import random
for i in range(5):
    i = random.randint(0, 95)
    print(i)


# Solicita os valores inicial e final ao usuário
valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))
contador = 0
soma = 0

if valor_inicial < valor_final:
    print("Sequência em ordem crescente:")
    for i in range(valor_inicial, valor_final +1, 1):
        print(i, end=" ")
        contador += 1
        soma += i
    print(f"\nA quantidade dos numeros foi: {contador}")
    print(f"\nA soma dos numeros foi de : {soma}")

elif valor_inicial > valor_final:
    print("Sequência em ordem decrescente:")
    for j in range(valor_inicial, valor_final -1, -1):
        print(j, end=" ")
        contador +=1
        soma += j
    print(f"\nA quantidade dos numeros foi: {contador}")
    print(f"\nA soma dos numeros foi de : {soma}")
else:
    print("Os valores são iguais, por favor, informe valores válidos")

#Começo do uso do def in fuction
def calcular_dobro(p_valor):
    dobro = p_valor *2
    return dobro

def calcular_triplo(p_valor2):
    triplo = p_valor2 *3
    return triplo

if __name__ == '__main__':
    p_valor = int(input("Digite o valor para dobrar: "))
    retorno = calcular_dobro(p_valor)
    print(f"o valor retornado de {p_valor} é {retorno}")

    p_valor2 = int(input("Digite o valor para ser triplicado: "))
    retorno2 = calcular_triplo(p_valor2)
    print(f"O valor informado de {p_valor2} é {retorno2}")

#informa mesnagem e numero passado pelo usuário
def mostar_mensagem (mensagem, numero):
    print(f'Descreva a messagem {mensagem} ')
    print(f'Escreva o número informado: {numero}')

def main ():
    mensagem = input("Mensagem passada: ")
    numero = float(input("Número a passar: "))
    mostar_mensagem(mensagem, numero)


if __name__ == '__main__':
    main()

#calcula a idade informada pelo ano pelo usuário
def calcula_idade(ano):
    ano_atual = 2024
    idade = ano_atual - ano
    return idade

def main():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = calcula_idade(ano_nascimento)
    print(f"A idade da pessoa é de: {idade} anos")

if __name__ == "__main__":
    main()


#informa 2 valores inteiros passados pelo usuário como retorno de leitura
def val_inteiro (val1, val2):
    print(f'O valor 1 foi: {val1}')
    print(f'O valor 2 foi: {val2}')

def main():
    print('Informe os valores em números inteiros!')
    val1 = int(input("Digite o valor 1: "))
    val2 = int(input("Digite o valor 2: "))
    val_inteiro(val1,val2)


if __name__ == '__main__':
    main()

## Compilado de codigos utulizando a lista e seus atributos envolvidos
numeros = []


while True:
    valor = input("Digite algo para acrescentar à lista ou [0] para parar: ")
    if valor.lower() == "sair":
        break
    valor = int(valor)
    numeros.append(valor)

quantidade = len(numeros)
print(quantidade)

soma = sum(numeros)
print(soma)

maior = max(numeros)
print(maior)

menor = min(numeros)
print(menor)

if 5 in numeros:
    print("True")
else:
    ("False")

verificar_posicao = print(numeros.index(5))
ordem_crescente = numeros.sort()
numeros [5] = 33

numeros.reverse()
print(numeros)

media = soma/quantidade
print(f"{media:.1f}")

contador = 0
for valor in numeros:
    if valor > 10:
        contador = + 1
valor_maior_10 = (contador / quantidade) * 100
print(valor_maior_10)

#gerador de senha usando for com método fácil
import random
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["@", "!", "#", "%", "¨", "&", "*", "(", ")", "-"]

quant_letra = int(input("Quantas letras você quer ter na senha? "))
quant_numero = int(input("Quantos numeros você quer ter na senha? "))
quant_simbolos = int(input("Quantos simbolos você quer ter na senha? "))

senha = ""

for char in range(1, quant_letra + 1):
    senha += random.choice(letras)

for char in range(1, quant_numero + 1):
    senha += random.choice(numeros)

for char in range(1, quant_simbolos + 1):
    senha += random.choice(simbolos)

print(senha)

#Cifra de cesar feito em python com codificador e decodificador:
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def encriptar(texto_original, espaco_usado):
    cipher_text = ""

    for letra in texto_original:
        if letra in alfabeto:
            espacamento_usado = (alfabeto.index(letra) + espaco_usado) % len(alfabeto)
            cipher_text += alfabeto[espacamento_usado]
        else:
            cipher_text += letra

    print(f"Aqui está o resultado da codificação: {cipher_text}")


def descodificar(texto_original, espaco_usado):
    texto_saida = ""

    for letra in texto_original:
        if letra in alfabeto:
            espacamento_usado = (alfabeto.index(letra) - espaco_usado) % len(alfabeto)
            texto_saida += alfabeto[espacamento_usado]
        else:
            texto_saida += letra

    print(f"Aqui está o resultado da decodificação: {texto_saida}")


deseja_continuar = True

while deseja_continuar:
    direcao = input("Digite 'codificar' para encriptar algo ou digite 'descodificar' para descriptar algo\n").lower()
    texto = input("Digite a sua mensagem:\n").lower()
    espaco = int(input("Digite a quantidade de espaço utilizado\n"))

    if direcao == 'codificar':
        encriptar(texto, espaco)
    elif direcao == 'descodificar':
        descodificar(texto, espaco)
    else:
        print("Opção inválida")

    reiniciar = input("Digite sim para continuar ou não para parar.\n").lower()

    if reiniciar == "não":
        deseja_continuar = False
        print("Processo finalizado\n")
    else:
        deseja_continuar = True
        print("Processo contínuo!\n")
