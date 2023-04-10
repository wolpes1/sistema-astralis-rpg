import random
import os

#Sistema de rolagem feito em conjunto por Filipe Botelho e Renan Cavalcante

def rolagem(lados,quant_dados):
    dados = quant_dados
    dados_rolados = []
    while dados != 0:
        dados_rolados.append(random.randint(1,lados))
        dados -= 1
    return dados_rolados

def processar_mensagem(mensagem):
    mensagem_separada = mensagem.split(" ",1)
    comando = mensagem_separada[0]
    dados_e_lados = mensagem_separada[1].lower().split("d")
    return dados_e_lados

mensagem_recebida = input("Qual sua rolagem? (Utilize /r (número de dados)D(número de lados))\n")

os.system('cls')

lados_e_dados_recebidos = processar_mensagem(mensagem_recebida)
dados = int(lados_e_dados_recebidos[0])
lados = int(lados_e_dados_recebidos[1])

print(f"Os dados rolados foram: {rolagem(lados, dados)}")
