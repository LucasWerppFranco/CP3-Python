n = int(input("Digite um número inteiro n: "))

soma_impares = 0
i = 1

while i <= n:
    soma_impares += i
    i += 2

print(f"A soma dos números ímpares de 1 a {n} é: {soma_impares}")

contador_pares_multiplos_3 = 0

for j in range(1, n + 1):
    if j % 2 == 0 and j % 3 == 0:
        contador_pares_multiplos_3 += 1

print(f"O número de números pares múltiplos de 3 entre 1 e {n} é: {contador_pares_multiplos_3}")
