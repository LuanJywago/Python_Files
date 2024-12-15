import random

vidas = 5

# Escolhe uma palavra aleatória
palavras = ["coelho", "girafa", "centopeia", "hamburguer"]
escolha_aleatoria = random.choice(palavras).lower()

# Dá a quantidade de letras em _ para as letras
espaco = ""
quantidade_letras = len(escolha_aleatoria)
for posicao in range(quantidade_letras):
    espaco += "_"
print(espaco)

game_over = False
letras_certas = []

# Pergunta a pessoa a letra
while not game_over:
    tentativa = input("Digite uma letra que possa conter no jogo da forca: ").lower()

    # Verifica se a tentativa já foi feita antes
    if tentativa in letras_certas:
        print("Você já tentou essa letra!")
        continue

    # Se a letra for correta, adiciona à lista de letras certas
    letras_certas.append(tentativa)

    # Revela as letras certas e mantém _ para as erradas em loop fechado
    mostrar = ""
    for letra in escolha_aleatoria:
        if letra in letras_certas:
            mostrar += letra
        else:
            mostrar += "_"

    print(mostrar)

    # Se a letra não estiver na palavra, perde uma vida
    if tentativa not in escolha_aleatoria:
        vidas -= 1
        print(f"Você errou! Vidas restantes: {vidas}")
        if vidas == 0:
            print(f"Você perdeu! A palavra era: {escolha_aleatoria}")
            game_over = True

    # Verifica se o jogador ganhou
    if "_" not in mostrar:
        game_over = True
        print(f"Você ganhou! A palavra era: {escolha_aleatoria}")










