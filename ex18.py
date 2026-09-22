"""Exercício 18 - Maior de dois números
Leia dois números reais e mostre qual deles é o maior.
Se os valores forem iguais, informe que não existe maior.
"""

from typing import Optional


def maior(a: float, b: float) -> Optional[float]:
    if a == b:
        return None
    return a if a > b else b


def main() -> None:
    a = float(input("Primeiro valor: ").replace(",", "."))
    b = float(input("Segundo valor: ").replace(",", "."))
    resultado = maior(a, b)
    if resultado is None:
        print("\nValores iguais")
    else:
        print(f"\nMaior valor: {resultado:g}")


if __name__ == "__main__":
    main()
