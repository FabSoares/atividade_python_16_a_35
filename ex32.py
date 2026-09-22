"""Exercício 32 - Número dentro do intervalo
Leia um número real e informe se ele está dentro do intervalo fechado de 10 até 20.
Regra: os valores 10 e 20 pertencem ao intervalo.
"""


def dentro_do_intervalo(numero: float) -> bool:
    return 10 <= numero <= 20


def main() -> None:
    numero = float(input("Número: ").replace(",", "."))
    resultado = "DENTRO" if dentro_do_intervalo(numero) else "FORA"
    print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    main()
