"""Exercício 33 - Dia da semana
Leia um número de 1 a 7 e mostre o dia da semana correspondente.
Para qualquer outro valor, mostre OPÇÃO INVÁLIDA.
"""

from typing import Optional

DIAS = {
    1: "SEGUNDA-FEIRA",
    2: "TERÇA-FEIRA",
    3: "QUARTA-FEIRA",
    4: "QUINTA-FEIRA",
    5: "SEXTA-FEIRA",
    6: "SÁBADO",
    7: "DOMINGO",
}


def dia_da_semana(numero: int) -> Optional[str]:
    return DIAS.get(numero)


def main() -> None:
    numero = int(input("Número (1 a 7): "))
    resultado = dia_da_semana(numero) or "OPÇÃO INVÁLIDA"
    print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    main()
