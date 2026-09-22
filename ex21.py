"""Exercício 21 - Aprovado ou reprovado
Leia duas notas, calcule a média e informe se o aluno foi aprovado ou reprovado.
Regra: média maior ou igual a 7,0 significa APROVADO; abaixo de 7,0 é REPROVADO.
"""


def situacao(nota1: float, nota2: float) -> str:
    media = (nota1 + nota2) / 2
    return "APROVADO" if media >= 7.0 else "REPROVADO"


def calcular_media(nota1: float, nota2: float) -> float:
    return (nota1 + nota2) / 2


def main() -> None:
    n1 = float(input("Nota 1: ").replace(",", "."))
    n2 = float(input("Nota 2: ").replace(",", "."))
    media = calcular_media(n1, n2)
    print(f"\nMédia: {media:g}")
    print(f"Situação: {situacao(n1, n2)}")


if __name__ == "__main__":
    main()
