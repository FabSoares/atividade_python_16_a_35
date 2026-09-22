"""
Testes automatizados para os exercícios 16 a 35.

Os casos de teste foram extraídos diretamente das tabelas "Teste seu
programa" e "Verificação final" de cada exercício, no material
"100 Exercícios de Lógica de Programação".

Execute com:
    python -m pytest tests/ -v
ou, sem pytest instalado:
    python -m unittest tests/test_exercicios.py -v
"""

import unittest

from exercicios import (
    ex16, ex17, ex18, ex19, ex20, ex21, ex22, ex23, ex24, ex25,
    ex26, ex27, ex28, ex29, ex30, ex31, ex32, ex33, ex34, ex35,
)


class TestEx16PositivoNegativoZero(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex16.classificar(12), "POSITIVO")
        self.assertEqual(ex16.classificar(-0.5), "NEGATIVO")
        self.assertEqual(ex16.classificar(0), "ZERO")


class TestEx17ParOuImpar(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex17.classificar(13), "ÍMPAR")
        self.assertEqual(ex17.classificar(0), "PAR")
        self.assertEqual(ex17.classificar(-8), "PAR")


class TestEx18MaiorDeDois(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex18.maior(4, 9), 9)
        self.assertEqual(ex18.maior(-2, -8), -2)
        self.assertIsNone(ex18.maior(5, 5))


class TestEx19MaiorMenorDeTres(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex19.maior_menor(3, 9, 5), (9, 3))
        self.assertEqual(ex19.maior_menor(-4, -1, -7), (-1, -7))
        self.assertEqual(ex19.maior_menor(6, 6, 2), (6, 2))


class TestEx20OrdemCrescente(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex20.ordenar([3, 1, 2]), [1, 2, 3])
        self.assertEqual(ex20.ordenar([7, 7, 4]), [4, 7, 7])
        self.assertEqual(ex20.ordenar([-1, -5, 0]), [-5, -1, 0])


class TestEx21AprovadoReprovado(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex21.situacao(5.0, 8.0), "REPROVADO")
        self.assertEqual(ex21.situacao(7.0, 7.0), "APROVADO")
        self.assertEqual(ex21.situacao(10.0, 9.0), "APROVADO")


class TestEx22SituacaoPorFaixa(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex22.situacao(4.0, 5.0), "REPROVADO")
        self.assertEqual(ex22.situacao(5.0, 5.0), "RECUPERAÇÃO")
        self.assertEqual(ex22.situacao(7.0, 7.0), "APROVADO")


class TestEx23CategoriaVotacao(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex23.categoria(15), "NÃO PODE VOTAR")
        self.assertEqual(ex23.categoria(16), "VOTO OPCIONAL")
        self.assertEqual(ex23.categoria(18), "VOTO OBRIGATÓRIO")
        self.assertEqual(ex23.categoria(70), "VOTO OPCIONAL")


class TestEx24AnoBissexto(unittest.TestCase):
    def test_casos(self):
        self.assertTrue(ex24.eh_bissexto(2024))
        self.assertFalse(ex24.eh_bissexto(1900))
        self.assertTrue(ex24.eh_bissexto(2000))
        self.assertFalse(ex24.eh_bissexto(2023))


class TestEx25PrecoPagamento(unittest.TestCase):
    def test_casos(self):
        self.assertAlmostEqual(ex25.valor_final(100, 2), 95.0)
        self.assertAlmostEqual(ex25.valor_final(100, 3), 100.0)
        self.assertAlmostEqual(ex25.valor_final(100, 4), 108.0)


class TestEx26ReajusteSalarial(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex26.calcular_reajuste(1500), (0.15, 225.0, 1725.0))
        self.assertEqual(ex26.calcular_reajuste(3000), (0.10, 300.0, 3300.0))
        self.assertEqual(ex26.calcular_reajuste(4000), (0.05, 200.0, 4200.0))


class TestEx27ClassificacaoIMC(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex27.classificar_imc(ex27.calcular_imc(50, 1.70)), "ABAIXO DA FAIXA")
        self.assertEqual(ex27.classificar_imc(ex27.calcular_imc(80, 1.80)), "FAIXA NORMAL")
        self.assertEqual(ex27.classificar_imc(ex27.calcular_imc(90, 1.70)), "FAIXA ELEVADA")


class TestEx28FormaTriangulo(unittest.TestCase):
    def test_casos(self):
        self.assertTrue(ex28.forma_triangulo(2, 2, 3))
        self.assertFalse(ex28.forma_triangulo(1, 2, 3))
        self.assertFalse(ex28.forma_triangulo(5, 5, 10))


class TestEx29TipoTriangulo(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex29.classificar_triangulo(5, 5, 5), "EQUILÁTERO")
        self.assertEqual(ex29.classificar_triangulo(5, 5, 3), "ISÓSCELES")
        self.assertEqual(ex29.classificar_triangulo(3, 4, 5), "ESCALENO")
        self.assertEqual(ex29.classificar_triangulo(1, 2, 3), "NÃO FORMA TRIÂNGULO")


class TestEx30AprovacaoEmprestimo(unittest.TestCase):
    def test_casos(self):
        _, _, r1 = ex30.avaliar_emprestimo(120_000, 2_000, 20)
        self.assertEqual(r1, "APROVADO")
        _, _, r2 = ex30.avaliar_emprestimo(300_000, 3_000, 15)
        self.assertEqual(r2, "NEGADO")
        _, _, r3 = ex30.avaliar_emprestimo(216_000, 2_000, 30)
        self.assertEqual(r3, "APROVADO")


class TestEx31Divisivel3e5(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex31.classificar(30), "DIVISÍVEL POR 3 E 5")
        self.assertEqual(ex31.classificar(9), "DIVISÍVEL APENAS POR 3")
        self.assertEqual(ex31.classificar(20), "DIVISÍVEL APENAS POR 5")
        self.assertEqual(ex31.classificar(7), "NÃO DIVISÍVEL POR 3 NEM 5")


class TestEx32NumeroNoIntervalo(unittest.TestCase):
    def test_casos(self):
        self.assertTrue(ex32.dentro_do_intervalo(10))
        self.assertTrue(ex32.dentro_do_intervalo(15.5))
        self.assertTrue(ex32.dentro_do_intervalo(20))
        self.assertFalse(ex32.dentro_do_intervalo(20.1))


class TestEx33DiaDaSemana(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex33.dia_da_semana(1), "SEGUNDA-FEIRA")
        self.assertEqual(ex33.dia_da_semana(6), "SÁBADO")
        self.assertEqual(ex33.dia_da_semana(7), "DOMINGO")
        self.assertIsNone(ex33.dia_da_semana(9))


class TestEx34DiasDoMes(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(ex34.dias_do_mes(2, 2024), 29)
        self.assertEqual(ex34.dias_do_mes(2, 2023), 28)
        self.assertEqual(ex34.dias_do_mes(4, 2026), 30)
        self.assertEqual(ex34.dias_do_mes(12, 2026), 31)
        self.assertIsNone(ex34.dias_do_mes(13, 2026))


class TestEx35ValorIngresso(unittest.TestCase):
    def test_casos(self):
        self.assertAlmostEqual(ex35.calcular_valor(10, False), 15.0)
        self.assertAlmostEqual(ex35.calcular_valor(25, True), 15.0)
        self.assertAlmostEqual(ex35.calcular_valor(65, False), 15.0)
        self.assertAlmostEqual(ex35.calcular_valor(30, False), 30.0)


if __name__ == "__main__":
    unittest.main()
