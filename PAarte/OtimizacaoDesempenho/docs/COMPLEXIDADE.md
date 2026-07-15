# Tipos de Complexidade

A Complexidade Algorítimca mede o crescimento do tempo de execução ou o uso de memória em função da dimensão de entrada

- O(1) - Constante
- O(log n) - Logarítmica
- O(n) - Linear
- O(n log n) - quase linear
- O(n²) - quadrática (evitar !)
- O(2^n) - Exponencial (catastrófica)

*Exemplo: 0(n)*

def soma(lista):
    total = 0
    for num in lista:
        total += num
    return total
