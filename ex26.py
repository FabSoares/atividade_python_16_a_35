"""Exercício 26 - Reajuste por faixa salarial
Leia o salário atual e calcule o novo salário conforme a tabela:
  até R$ 1.500,00                          -> 15%
  de R$ 1.500,01 até R$ 3.000,00           -> 10%
  acima de R$ 3.000,00                     -> 5%
Requisito: mostrar o percentual, o valor do aumento e o novo salário.
"""

from typing import Tuple


def percentual_reajuste(salario: float) -> float:
    if salario <= 1500:
        return 0.15
    if salario <= 3000:
        return 0.10
    return 0.05


def calcular_reajuste(salario: float) -> Tuple[float, float, float]:
    percentual = percentual_reajuste(salario)
    aumento = round(salario * percentual, 2)
    novo_salario = round(salario + aumento, 2)
    return percentual, aumento, novo_salario


def main() -> None:
    salario = float(input("Salário atual: ").replace(",", "."))
    percentual, aumento, novo_salario = calcular_reajuste(salario)
    print(f"\nPercentual aplicado: {percentual * 100:.0f}%")
    print(f"Valor do aumento: R$ {aumento:.2f}".replace(".", ","))
    print(f"Novo salário: R$ {novo_salario:.2f}".replace(".", ","))


if __name__ == "__main__":
    main()
