import pandas

def converter_dados_personagem(personagem):
    dados_personagem = None
    dados_personagem = {'Nome' : personagem.nome, 'Jogador' : personagem.jogador, 'Força' : personagem.forca, 'Habilidade' : personagem.habilidade, 'Vitalidade' :  personagem.vitalidade, 'Resistência': personagem.resistencia, 'Inteligência': personagem.inteligencia, 'Afinidade Mágica': personagem.afinidade_magica}
    return dados_personagem

def salvar_personagem(personagem, nome_personagem):
    dados_convertidos = None
    dados_convertidos = converter_dados_personagem(personagem)
    dataframe_feito = pandas.DataFrame([dados_convertidos])
    dataframe_feito.to_excel(r'personagens/Ficha ' + nome_personagem + '.xlsx')
