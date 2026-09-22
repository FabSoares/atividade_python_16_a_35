"""Exercício 22 - Situação do aluno por faixa
Leia duas notas, calcule a média e informe a situação do aluno conforme a tabela:
  média < 5,0                    -> REPROVADO
  5,0 <= média < 7,0             -> RECUPERAÇÃO
  média >= 7,0                   -> APROVADO
"""


def situacao(nota1: float, nota2: float) -> str:
    media = (nota1 + nota2) / 2
    if media < 5.0:
        return "REPROVADO"
    if media < 7.0:
        return "RECUPERAÇÃO"
    return "APROVADO"


def main() -> None:
    n1 = float(input("Nota 1: ").replace(",", "."))
    n2 = float(input("Nota 2: ").replace(",", "."))
    media = (n1 + n2) / 2
    print(f"\nMédia: {media:g}")
    print(f"Situação: {situacao(n1, n2)}")


if __name__ == "__main__":
    main()
