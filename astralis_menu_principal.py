import astralis_carregar as carregamento
import astralis_salvar as salvamento
import astralis_personagem as personagem
import astralis_rolagem as rolagem_dados
import os

def limpar_tela():
    os.system('cls')

opcao_escolhida = None

ficha_personagem = None

ficha_carregada = None

limpar_tela()

while opcao_escolhida != 'sair':

    opcao_escolhida = input("""Bem vinde ao Astralis RPG!
    O que deseja fazer?
    criar => Criar Personagem
    salvar => Salvar Personagem
    carregar => Carregar Personagem
    visualizar => Visualizar Personagem
    rolar => Rolar dados
    sair => Sair do programa

    Opção:""").lower()

    match opcao_escolhida:
        case 'criar':
            limpar_tela()
            nome_personagem = input('Qual será o nome do personagem?')
            limpar_tela()
            jogador_personagem = input('E quem será o jogador controlando o personagem?')
            limpar_tela()
            for_personagem = int(input('E seus niveis de:\nForça:'))
            limpar_tela()
            hab_personagem = int(input('E seus niveis de:\nHabilidade:'))
            limpar_tela()
            res_personagem = int(input('E seus niveis de:\nResistência:'))
            limpar_tela()
            vit_personagem = int(input('E seus niveis de:\nVitalidade:'))
            limpar_tela()
            int_personagem = int(input('E seus niveis de:\nInteligência:'))
            limpar_tela()
            afi_personagem = int(input('E seus niveis de:\nAfinidade Mágica:'))
            limpar_tela()
            print('Definindo personagem...')
            ficha_personagem = personagem.Personagem_jogador
            ficha_personagem.definir_nome(ficha_personagem, nome_personagem)
            ficha_personagem.definir_jogador(ficha_personagem, jogador_personagem)
            ficha_personagem.definir_for(ficha_personagem, for_personagem)
            ficha_personagem.definir_hab(ficha_personagem, hab_personagem)
            ficha_personagem.definir_int(ficha_personagem, int_personagem)
            ficha_personagem.definir_res(ficha_personagem, res_personagem)
            ficha_personagem.definir_vit(ficha_personagem, vit_personagem)
            ficha_personagem.definir_afi(ficha_personagem, afi_personagem)
            input('Pressione enter para continuar...')
            limpar_tela()
            print('Personagem definido!')
            print(ficha_personagem.__str__(ficha_personagem))
            input('Pressione enter para finalizar.')

        case 'salvar':
            if ficha_personagem == None:
                input('Não existe ficha! Crie uma para poder salvar.\nPressione enter para continuar.')
                limpar_tela()
            else:
                salvamento.salvar_personagem(ficha_personagem, ficha_personagem.nome)
                input('Salvamento concluido! Pressione Enter para continuar.')
                limpar_tela()

        case 'carregar':
            nome_salvo = input('Qual o nome do seu personagem?').capitalize()

            try:
                ficha_carregada = carregamento.carregar_dados(nome_salvo)
                input("Carregamento executado com sucesso!")
                ficha_personagem = ficha_carregada
                limpar_tela()
            except:
                input('Houve um erro no carregamento!\nPressione enter para continuar.')
                limpar_tela()

        case 'visualizar':
            print(ficha_personagem.__str__(ficha_personagem))
            input('Pressione Enter para continuar.')


        case 'rolar':
            rolagem_dados.execucao()
            input('Pressione Enter para continuar.')
            limpar_tela()

        case 'sair':
            input('Obrigade por usar este app!\nPressione enter para sair.')
            limpar_tela()
            break

        case _:
            input('Esta opção não é válida!\nPressione enter para continuar.')
