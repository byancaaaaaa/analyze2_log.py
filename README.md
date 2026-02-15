## Análise por Janela de Tempo

O script aplica uma janela de tempo de 5 minutos para correlacionar tentativas
de login com falha. Quando três ou mais falhas ocorrem nesse intervalo para o
mesmo usuário e endereço IP, o evento é classificado como risco elevado.

Os eventos foram correlacionados por janela de tempo e consolidados para apresentar apenas o maior número de falhas por usuário e endereço IP
