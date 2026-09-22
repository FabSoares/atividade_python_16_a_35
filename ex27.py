"""Exercício 27 - Classificação de IMC
Leia o peso (kg) e a altura (m). Calcule o IMC = peso / (altura * altura)
e classifique conforme a tabela:
  IMC < 18,5                       -> ABAIXO DA FAIXA
  18,5 <= IMC < 25,0               -> FAIXA NORMAL
  25,0 <= IMC < 30,0               -> ACIMA DA FAIXA
  IMC >= 30,0                      -> FAIXA ELEVADA
"""

from typing import Tuple


def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura * altura)


def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "ABAIXO DA FAIXA"
    if imc < 25.0:
        return "FAIXA NORMAL"
    if imc < 30.0:
        return "ACIMA DA FAIXA"
    return "FAIXA ELEVADA"


def avaliar(peso: float, altura: float) -> Tuple[float, str]:
    imc = calcular_imc(peso, altura)
    return imc, classificar_imc(imc)


def main() -> None:
    peso = float(input("Peso (kg): ").replace(",", "."))
    altura = float(input("Altura (m): ").replace(",", "."))
    imc, classificacao = avaliar(peso, altura)
    print(f"\nIMC: {imc:.1f}".replace(".", ","))
    print(f"Classificação: {classificacao}")


if __name__ == "__main__":
    main()
