#Classe de Magias para o Sistema Astralis RPG

class Magia:

    def __init__(self, nome = str, tipo = str, descricao = str, dano = None, efeito = None):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.dano = dano
        self.efeito = efeito

    def __str__(self):

        tipo = None

        match (self.tipo).capitalize():

            case 'Dano':
                tipo = f'Dano: {self.dano}'
            case 'Efeito':
                tipo = f'Efeito: {self.efeito}'
            case 'Ambos':
                tipo = f'Dano: {self.dano}\nEfeito: {self.efeito}'
            case _:
                input('Esta opção não é válida!\nPressione Enter para continuar.')

        return f"Magia {self.nome}\nTipo: {self.tipo}\nDescrição: {self.descricao}\n{tipo}"


    