"""Exercício 29 - Tipo de triângulo
Leia três medidas. Primeiro verifique se elas formam um triângulo.
Se formarem, classifique-o como equilátero, isósceles ou escaleno.
"""

from exercicios.ex28 import forma_triangulo


def classificar_triangulo(a: float, b: float, c: float) -> str:
    if not forma_triangulo(a, b, c):
        return "NÃO FORMA TRIÂNGULO"
    if a == b == c:
        return "EQUILÁTERO"
    if a == b or b == c or a == c:
        return "ISÓSCELES"
    return "ESCALENO"


def main() -> None:
    bruto = input("Lados (separados por vírgula): ")
    a, b, c = (float(v.strip().replace(",", ".")) for v in bruto.split(","))
    print(f"\nResultado: {classificar_triangulo(a, b, c)}")


if __name__ == "__main__":
    main()
