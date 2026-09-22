"""Exercício 23 - Categoria de votação
Leia a idade de uma pessoa e informe a categoria de votação:
  idade < 16          -> NÃO PODE VOTAR
  16 ou 17            -> VOTO OPCIONAL
  18 a 69             -> VOTO OBRIGATÓRIO
  70 ou mais          -> VOTO OPCIONAL
"""


def categoria(idade: int) -> str:
    if idade < 16:
        return "NÃO PODE VOTAR"
    if idade <= 17:
        return "VOTO OPCIONAL"
    if idade <= 69:
        return "VOTO OBRIGATÓRIO"
    return "VOTO OPCIONAL"


def main() -> None:
    idade = int(input("Idade: "))
    print(f"\nCategoria: {categoria(idade)}")


if __name__ == "__main__":
    main()
