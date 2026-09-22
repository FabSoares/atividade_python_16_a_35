"""Exercício 17 - Par ou ímpar
Leia um número inteiro e informe se ele é par ou ímpar.
Regra: um número é par quando o resto da divisão por 2 é igual a zero.
"""


def classificar(numero: int) -> str:
    return "PAR" if numero % 2 == 0 else "ÍMPAR"


def main() -> None:
    numero = int(input("Digite um número: "))
    print(f"\nResultado: {classificar(numero)}")


if __name__ == "__main__":
    main()
