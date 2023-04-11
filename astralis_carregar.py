#Módulo de carregamento do personagem do Sistema Astralis RPG

#Módulos necessários

import pandas
import astralis_classe_personagem as as_p

#Importar os dados puros diretamente do xlsx contendo infos sobre o personagem

def importar_dados(personagem):
    dados_extraidos = None
    dados_extraidos = pandas.read_excel(r'personagens\Ficha ' + personagem + '.xlsx')
    return dados_extraidos

#Transformar os dados puros em um DataFrame para manipulação dos objetos

def converter_dados_importados(ficha):
    dados_convertidos = pandas.DataFrame(ficha).to_dict()
    ficha_refeita = {'Nome':dados_convertidos['Nome'][0], 'Jogador':dados_convertidos['Jogador'][0], 'Força':dados_convertidos['Força'][0], 'Habilidade':dados_convertidos['Habilidade'][0], 'Inteligência':dados_convertidos['Inteligência'][0], 'Resistência':dados_convertidos['Resistência'][0], 'Vitalidade':dados_convertidos['Vitalidade'][0], 'Afinidade Mágica': dados_convertidos['Afinidade Mágica'][0]}
    return ficha_refeita

#Carregamento dos dados do DataFrame para os atributos do personagem

def carregar_dados(nome_personagem):
    dados_importados = importar_dados(nome_personagem)
    ficha_carregada = converter_dados_importados(dados_importados)

    personagem = as_p.Personagem_jogador
    personagem.definir_nome(personagem, ficha_carregada['Nome'])
    personagem.definir_jogador(personagem, ficha_carregada['Jogador'])
    personagem.definir_for(personagem, ficha_carregada['Força'])
    personagem.definir_hab(personagem, ficha_carregada['Habilidade'])
    personagem.definir_int(personagem, ficha_carregada['Inteligência'])
    personagem.definir_res(personagem, ficha_carregada['Resistência'])
    personagem.definir_vit(personagem, ficha_carregada['Vitalidade'])
    personagem.definir_afi(personagem, ficha_carregada['Afinidade Mágica'])
    return personagem