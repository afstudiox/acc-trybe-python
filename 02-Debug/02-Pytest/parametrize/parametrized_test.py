import pytest

from main import mean


@pytest.mark.parametrize(
    "input_numbers, expected_result",  # 1
    [  # 2
        ([1, 2, 3, 4, 5], 3.0),  # 3
        ([2.5, 3.75, 1.25, 4], 2.875),
    ],
)
def test_mean(input_numbers, expected_result):  # 4
    assert mean(input_numbers) == expected_result


def test_mean_fail():  # 5
    with pytest.raises(ZeroDivisionError):
        mean([])


'''
1 - O primeiro argumento, que poderia ser uma lista: [“input_numbers”, “expected_result”].
2 - O segundo argumento, uma lista de tuplas, na qual cada tupla da lista é uma rodada a mais do teste, e cada parâmetro declarado no primeiro argumento precisa ter um valor correspondente na tupla.
3 - Primeira tupla com dois parâmetros: input_numbers (lista de números) e expected_result (a média esperada para o teste).
4 - Os parâmetros declarados no primeiro argumento de parametrize devem ser recebidos pela função de teste.
5 - O ideal é parametrizar somente os testes que verificam um mesmo comportamento, mudando apenas os valores: quando o comportamento esperado é diferente, o ideal é criar um novo teste.
'''
