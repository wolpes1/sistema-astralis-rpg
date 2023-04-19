import astralis_classe_personagem as cl_personagem
import astralis_classe_magia as cl_magia

eliner = cl_personagem.Personagem_jogador('Eliner', 'Renan')
bola_de_fogo = cl_magia.Magia('Bola de fogo', 'Dano', 'Uma bola de fogo saida das mãos do conjurador.', 1, 2)

cura = cl_magia.Magia('Cura', 'Cura', 'Cura.', 1,0,3)

eliner.adicionar_magia(magia = bola_de_fogo.nome)
eliner.adicionar_magia(magia = cura.nome)

print(eliner.__str__())