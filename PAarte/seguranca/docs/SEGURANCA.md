# Princípios de Segurança em Aplicações

## 1. Confidencialidade
- Garantir que apenas os utilizadores autorizados acedem aos dados

## 2. Integridade
- Assegurar que os dados não são alterados indevidamente

## 3. Disponibilidade
- O sistema deve estar disponível para quem precisa dele

## 4. Autenticação
- Verificar a identidade dos utilizadores

## 5. Autorização
- Conceder acesso apenas a operações permitidas

## 6. Registo (_logging_) e auditoria
- Rastrear ações para diagnóstico e responsabilização

# Vulnerabilidades comuns 

*Nome* | *Descrição* | *Exemplo*
SQL Injection | Injeção de comandos SQL via campos de input | ' OR 1 = 1 --
XSS (Cross-site Scripting) | Injeção de scripts maliciosos num site | <script> alert(1)</script>
CSRF | Execução de ações indevidas por utilizadores autenticados | Envio automático de formulário
Command Injection | Execução de comandos no servidor via input | rm -rf/

# Prevenção de Vulnerabilidades

*Sanitização de Input:*
- Remover ou escapar caracteres perigosos
- Usar expressões regulares e listas de permissões

*Prepared Statments:*
- Impedir SQL Injection ao separar lógica e dados

_cursor.execute("SELECT * FROM users WHERE email = ?", (email,))_

*Escapar html:*
- Evitar XSS ao codificar os dados antes de mostrar no front-end

*Tokens CSRF:*
- Impedir envio de pedidos não autorizados em sessões autenticadas

*Evitar execução dinâmica:*
- Não usar _eval()_, _exec()_, _os.system()_ com input direto do utilizador

# Validação de Dados (Client-Side vs. Server-Side)

*Validação Cliente-Side (JS, HTML)*
- Boa experiência para o utilizador
- Pode ser facilmente contornada

*Validação Server-Side(Python, PHP, etc...)*
- Obrigatória !
- Responsável por verificar regras de negócio, segurança e integridade.

*Exemplo com Python (regex):*

import re
email = "teste@dominio.pt"
if re.match(r"[^@]+@[^@]+.\[^@]+", email):
    print("Email válido")



