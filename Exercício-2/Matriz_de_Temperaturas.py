# Inicialização da matriz
matriz = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
]

# Função para ler temperaturas e calcular médias
def ler_temperaturas(semana):
    dias = 1
    temp_media = 0
    menor = None
    maior = None

    while dias != 5:
        temp = float(input(f"Insira a temperatura da semana {semana} do dia {dias}: "))
        matriz[semana - 1][dias - 1] = temp  # Armazenar na matriz
        dias += 1
        temp_media += temp

        if maior is None or maior < temp:
            maior = temp
        if menor is None or menor > temp:
            menor = temp

    media = temp_media / 4  # 4 dias
    return media, menor, maior

# Ler temperaturas para cada semana
media1, menor1, maior1 = ler_temperaturas(1)
print(f"A média de temperatura da semana 1 foi {media1:.2f} °C")

media2, menor2, maior2 = ler_temperaturas(2)
print(f"A média de temperatura da semana 2 foi {media2:.2f} °C")

media3, menor3, maior3 = ler_temperaturas(3)
print(f"A média de temperatura da semana 3 foi {media3:.2f} °C")

# A maior temperatura registrada
maiorT = max(maior1, maior2, maior3)
print(f"A maior temperatura registrada nas semanas foi {maiorT:.2f} °C")

# A menor temperatura registrada
menorT = min(menor1, menor2, menor3)
print(f"A menor temperatura registrada nas semanas foi {menorT:.2f} °C")

# Temperatura média geral
tempMG = (media1 + media2 + media3) / 3
print(f"A média geral das temperaturas foi {tempMG:.2f} °C")

# Exibir a matriz de temperaturas
print("\nMatriz de Temperaturas:")
for linha in matriz:
    print(" | ".join(f"{valor:>5}" for valor in linha))
