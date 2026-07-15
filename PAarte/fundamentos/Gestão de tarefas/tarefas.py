# Mesmo programa, no entanto utilizando a prática de Programação Funcional

# Cada tarefa é representada como um dicionário imutável, ao invés de um objeto

def criar_tarefa(descricao, prioridade):
    return {
        "descricao": descricao,
        "prioridade": prioridade,
        "concluida": False
    }

def listar_pendentes(tarefas):
    return list(filter(lambda t: not t["concluida"], tarefas))

def remover_concluidas(tarefas):
    return list(filter(lambda t: not t["concluida"], tarefas))

# As funções são puras (Sempre que possível)
# Ou seja, não modificam dados diretamente, mas retornam cópias
# Usamos filter() para filtrar tarefas pendentes ou remover concluidas

# Versão Pura / Funcional

def concluir_tarefa(tarefas, index_a_concluir):
    nova_lista = []

    for index, tarefa in enumerate(tarefas):
        if index == index_a_concluir:

            # Cria uma cópia da tarefa com o estado alterado
            tarefa_atualizada = tarefa.copy()
            tarefa_atualizada['concluida'] = True
            nova_lista.append(tarefa_atualizada)
        
        else:

            # Adiciona a tarefa original sem alterações
            nova_lista.append(tarefa)
        return nova_lista

# A abordagem é mais concsa, mas enos estruturada, o que pode dificultar a legibilidade e escalabilidade

# Criar lista de tarefas
tarefas = []
tarefas.append(criar_tarefa("Estudar programação", 2))
tarefas.append(criar_tarefa("Fazer exercício físico", 1))

# Concluir primeira tarefa
tarefas = concluir_tarefa(tarefas, 0)

# Remover Concluídas
tarefas = remover_concluidas(tarefas)

# Listar pendentes
for t in listar_pendentes(tarefas):
    print(f"{t['descricao']} (Prioridade: {t['prioridade']})")