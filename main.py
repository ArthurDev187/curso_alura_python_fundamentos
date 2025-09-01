import os
restaurantes = [
    {'nome': 'Restaurante da tia Raimunda',
     'categoria': 'Comida caseira', 
     'ativo': True}
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


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def atualizar_restaurante():
    imprimir_subtitulo('Vamos atualizar o restaurante')
    nome_restaurante_atualizar = input('Digite o nome do restaurante que deseja atualizar: ')
    for restaurante in restaurantes:
        if nome_restaurante_atualizar.lower() == restaurante['nome'].lower():
            try: 
                print('1=nome, 2=categoria, 3=ativo')
                qual_atualizar = int(input('Digite o numero do item que deseja atualizar: '))
                match qual_atualizar:
                    case 1:
                        nome_antigo = restaurante['nome']
                        nome_novo = input('Digite o novo nome do restaurante: ')
                        restaurante['nome'] = nome_novo
                        print(f'O restaurante de nome: {nome_antigo}, teve o nome atualizado para: {nome_novo}')
            except:
                pass

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
    dados_restaurante = {'Nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
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