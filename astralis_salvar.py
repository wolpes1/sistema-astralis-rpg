import pandas

def converter_dados_personagem(personagem):
    dados_personagem = None
    dados_personagem = {'Nome' : personagem.nome, 'Jogador' : personagem.jogador, 'Força' : personagem.status['Força'], 'Habilidade' : personagem.status['Habilidade'], 'Vitalidade' :  personagem.status['Vitalidade'], 'Resistência': personagem.status['Resistência'], 'Inteligência': personagem.status['Inteligência'], 'Afinidade Mágica': personagem.status["Afinidade Mágica"]}
    return dados_personagem

def salvar_personagem(personagem, nome_personagem):
    dados_convertidos = None
    dados_convertidos = converter_dados_personagem(personagem)
    dataframe_feito = pandas.DataFrame([dados_convertidos])
    dataframe_feito.to_excel(r'personagens/Ficha ' + str(nome_personagem) + '.xlsx')
