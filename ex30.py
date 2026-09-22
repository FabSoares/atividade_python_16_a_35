"""Exercício 30 - Aprovação de empréstimo
Leia o valor de um imóvel, o salário mensal do comprador e o prazo em anos.
Regra: prestação = valor do imóvel / (anos * 12).
O empréstimo é aprovado quando a prestação não ultrapassa 30% do salário.
"""

from typing import Tuple


def calcular_prestacao(valor_imovel: float, anos: int) -> float:
    return valor_imovel / (anos * 12)


def avaliar_emprestimo(valor_imovel: float, salario: float, anos: int) -> Tuple[float, float, str]:
    prestacao = calcular_prestacao(valor_imovel, anos)
    limite = salario * 0.30
    resultado = "APROVADO" if prestacao <= limite else "NEGADO"
    return prestacao, limite, resultado


def main() -> None:
    valor_imovel = float(input("Valor do imóvel: ").replace(",", "."))
    salario = float(input("Salário: ").replace(",", "."))
    anos = int(input("Prazo (anos): "))
    prestacao, limite, resultado = avaliar_emprestimo(valor_imovel, salario, anos)
    print(f"\nPrestação: R$ {prestacao:.2f}".replace(".", ","))
    print(f"Limite: R$ {limite:.2f}".replace(".", ","))
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
