#Módulo de carregamento do magia_carregada do Sistema Astralis RPG

#Módulos necessários

import pandas
import astralis_classe_magia as as_m

#Importar os dados puros diretamente do xlsx contendo infos sobre o magia_carregada

def importar_dados(magia_carregada):
    dados_extraidos = None
    dados_extraidos = pandas.read_excel(r'magias\Magia ' + str(magia_carregada) + '.xlsx')
    return dados_extraidos

#Transdescricaomar os dados puros em um DataFrame para manipulação dos objetos

def converter_dados_importados(ficha_magia):
    dados_convertidos = pandas.DataFrame(ficha_magia).to_dict()
    ficha_refeita = {'Nome':dados_convertidos['Nome'][0],'Tipo':dados_convertidos['Tipo'][0],'Descrição':dados_convertidos['Descrição'][0], 'Custo':dados_convertidos['Custo'][0], 'Efeito':dados_convertidos['Efeito'][0]}
    return ficha_refeita

#Carregamento dos dados do DataFrame para os atributos do magia_carregada

def carregar_dados(nome_magia):
    dados_importados = importar_dados(nome_magia)
    ficha_carregada = converter_dados_importados(dados_importados)

    magia_carregada = as_m.Magia
    magia_carregada.definir_nome(magia_carregada, ficha_carregada['Nome'])
    magia_carregada.definir_tipo(magia_carregada, ficha_carregada['Tipo'])
    magia_carregada.definir_descricao(magia_carregada, ficha_carregada['Descrição'])
    magia_carregada.definir_custo(magia_carregada, ficha_carregada['Custo'])
    magia_carregada.definir_efeito(magia_carregada, ficha_carregada['Efeito'])
    return magia_carregada

