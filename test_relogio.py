"""Casos de regressão com resultados calculados independentemente."""

import pytest

from relogio import compara_horario, soma_horario, subtrai_horario, tique


@pytest.mark.parametrize("primeiro, segundo, esperado", [
    ("22:43:45", "10:28:00", "09:11:45"),
    ("00:30:00", "00:30:00", "01:00:00"),
    ("00:59:59", "00:00:01", "01:00:00"),
    ("23:59:59", "00:00:01", "00:00:00"),
    ("23:59:59", "23:59:59", "23:59:58"),
    ("00:00:00", "00:00:00", "00:00:00"),
])
def test_soma_normaliza_segundos_minutos_e_virada_do_dia(primeiro, segundo, esperado):
    assert soma_horario(primeiro, segundo) == esperado


@pytest.mark.parametrize("primeiro, segundo, esperado", [
    ("22:43:45", "23:46:51", "22:56:54"),
    ("12:30:00", "00:00:01", "12:29:59"),
    ("12:00:00", "00:01:00", "11:59:00"),
    ("00:00:00", "00:00:01", "23:59:59"),
    ("00:00:00", "23:59:59", "00:00:01"),
    ("12:30:45", "12:30:45", "00:00:00"),
    ("22:43:45", "02:03:25", "20:40:20"),
])
def test_subtracao_trata_emprestimos_e_retorna_horario_em_24_horas(primeiro, segundo, esperado):
    assert subtrai_horario(primeiro, segundo) == esperado


@pytest.mark.parametrize("primeiro, segundo, esperado", [
    ("12:30:45", "12:30:45", "12:30:45"),
    ("00:00:00", "00:00:00", "00:00:00"),
    ("23:00:00", "01:59:59", "23:00:00"),
    ("01:59:59", "23:00:00", "23:00:00"),
    ("12:31:00", "12:30:59", "12:31:00"),
    ("12:30:01", "12:30:02", "12:30:02"),
    ("12:30:02", "12:30:01", "12:30:02"),
])
def test_comparacao_retorna_maior_horario_inclusive_em_empate(primeiro, segundo, esperado):
    assert compara_horario(primeiro, segundo) == esperado


@pytest.mark.parametrize("horario, esperado", [
    ("00:00:00", "00:00:01"),
    ("12:30:59", "12:31:00"),
    ("12:59:59", "13:00:00"),
    ("23:59:59", "00:00:00"),
])
def test_tique_incrementa_um_segundo_com_viradas(horario, esperado):
    assert tique(horario) == esperado
