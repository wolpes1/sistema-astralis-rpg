import astralis_personagem as as_p
import astralis_carregar as carregamento
import os

def limpar_tela():
    os.system('cls')

ficha_alir = carregamento.carregar_dados('Alir')
print(ficha_alir)
print(ficha_alir.nome)
print(ficha_alir.forca)
ficha_alir.definir_for(ficha_alir,50)
print(ficha_alir.forca)
