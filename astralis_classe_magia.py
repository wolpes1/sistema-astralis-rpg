class Magia:

    def __init__(self, nome = str, tipo = str , descricao = str, custo = int, dano = int, cura = int):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.custo = custo
        self.dano = dano
        self.cura = cura

    def __str__(self):

        match self.tipo:

            case 'dano':
                return f'Magia {self.nome}\nTipo: {self.tipo}\nDescrição: {self.descricao}\nCusto em Mana: {self.custo}\nDano mágico: {self.dano}'
            case 'cura':
                return f'Magia {self.nome}\nTipo: {self.tipo}\nDescrição: {self.descricao}\nCusto em Mana: {self.custo}\nCura: {self.cura}'
            case _:
                return f'Magia {self.nome}\nTipo: {self.tipo}\nDescrição: {self.descricao}\nCusto em Mana: {self.custo}'
            
