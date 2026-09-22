# 100 Exercícios de Lógica de Programação — Exercícios 16 a 35

Soluções em Python para os exercícios 16 a 35 do material **"100 Exercícios
de Lógica de Programação"** (Módulo 02 — Estruturas Condicionais).

Cada exercício foi implementado como um módulo independente, com:

- uma função **pura** (fácil de testar), contendo a lógica do problema;
- um bloco `main()` que lê a entrada do usuário via terminal e imprime a
  saída, reproduzindo o "Exemplo de execução" do enunciado;
- testes automatizados baseados nas tabelas **"Teste seu programa"** de
  cada exercício.

## Estrutura do repositório

```
.
├── exercicios/
│   ├── ex16.py   # Positivo, negativo ou zero
│   ├── ex17.py   # Par ou ímpar
│   ├── ex18.py   # Maior de dois números
│   ├── ex19.py   # Maior e menor de três números
│   ├── ex20.py   # Três valores em ordem crescente
│   ├── ex21.py   # Aprovado ou reprovado
│   ├── ex22.py   # Situação do aluno por faixa
│   ├── ex23.py   # Categoria de votação
│   ├── ex24.py   # Ano bissexto
│   ├── ex25.py   # Preço conforme a forma de pagamento
│   ├── ex26.py   # Reajuste por faixa salarial
│   ├── ex27.py   # Classificação de IMC
│   ├── ex28.py   # É possível formar um triângulo?
│   ├── ex29.py   # Tipo de triângulo
│   ├── ex30.py   # Aprovação de empréstimo
│   ├── ex31.py   # Divisível por 3 e por 5
│   ├── ex32.py   # Número dentro do intervalo
│   ├── ex33.py   # Dia da semana
│   ├── ex34.py   # Quantidade de dias do mês
│   └── ex35.py   # Valor do ingresso
└── tests/
    └── test_exercicios.py
```

## Requisitos

- Python 3.8 ou superior (nenhuma biblioteca externa é necessária).

## Como executar um exercício

Rode qualquer módulo diretamente, a partir da raiz do repositório:

```bash
python -m exercicios.ex16
```

Exemplo (Exercício 16):

```
Digite um número: -7

Resultado: NEGATIVO
```

## Como rodar os testes

Com `unittest` (nenhuma dependência extra):

```bash
python -m unittest discover -s tests -v
```

Ou, se preferir `pytest`:

```bash
pip install pytest
python -m pytest tests/ -v
```

Os 20 exercícios possuem testes cobrindo os casos apresentados nas tabelas
"Teste seu programa" de cada enunciado.

## Como subir este projeto para o GitHub

```bash
cd caminho/para/este/repositorio
git init
git add .
git commit -m "Exercícios 16 a 35 - Lógica de Programação"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
git push -u origin main
```

## Licença

Uso livre para fins de estudo.
