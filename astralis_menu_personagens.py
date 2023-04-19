#Menu de personagens do Sistema Astralis RPG

#Módulos Necessários

import astralis_opcao_carregar_pers as carregamento
import astralis_opcao_salvar_pers as salvamento
import astralis_opcao_criar_pers as criacao
import os

#Limpeza do terminal

def limpar_tela():
    os.system('cls')

#Variáveis previamente inicializadas

opcao_escolhida = None

limpar_tela()

#Loop do programa

while opcao_escolhida != 'sair':

    opcao_escolhida = input("""Bem vinde ao Sistema de criação de personagens Astralis RPG!

    O que deseja fazer?

    criar => Criar Personagem
    salvar => Salvar Personagem
    carregar => Carregar Personagem
    visualizar => Visualizar Personagem
    adicionarm => Adicionar Magia ao personagem
    sair => Sair do programa

    Opção:""").lower()

    match opcao_escolhida:
        
        case 'criar':

            limpar_tela()
            ficha_criada = criacao.criar_personagem()
            limpar_tela()

        case 'salvar':

            limpar_tela()  

            try:
  
                salvamento.salvar_personagem(ficha_criada, ficha_criada.nome)
                input('Salvamento concluido! Pressione Enter para continuar.')
                limpar_tela()
            except:
                input('Não há personagem para salvar!\nPressione enter para continuar.')
                limpar_tela()

        case 'carregar':
            
            limpar_tela()
            nome_salvo = input('Qual o nome do seu personagem?').capitalize()
            limpar_tela()

            try:
                ficha_carregada = carregamento.carregar_dados(nome_salvo)
                input("Carregamento executado com sucesso!")
                limpar_tela()
            except:
                input('Houve um erro no carregamento!\nPressione enter para continuar.')
                limpar_tela()

        case 'adicionarm':

            limpar_tela()
            magia_desejada = input('Qual magia você deseja adicionar?')
            ficha_carregada.adicionar_magia(magia_desejada)
            limpar_tela()
            input('Sua magia foi adicionada!')
            limpar_tela()

        case 'visualizar':

            limpar_tela()

            try:
                print(ficha_carregada.__str__(ficha_carregada))
                input('Pressione Enter para continuar.')
                limpar_tela()
            except:
                input('Não há personagem carregado!\nPressione enter para continuar.')
                limpar_tela()

        case 'sair':

            limpar_tela()
            input('Obrigade por usar este app!\nPressione enter para sair.')
            limpar_tela()
            break

        case _:
            
            limpar_tela()
            input('Esta opção não é válida!\nPressione enter para continuar.')
