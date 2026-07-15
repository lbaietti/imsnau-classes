# Threads e Processos

## Threads (multi-threading):
- Partilham o mesmo espaço de memória 
- Mais leves, mas sujeitas a condições de corrida

## Processos (multi-processing):
- Cada processo tem o seu próprio espaço de memória
- Mais seguros, mas consomem mais recursos

*Exemplo:*
- Usar Thread para operações de I/O e Process para cálculos pesados

from threading import Thread 
from multiprocessing import Process