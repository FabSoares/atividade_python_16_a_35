"""Exercício 20 - Três valores em ordem crescente
Leia três números inteiros e mostre os valores em ordem crescente.
Requisito: aceite valores repetidos.
"""

from typing import List


def ordenar(valores: List[int]) -> List[int]:
    return sorted(valores)


def main() -> None:
    bruto = input("Valores (separados por vírgula): ")
    valores = [int(v.strip()) for v in bruto.split(",")]
    ordenados = ordenar(valores)
    print("\nOrdem crescente:", ", ".join(str(v) for v in ordenados))


if __name__ == "__main__":
    main()
