## for com contador in range
contador = 0

for numero in range(11):
    contador += 1
    print("Numeros naturais inteiros na vertical: ", numero)
print (contador)

## for com lista de numeros
numeros = ['1', '2', '3', '5', '6', '7', '8', '9', '10']
for numeros in numeros:
    print (numeros, end=" ")

## for com numeros na horizontal
for numero in range(0, 11, 5):
    print (numero, end= ', ')

## for com if para finalizar com ponto final
for numero in range(0, 10, 1):
    print(numero, end=', ')
    if numero == 9:
        print("10.")

#for com numero para dar valores apenas pares
for numero in range(0, 14, 1):
    if numero % 2 == 0:
        print(numero, end=', ')
        if numero == 12:
            print("14.")

#for inicial dos projetos
for numero in range(7, -1, -1):
    print(numero)

# Cria uma lista de 0 a 7
numeros = list(range(8))
for numero in reversed(numeros):
    print(numero)
