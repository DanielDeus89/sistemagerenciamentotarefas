# Sistema de Gerenciamento de Tarefas
---

 Atividade: Gerenciamento de Lista de Tarefas

Crie um programa que gerencie uma lista de tarefas. O programa deve permitir ao usuário adicionar, listar, atualizar, marcar como concluída e excluir tarefas. Ele deve exibir um menu de opções para o usuário interagir.

---

 Funcionalidades

1. Adicionar Nova Tarefa:
   - Permita que o usuário adicione uma tarefa com um título e uma descrição opcional.
   - A tarefa deve começar com o status "Pendente".

2. Listar Tarefas:
   - Exiba todas as tarefas cadastradas, incluindo:
     - Título
     - Descrição
     - Status (Pendente ou Concluída)
   - Mostre as tarefas numeradas.

3. Atualizar Tarefa:
   - Permita que o usuário escolha uma tarefa pelo número.
   - O usuário pode alterar o título ou a descrição.

4. Marcar Tarefa Como Concluída:
   - O usuário pode marcar uma tarefa pelo número como "Concluída".

5. Excluir Tarefa:
   - O usuário pode excluir uma tarefa pelo número.

6. Sair do Programa:
   - Encerre o programa com uma mensagem de despedida.

---

 Estrutura do Menu

Exemplo:
```
📋 GERENCIADOR DE TAREFAS
1. Adicionar nova tarefa
2. Listar tarefas
3. Atualizar tarefa
4. Marcar tarefa como concluída
5. Excluir tarefa
6. Sair

Escolha uma opção: _
```

---

 Regras
- Use uma lista para armazenar as tarefas no formato:
  ```python
  {'titulo': 'Estudar Python', 'descricao': 'Praticar listas e dicionários', 'status': 'Pendente'}
  ```
- Valide as entradas:
  - O título da tarefa não pode estar vazio.
  - O número da tarefa deve ser válido (dentro do intervalo da lista).
- Exiba mensagens claras e amigáveis para o usuário.

---

 Exemplo de Execução

 Adicionar Tarefa
```
Digite o título da tarefa: Estudar Python
Digite a descrição da tarefa (opcional): Praticar listas e dicionários

✅ Tarefa 'Estudar Python' foi adicionada com sucesso!
```

 Listar Tarefas
```
📋 Lista de Tarefas:
1. [Pendente] Estudar Python - Praticar listas e dicionários
2. [Concluída] Fazer compras - Comprar frutas e legumes
```

 Atualizar Tarefa
```
Digite o número da tarefa que deseja atualizar: 1
Digite o novo título (ou pressione Enter para manter): Estudar Python Avançado
Digite a nova descrição (ou pressione Enter para manter): 

✅ Tarefa 'Estudar Python Avançado' foi atualizada com sucesso!
```

 Marcar Como Concluída
```
Digite o número da tarefa que deseja marcar como concluída: 1

✅ Tarefa 'Estudar Python Avançado' foi marcada como concluída!
```

 Excluir Tarefa
```
Digite o número da tarefa que deseja excluir: 2

✅ Tarefa 'Fazer compras' foi excluída com sucesso!
```

---

 Como Começar
1. Crie uma lista chamada `tarefas` para armazenar as tarefas.
2. Implemente funções para cada funcionalidade do menu.
3. Use um loop `while` no `main()` para exibir o menu e permitir que o usuário escolha opções.

---
