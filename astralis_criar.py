#Módulo de criação de personagem do Sistema Astralis RPG

#Módulos necessários

import os
import astralis_classe_personagem as personagem

#Limpeza do terminal

def limpar_tela():
    os.system('cls')

#Atribuição dos dados do personagem via Terminal

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
    return ficha_personagem