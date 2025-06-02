# Sistema de Abertura de Chamados

Este é um sistema simples de abertura, acompanhamento e fechamento de chamados, desenvolvido em Python. Permite registrar chamados, filtrar por urgência, fechar chamados por ID e visualizar estatísticas básicas.

## Funcionalidades

- Abrir novos chamados com setor, descrição e urgência.
- Listar todos os chamados ou apenas os abertos.
- Filtrar chamados por nível de urgência.
- Fechar chamados abertos marcando-os como resolvidos.
- Visualizar contagem de chamados abertos, resolvidos e total.

## Como usar

1. **Clone o repositório:**
   ```
   git clone https://github.com/seu-usuario/sistema-chamados.git
   cd sistema-chamados
   ```

2. **Execute o sistema:**
   ```
   python sistema_chamados.py
   ```

3. **Siga as instruções do menu interativo no terminal.**

## Requisitos

- Python 3.7 ou superior
- Sistema operacional que suporte o comando `cls` (Windows). Para Linux/MacOS, altere `os.system("cls")` para `os.system("clear")` no código.

## Observações

- Os chamados são mantidos apenas em memória (não persistem após fechar o programa).
- Ideal para fins didáticos e pequenas demonstrações de lógica de programação.

---
