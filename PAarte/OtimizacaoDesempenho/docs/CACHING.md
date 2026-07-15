# Caching: Armazenamento de Resultados

## Definição
- Caching é a *técnica de guardar resultados* de operações dispendiosas, para não repetir cálculos.

## Vantagem
- Redução drástica de tempo de execução em funções recursivas e chamadas repetidas.

*Ex:*

from functools import lru_cache

@lru_cache(maxsize = None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)