lista_nomes = []
lista_notas = []
n_alunos = int(input("Insira o número de alunos: "))
nota_geral = 0
maior_nota = 0
maior = None
menor = None
maior_aluno = None
menor_aluno = None

for i in range(n_alunos):
    while True:
        nota = int(input("Insira a nota do aluno (entre 0 e 10): "))
        if 0 <= nota <= 10:
            break
        else:
            print("Nota inválida! Por favor, insira uma nota entre 0 e 10.")

    lista_notas.append(nota)
    nome = input("Insira o nome do aluno: ").capitalize()
    lista_nomes.append(nome)
    nota_geral += nota

    if maior is None or maior < nota:
        maior = nota
        maior_aluno = nome
    if menor is None or menor > nota:
        menor = nota
        menor_aluno = nome

media_geral = nota_geral / n_alunos
acima_da_media = sum(1 for nota in lista_notas if nota > media_geral)

print(f"A média geral da turma é: {media_geral:.2f}")
print(f"O aluno com a maior nota da turma é {maior_aluno} e sua nota é: {maior}")
print(f"O aluno com a menor nota da turma é {menor_aluno} e sua nota é: {menor}")
print(f"A quantidade de alunos da turma que estão acima da média é {acima_da_media}")

