#Módulo de salvamento de dados do magia do Sistema Astralis RPG

#Módulos necessários

import os
import pandas

#Conversão dos dados de magia para dict

def converter_dados_magia(magia):
    dados_magia = None
    dados_magia = {'Nome' : magia.nome, 'Tipo' : magia.tipo, 'Descrição' : magia.descricao, "Custo" : magia.custo, "Efeito" : magia.efeito}
    return dados_magia

#Salvamento do dict como list em um Dataframe e salvamento do Dataframe em excel

def salvar_magia(magia):
    dados_convertidos = None
    dados_convertidos = converter_dados_magia(magia)
    dataframe_feito = pandas.DataFrame([dados_convertidos])

    if os.path.isdir('magias') == False:
        os.mkdir('./magias')

    dataframe_feito.to_excel('./magias/Magia ' + str(magia.nome) + '.xlsx')




