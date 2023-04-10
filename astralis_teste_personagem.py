import astralis_personagem as as_p
import astralis_salvar as salvar
import os

def limpar_tela():
    os.system('cls')

alir = as_p.Personagem_jogador("Fifnier", "Renan")

salvar.salvar_personagem(alir, 'Alir')
