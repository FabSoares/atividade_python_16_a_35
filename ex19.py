"""Exercício 19 - Maior e menor de três números
Leia três números reais e mostre o maior e o menor valor informado.
Requisito: o programa deve funcionar também quando houver valores repetidos.
"""

from typing import Tuple


def maior_menor(a: float, b: float, c: float) -> Tuple[float, float]:
    return max(a, b, c), min(a, b, c)


def main() -> None:
    bruto = input("Valores (separados por vírgula): ")
    a, b, c = (float(v.strip().replace(",", ".")) for v in bruto.split(","))
    maximo, minimo = maior_menor(a, b, c)
    print(f"\nMaior: {maximo:g}")
    print(f"Menor: {minimo:g}")


if __name__ == "__main__":
    main()
