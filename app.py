

tarefas = [
    {'titulo': 'Estudar Python', 'descricao': 'Praticar listas e dicionários', 'status': False},
    {'titulo': 'Fazer compras', 'descricao': 'Comprar frutas e legumes', 'status': True},
    {'titulo': 'Organizar gavetas', 'descricao': '', 'status': False}
]

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
        nome_tarefa = input('Digite o título da tarefa:')
        if not nome_tarefa:
            print('❌ A tarefa não pode estar vazio! Tente novamente.')
            continue

        descricao_tarefa = input('Digite a descrição da tarefa (opcional):')

        dados_tarefa = {'titulo': nome_tarefa, 'descricao':descricao_tarefa, 'status':False}

        tarefas.append(dados_tarefa)
        print(f"\n✅ A tarefa '{nome_tarefa}' foi cadastrado com sucesso!")


        while True:
            continuar = input('Deseja inserir outro Tarefa? (s/n): ').strip().lower()
            if continuar == 's':
                break
            elif continuar == 'n':
                print("\n👍 Cadastro concluído! Retornando ao menu principal...")
                return
            else:
                print('❌ Opção inválida! Digite "s" para Sim ou "n" para Não.')

def listar_tarefas():
    print('Listar tarefas')
    if not tarefas:
        print("❌ Nenhum Tarefa cadastrado ainda.")
        input('Pressione Enter para voltar ao menu.')
        return

    print('📋 Lista de Tarefas 📋')
    print('-' * 80)
    print(f"{'Nº'.ljust(5)} | {'Título'.ljust(20)} | {'Descrição'.ljust(30)} | {'Status'}")
    print('-' * 80)
    for i, tarefa in enumerate(tarefas):
        status = 'Concluída' if tarefa['status'] else 'Pendente'
        descricao = tarefa['descricao'] if tarefa['descricao']  else 'Sem descricao'

        print(f'{str(i+1).ljust(5)} | {tarefa["titulo"].ljust(20)} | {descricao.ljust(30)} | [{status}]')

    print('')
    input('Pressione Enter para voltar ao menu.')

def atualizar_tarefa():
    print('Atualizar tarefa')

def marcar_tarefa_como_concluída():
    print('Marcar tarefa como concluída')

def excluir_tarefa():
    print('Excluir tarefa')


def main():
    while True:
        exibir_opcoes()
        try:
            opcao = int(input('Escolha uma opção: _'))
            if opcao == 1:
                adicionar_nova_tarefa()
            elif opcao == 2:
                listar_tarefas()
            elif opcao == 3:
                atualizar_tarefa()
            elif opcao == 4:
                marcar_tarefa_como_concluída()
            elif opcao == 5:
                excluir_tarefa()
            elif opcao == 6:
                print("\n👋 Obrigado por usar o Gerenciamento de Filmes! Até a próxima!")
                break
            else:
                print('❌ Opção inválida. Escolha entre 1 e 6.')
                input('Pressione Enter para voltar ao menu.')
        except ValueError:
            print('❌ Insira um número válido.')
            input('Pressione Enter para voltar ao menu.')



if __name__ == '__main__':
    main()