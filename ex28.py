"""Exercício 28 - É possível formar um triângulo?
Leia três medidas positivas e informe se elas podem formar um triângulo.
Regra: três lados formam um triângulo quando cada lado é menor que a soma
dos outros dois.
"""


def forma_triangulo(a: float, b: float, c: float) -> bool:
    return a < b + c and b < a + c and c < a + b


def main() -> None:
    bruto = input("Lados (separados por vírgula): ")
    a, b, c = (float(v.strip().replace(",", ".")) for v in bruto.split(","))
    resultado = "FORMAM UM TRIÂNGULO" if forma_triangulo(a, b, c) else "NÃO FORMAM UM TRIÂNGULO"
    print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    main()
