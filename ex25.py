"""Exercício 25 - Preço conforme a forma de pagamento
Leia o preço de um produto e a opção de pagamento, calcule o valor final:
  1 - Dinheiro ou Pix     -> 10% de desconto
  2 - Débito              -> 5% de desconto
  3 - Crédito à vista     -> sem alteração
  4 - Crédito parcelado   -> 8% de acréscimo
"""

from typing import Optional

FATORES = {1: 0.90, 2: 0.95, 3: 1.00, 4: 1.08}


def valor_final(preco: float, opcao: int) -> Optional[float]:
    fator = FATORES.get(opcao)
    if fator is None:
        return None
    return round(preco * fator, 2)


def main() -> None:
    preco = float(input("Preço: ").replace(",", "."))
    opcao = int(input("Opção: "))
    resultado = valor_final(preco, opcao)
    if resultado is None:
        print("\nOpção inválida")
    else:
        print(f"\nValor final: R$ {resultado:.2f}".replace(".", ","))


if __name__ == "__main__":
    main()
