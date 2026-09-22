"""Exercício 16 - Positivo, negativo ou zero
Leia um número real e informe se ele é positivo, negativo ou igual a zero.
"""


def classificar(numero: float) -> str:
    if numero > 0:
        return "POSITIVO"
    elif numero < 0:
        return "NEGATIVO"
    return "ZERO"


def main() -> None:
    numero = float(input("Digite um número: ").replace(",", "."))
    print(f"\nResultado: {classificar(numero)}")


if __name__ == "__main__":
    main()
