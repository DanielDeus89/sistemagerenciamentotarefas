tarefas = [
    {'titulo': 'Estudar Python', 'descricao': 'Praticar listas e dicionários', 'status': False},
    {'titulo': 'Fazer compras', 'descricao': 'Comprar frutas e legumes', 'status': True},
    {'titulo': 'Organizar gavetas', 'descricao': '', 'status': False}
]

def verificar_lista():
    if not tarefas:
        print("❌ Nenhuma tarefa cadastrada ainda.")
        input('Pressione Enter para voltar ao menu.')
        return False
    return True

def exibir_opcoes():
    print('''
📋 GERENCIADOR DE TAREFAS
1. Adicionar nova tarefa
2. Listar tarefas
3. Atualizar tarefa
4. Marcar tarefa como concluída
5. Excluir tarefa
6. Sair
''')

def adicionar_nova_tarefa():
    while True:
        nome_tarefa = input('Digite o título da tarefa: ').strip()
        if not nome_tarefa:
            print('❌ O título da tarefa não pode estar vazio! Tente novamente.')
            continue

        descricao_tarefa = input('Digite a descrição da tarefa (opcional): ').strip()
        tarefas.append({'titulo': nome_tarefa, 'descricao': descricao_tarefa, 'status': False})
        print(f"\n✅ A tarefa '{nome_tarefa}' foi cadastrada com sucesso!")

        while True:
            continuar = input('Deseja inserir outra tarefa? (s/n): ').strip().lower()
            if continuar == 's':
                break
            elif continuar == 'n':
                print("\n👍 Cadastro concluído! Retornando ao menu principal...")
                return
            else:
                print('❌ Opção inválida! Digite "s" para Sim ou "n" para Não.')

def listar_tarefas():
    if not verificar_lista():
        return

    print('\n📋 Lista de Tarefas 📋')
    print('-' * 80)
    print(f"{'Nº'.ljust(5)} | {'Título'.ljust(20)} | {'Descrição'.ljust(30)} | {'Status'}")
    print('-' * 80)

    for i, tarefa in enumerate(tarefas):
        status = 'Concluída' if tarefa['status'] else 'Pendente'
        descricao = tarefa['descricao'] if tarefa['descricao'] else 'Sem descrição'
        print(f"{str(i + 1).ljust(5)} | {tarefa['titulo'].ljust(20)} | {descricao.ljust(30)} | [{status}]")
    input('\nPressione Enter para voltar ao menu.')

def atualizar_tarefa():
    if not verificar_lista():
        return

    try:
        id_tarefa = int(input('Digite o número da tarefa que deseja atualizar: '))
        if 1 <= id_tarefa <= len(tarefas):
            tarefa = tarefas[id_tarefa - 1]
            print(f"\nInformações atuais: {tarefa}")

            novo_titulo = input('Digite o novo título (ou pressione Enter para manter): ').strip()
            if novo_titulo:
                tarefa['titulo'] = novo_titulo

            nova_descricao = input('Digite a nova descrição (ou pressione Enter para manter): ').strip()
            if nova_descricao:
                tarefa['descricao'] = nova_descricao

            print(f"\n✅ A tarefa '{tarefa['titulo']}' foi atualizada com sucesso!")
        else:
            print("❌ Tarefa não encontrada.")
    except ValueError:
        print("❌ Entrada inválida. Digite um número válido.")
    input('Pressione Enter para voltar ao menu.')

def marcar_tarefa_como_concluida():
    if not verificar_lista():
        return

    try:
        id_tarefa = int(input('Digite o número da tarefa que deseja atualizar: '))
        if 1 <= id_tarefa <= len(tarefas):
            tarefa = tarefas[id_tarefa - 1]
            tarefa['status'] = not tarefa['status']
            status_atual = 'Concluída' if tarefa['status'] else 'Pendente'
            print(f"\n✅ A tarefa '{tarefa['titulo']}' foi marcada como {status_atual}!")
        else:
            print("❌ Tarefa não encontrada.")
    except ValueError:
        print("❌ Entrada inválida. Digite um número válido.")
    input('Pressione Enter para voltar ao menu.')

def excluir_tarefa():
    if not verificar_lista():
        return

    try:
        id_tarefa = int(input('Digite o número da tarefa que deseja excluir: '))
        if 1 <= id_tarefa <= len(tarefas):
            tarefa = tarefas.pop(id_tarefa - 1)
            print(f"\n✅ A tarefa '{tarefa['titulo']}' foi excluída com sucesso!")
        else:
            print("❌ Tarefa não encontrada.")
    except ValueError:
        print("❌ Entrada inválida. Digite um número válido.")
    input('Pressione Enter para voltar ao menu.')

def main():
    while True:
        exibir_opcoes()
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                adicionar_nova_tarefa()
            elif opcao == 2:
                listar_tarefas()
            elif opcao == 3:
                atualizar_tarefa()
            elif opcao == 4:
                marcar_tarefa_como_concluida()
            elif opcao == 5:
                excluir_tarefa()
            elif opcao == 6:
                print("\n👋 Obrigado por usar o Gerenciador de Tarefas! Até a próxima!")
                break
            else:
                print('❌ Opção inválida. Escolha entre 1 e 6.')
        except ValueError:
            print('❌ Insira um número válido.')

if __name__ == '__main__':
    main()
