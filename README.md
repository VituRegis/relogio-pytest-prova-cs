*Implementação de algumas funções de manipulação de horários, usando pytest para testes automatizados, questão de uma prova de Construção de Software*

## Execução dos testes

Requer Python 3.10 ou superior. Instale as dependências de desenvolvimento e execute toda a suíte:

```sh
python -m pip install -r requirements-dev.txt
python -m pytest
```

O `pytest.ini` inclui tanto os oito testes originais em `relogio.py` quanto os casos de regressão em `test_relogio.py`.

## Regras e cobertura

- As funções recebem horários válidos no formato `HH:MM:SS`, entre `00:00:00` e `23:59:59`.
- Soma e subtração retornam um horário em um ciclo de 24 horas; diferenças negativas também são normalizadas nesse ciclo.
- A comparação retorna o maior horário do dia; no empate, retorna o próprio horário.
- `tique` avança um segundo, incluindo a passagem de `23:59:59` para `00:00:00`.

Os 32 testes cobrem transporte de segundos e minutos, empréstimos na subtração, virada do dia e comparação com empate. Os resultados esperados são valores fixos calculados independentemente da implementação.

Exemplos corrigidos: `22:43:45 + 10:28:00 = 09:11:45` e `22:43:45 - 23:46:51 = 22:56:54`.
