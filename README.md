# analyze2_log.py
## Análise por Janela de Tempo

Além da contagem de falhas, foi aplicada uma janela de tempo de 5 minutos para
avaliar se múltiplas tentativas de login ocorreram em um curto intervalo.
Falhas repetidas dentro dessa janela foram classificadas como risco elevado,
indicando possível ataque de força bruta.
