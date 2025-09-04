import os
restaurantes = [
     {
        'id': 1,
        'nome': 'Restaurante tia Raimunda',
        'categoria': 'Comida caseira', 
        'ativo': True
     }, 
     {
         'id': 2,
         'nome': 'Dona Mada',
         'categoria': 'Comida nordestina',
         'ativo': False
     }
]

def exibir_nome_do_programa():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)



def finalizar_app():
    os.system('cls')
    print('Finalizando app\n')


def retornar_para_menu_principal():
    input('\nDigite qualquer tecla para voltar para o menu principal.\n')
    main()


def opcao_invalida():
    print('Opcao invalida\n')
    retornar_para_menu_principal()


def imprimir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()


def cadastrar_restaurante():
    imprimir_subtitulo('Cadastrando restaurante')
    nome_restaurante = input('Digite o nome do restaurante que voce deseja cadastrar: ')
    categoria_restaurante = input('Digite a categoria do restaurante: ')
    id_restaurante = int(len(restaurantes) + 1)
    dados_restaurante = {'id': id_restaurante, 'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante}, foi cadastrado com sucesso.')
    retornar_para_menu_principal()


def listar_restaurantes():
    imprimir_subtitulo('Listando restaurantes')
    print(f'{'\033[1mID':^20} | {'Nome restaurante':^40} | {'Categoria restaurante':^40} | {'Ativo':^20}\033[0m')
    print('=' * 170)
    for restaurante in restaurantes:
        id_rest = restaurante['id']
        nome_rest = restaurante['nome']
        categ_rest = restaurante['categoria']
        ativo_rest = 'Sim' if restaurante['ativo'] else 'Nao'
        print(f'{id_rest:^16} | {nome_rest:^40} | {categ_rest:^40} | {ativo_rest:^20}')
        print('-' * 170)
    retornar_para_menu_principal()


def ativar_restaurante():
    imprimir_subtitulo('Ativando Restaurante')
    id_a_ser_ativado = input('Digite o ID do restaurante a ser ativado: ')
    for restaurante in restaurantes:
        if int(id_a_ser_ativado) == int(restaurante['id']):
            restaurante['ativo'] = not bool(restaurante['ativo'])
            mensagem = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'Restaurante {restaurante['nome']} foi {mensagem} com sucesso.')
    
    retornar_para_menu_principal()



def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Editar restaurante')
    print('5. Sair\n')


def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opcao: '))
    # print(f'Voce escolheu a opcao: {opcao_escolhida}')
    if opcao_escolhida == 1:
        # Cadastrar restaurantes
        cadastrar_restaurante()
    elif opcao_escolhida == 2:
        # Listar restaurantes
        listar_restaurantes()
    elif opcao_escolhida == 3:
        # Ativar restaurantes
        ativar_restaurante()
    elif opcao_escolhida == 4:
        # Editar restaurantes
        print('Atualizar restaurante')
        retornar_para_menu_principal()
    elif opcao_escolhida == 5:
        # Sair
        finalizar_app()
    else:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()




if __name__ ==  '__main__':
    main()


# criar funcao cadastrar restaurantes
# criar funcao listar restaurantes
# criar funcao que retorna ao menu principal