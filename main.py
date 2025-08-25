import os
restaurantes = []

def exibir_nome_do_programa():
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


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
    restaurantes.append(nome_restaurante)
    print(f'Restaurante {nome_restaurante}, foi cadastrado com sucesso.')
    retornar_para_menu_principal()


def listar_restaurantes():
    imprimir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes:
        print(restaurante)
    retornar_para_menu_principal()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        # print(f'Voce escolheu a opcao: {opcao_escolhida}')
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
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