"""Exercício 35 - Valor do ingresso
O ingresso custa R$ 30,00. Leia a idade e informe se a pessoa é estudante.
Regra: paga meia-entrada quem tiver menos de 12 anos, quem for estudante ou
quem tiver 60 anos ou mais. O desconto é de 50% e não é acumulativo.
"""

PRECO_CHEIO = 30.00


def tem_direito_a_meia(idade: int, estudante: bool) -> bool:
    return idade < 12 or estudante or idade >= 60


def calcular_valor(idade: int, estudante: bool) -> float:
    if tem_direito_a_meia(idade, estudante):
        return round(PRECO_CHEIO * 0.5, 2)
    return PRECO_CHEIO


def _ler_sim_nao(pergunta: str) -> bool:
    return input(pergunta).strip().upper() in ("SIM", "S")


def main() -> None:
    idade = int(input("Idade: "))
    estudante = _ler_sim_nao("Estudante (SIM/NÃO): ")
    valor = calcular_valor(idade, estudante)
    print(f"\nValor do ingresso: R$ {valor:.2f}".replace(".", ","))


if __name__ == "__main__":
    main()
