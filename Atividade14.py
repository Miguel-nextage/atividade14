# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado

N1, N2, N3 = int(input("Sua primeira nota aqui")), int(input("Sua segunda nota aqui")), int(input("Sua terceira nota aqui"))

media = (N1 + N2 + N3) / 3

if media >= 7:
    print("Aprovado!")

elif 5 <= media < 7:
    print("Recuperação")

elif  media < 5:
    print("Reprovado!") 