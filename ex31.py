"""Exercício 31 - Divisível por 3 e por 5
Leia um número inteiro e informe em qual situação ele se encontra:
  divisível por 3 e por 5   -> DIVISÍVEL POR 3 E 5
  apenas por 3              -> DIVISÍVEL APENAS POR 3
  apenas por 5              -> DIVISÍVEL APENAS POR 5
  por nenhum dos dois       -> NÃO DIVISÍVEL POR 3 NEM 5
"""


def classificar(numero: int) -> str:
    div3 = numero % 3 == 0
    div5 = numero % 5 == 0
    if div3 and div5:
        return "DIVISÍVEL POR 3 E 5"
    if div3:
        return "DIVISÍVEL APENAS POR 3"
    if div5:
        return "DIVISÍVEL APENAS POR 5"
    return "NÃO DIVISÍVEL POR 3 NEM 5"


def main() -> None:
    numero = int(input("Número: "))
    print(f"\nResultado: {classificar(numero)}")


if __name__ == "__main__":
    main()
