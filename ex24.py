"""Exercício 24 - Ano bissexto
Leia um ano inteiro e informe se ele é bissexto.
Regra: divisível por 400, ou divisível por 4 e não divisível por 100.
"""


def eh_bissexto(ano: int) -> bool:
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)


def main() -> None:
    ano = int(input("Ano: "))
    resultado = "ANO BISSEXTO" if eh_bissexto(ano) else "NÃO É ANO BISSEXTO"
    print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    main()
