# Assincronismo e Event Loop

## Assincronismo (async/await)
- Ideal para tarefas de I/O: redes, bases de dados, ficheiros
- Usa um event loop para alternar entre tarefas sem bloquear a execução

*Ex:*
- Não usa threads nem processos, apenas suspende e retoma a tarefa de forma eficiente
```
import asyncio

async def tarefa():
    await asyncio.sleep(1)
    print("Concluída")

asyncio.run(tarefa())
``` 
