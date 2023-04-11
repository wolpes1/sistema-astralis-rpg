import astralis_carregar as carregamento
import astralis_salvar as salvamento
import astralis_rolagem as rolagem_dados
import astralis_criar as criar
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
            ficha_personagem = criar.criar_personagem()
            limpar_tela()
        case 'salvar':

            limpar_tela()  

            try:
  
                salvamento.salvar_personagem(ficha_personagem, ficha_personagem.nome)
                input('Salvamento concluido! Pressione Enter para continuar.')
                limpar_tela()
            except:
                input('Não há personagem para salvar!\nPressione enter para continuar.')

        case 'carregar':
            
            limpar_tela()
            nome_salvo = input('Qual o nome do seu personagem?').capitalize()
            limpar_tela()

            try:
                ficha_carregada = carregamento.carregar_dados(nome_salvo)
                input("Carregamento executado com sucesso!")
                ficha_personagem = ficha_carregada
                limpar_tela()
            except:
                input('Houve um erro no carregamento!\nPressione enter para continuar.')
                limpar_tela()

        case 'visualizar':
            limpar_tela()
            try:
                print(ficha_personagem.__str__(ficha_personagem))
                input('Pressione Enter para continuar.')
                limpar_tela()
            except:
                input('Não há personagem carregado!\nPressione enter para continuar.')


        case 'rolar':
            limpar_tela()
            rolagem_dados.execucao()
            input('Pressione Enter para continuar.')
            limpar_tela()

        case 'sair':
            limpar_tela()
            input('Obrigade por usar este app!\nPressione enter para sair.')
            limpar_tela()
            break

        case _:
            limpar_tela()
            input('Esta opção não é válida!\nPressione enter para continuar.')
