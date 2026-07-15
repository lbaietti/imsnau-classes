#Criar um sistema de gestão de tarefas simples com:
# - adição de tarefas com prioridade;
# - listagem de tarefas pendentes;
# - remoção de tarefas concluídas;

# Cada tarefa tem:
# - uma descrição;
# - um nível de prioridade;
# - um estado de concluído (true/false);

# OBJETIVO:
# Implementar o mesmo sistema com 2 paradigmas:
# - POO
# - Programação Funcional

# ====================== ENCAPSULAMENTO =========================

# Encapsula os dados e comportamento de uma tarefa

class Tarefa:
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        estado = "OK" if self.concluida else "Wait"
        return f"{estado} {self.descricao} (Prioridade: {self.prioridade})"



# Gere uma listqa de tarefas com métodos específicos

class GestorTarefas:

    def __init__(self):
        self.tarefas = []
    
    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_pendentes(self):
        for t in self.tarefas:
            if not t.concluida:
                print(t)

    def remover_concluidas(self):
        self.tarefas = [t for t in self.tarefas if not t.concluida]


#Criar gestor de tarefas
gestor = GestorTarefas()

# Adicionar tarefas
gestor.adicionar(Tarefa("Estudar programação", 2))
gestor.adicionar(Tarefa("Fazer exercício físico", 1))

# Listar pendentes

print("Pendentes: ")
gestor.listar_pendentes()

#concluir tarefa

gestor.tarefas[0].concluir()

# Remover concluídas

gestor.remover_concluidas()

print("\n Após remoção de concluídas: ")
gestor.listar_pendentes()
