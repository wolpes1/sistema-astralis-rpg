#Módulo de salvamento de dados do personagem do Sistema Astralis RPG

#Módulos necessários

import os
import pandas

#Conversão dos dados de personagem para dict

def converter_dados_personagem(personagem):
    dados_personagem = None
    dados_personagem = {'Nome' : personagem.nome, 'Jogador' : personagem.jogador, 'Força' : personagem.forca, 'Habilidade' : personagem.habilidade, 'Vitalidade' :  personagem.vitalidade, 'Resistência': personagem.resistencia, 'Inteligência': personagem.inteligencia, 'Afinidade Mágica': personagem.afinidade_magica, 'Magias': personagem.magias.str()}
    return dados_personagem

#Salvamento do dict como list em um Dataframe e salvamento do Dataframe em excel

def salvar_personagem(personagem, nome_personagem):
    dados_convertidos = None
    dados_convertidos = converter_dados_personagem(personagem)
    dataframe_feito = pandas.DataFrame([dados_convertidos])
    if os.path.isdir('personagens') == False:
        os.mkdir('./personagens')

    dataframe_feito.to_excel(r'personagens/Ficha ' + nome_personagem + '.xlsx')
