import threading
import time
import random

def download(ficheiro):
    tempo = random.randint(1, 3)
    print(f"Iniciar {ficheiro} (vai demorar {tempo}s)...")
    time.sleep(tempo)
    print(f"{ficheiro} concluído !")

ficheiros = [f"ficheiro_{i}" for i in range(1, 6)]
threads = []

for f in ficheiros:
    t = threading.Thread(target = download, args = (f,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Todos os downloads terminaram.")

# - Cada thread representa uma tarefa independente (um download)
# - start() inicia a execução da thread
# - join() garante que o programa só termina quando todas as threads tiverem terminado
# - A função sleep() simula um tempo de espera variável para imitar um download real.
# - Com threading, conseguimos executar várias tarefas I/O simultaneamente sem bloquear a interface