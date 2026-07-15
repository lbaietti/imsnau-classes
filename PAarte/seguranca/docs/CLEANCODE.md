# Código Limpo e Legível 

## Princípios Fundamentais
- Clareza > Esperteza: Prioriza a compreensão por outros programadores
- Nomeação Significativa: 
    - Evita nomes genéricos (x, temp, var)
    - Ex: total_compras, obter_id_utilizador()
- Funções curtas e coesas:
    - Uma função deve fazer uma única coisa
- Comentários úteis (não redundantes)
    - Explicam porquê, não o quê

### Mau exemplo:
    def x(a, b): return a + b

### Bom exemplo
    def somar_preco_com_taxa(preco, taxa): return preco + taxa

## Testes de Código
- Unitários: Testam funções isoladas
- Integração: Verificam se os componentes funcionam em conjunto 
- Funcionais: Testam comportamentos reais da aplicação

*Exemplo com _Unittest_*

```
import unittest

def soma(a, b): return a + b

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
```

## Documentação e Manutenção

*Documentar é investir no futuro*
- Descreve o funcionamento do código
- Facilita o onboarding e debugging

*Boas Práticas*
- Docstrings em funções/classes
- README.md para o projeto
- Atualizar comentários com o código

*Exemplo de docstring*
```
def calcular_imc(peso, altura):
    """ Calcula o Índice de Massa Corporal (IMC)"""
    return peso / (altura ** 2)
```

## Controlo de versões com GIT

*Porquê usar GIT ?*
- Histórico de alterações 
- Trabalho em equipa
- Reversões de erros
- Ramificações (branches) para novas funcionalidades

*Comandos Básicos*
- Ver QRF - Git (Anexos)

*Boas Práticas em GIT*
- Ver QRF - Git (Anexos)