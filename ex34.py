"""Exercício 34 - Quantidade de dias do mês
Leia o número de um mês e um ano. Mostre quantos dias o mês possui.
Requisito: se o mês estiver fora de 1 a 12, mostre MÊS INVÁLIDO.
"""

from typing import Optional

from exercicios.ex24 import eh_bissexto

MESES_31 = {1, 3, 5, 7, 8, 10, 12}
MESES_30 = {4, 6, 9, 11}


def dias_do_mes(mes: int, ano: int) -> Optional[int]:
    if mes in MESES_31:
        return 31
    if mes in MESES_30:
        return 30
    if mes == 2:
        return 29 if eh_bissexto(ano) else 28
    return None


def main() -> None:
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    dias = dias_do_mes(mes, ano)
    if dias is None:
        print("\nResultado: MÊS INVÁLIDO")
    else:
        print(f"\nResultado: {dias} dias")


if __name__ == "__main__":
    main()
