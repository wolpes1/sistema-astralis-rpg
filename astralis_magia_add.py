#Módulo de salvamento de dados do magia do Sistema Astralis RPG

#Módulos necessários

import os
import pandas
import openpyxl
import astralis_classe_magia as as_m

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


poca_de_lava = as_m.Magia('Poça de Lava', 'Dano em área tipo Fogo', 'Uma poça de lava é conjurada no local desejado, permanecendo como uma armadilha.\nDura 2 turnos.', 2, "Dano: Erro Crítico do oponente: 2x Dano Mágico\nErro Normal: 1x Dano Mágico")
bola_de_fogo = as_m.Magia('Bola de fogo', 'Dano tipo Fogo', 'Lança uma bola de fogo no alvo', 1, 'Dano: Acerto Crítico: 2x Dano mágico\n Acerto Normal: 1x Dano Mágico')

salvar_magia(bola_de_fogo)

salvar_magia(poca_de_lava)
