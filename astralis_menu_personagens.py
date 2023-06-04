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

    Opção:""").lower()

    match opcao_escolhida:
        
        case 'criar':

            limpar_tela()
            ficha_criada = criacao.criar_personagem()
            limpar_tela()

        case 'salvar':

            limpar_tela()    
            salvamento.salvar_personagem(ficha_criada, ficha_criada.nome)
            input('Salvamento concluido! Pressione Enter para continuar.')
            limpar_tela()

        case 'carregar':
            
            limpar_tela()
            nome_salvo = input('Qual o nome do seu personagem?').capitalize()
            limpar_tela()

            ficha_carregada = carregamento.carregar_dados(nome_salvo)
            input("Carregamento executado com sucesso!")
            limpar_tela()

        case 'visualizar':

            limpar_tela()
            print(ficha_carregada.__str__(ficha_carregada))
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
