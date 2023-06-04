#Módulo de criação de personagem do Sistema Astralis RPG

#Módulos necessários

import os
import astralis_classe_personagem as personagem

#Limpeza do terminal

def limpar_tela():
    os.system('cls')

#Atribuição dos dados do personagem via Terminal

frase_pericia = 'O personagem tem treino em'

def criar_personagem():
    nome_personagem = input('Qual será o nome do personagem?\n')
    limpar_tela()
    jogador_personagem = input('E quem será o jogador controlando o personagem?\n')
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
    ficha_personagem = personagem.Personagem_jogador(nome_personagem,jogador_personagem,for_personagem,hab_personagem,res_personagem,vit_personagem,int_personagem,afi_personagem)
    input('Pressione enter para continuar...')
    limpar_tela()
    print('Personagem definido!')
    print(ficha_personagem.__str__())
    input('Pressione enter para finalizar.')
    return ficha_personagem