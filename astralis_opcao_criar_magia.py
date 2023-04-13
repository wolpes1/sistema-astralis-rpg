import os
import astralis_classe_magia as as_m
import astralis_opcao_salvar_magia as criar_magia

def limpar_tela():
    os.system('cls')

def execucao():
    limpar_tela()
    nome_magia = input('Qual o nome da nova magia?\n')
    limpar_tela()
    tipo_magia = input('E qual o tipo de magia?\n')
    limpar_tela()
    descricao_magia = input('Qual a descrição da magia?\n')
    limpar_tela()
    custo_magia = int(input('Qual o custo em mana da magia?\n'))
    limpar_tela()
    efeito_magia = input('Qual o efeito da magia?\n')
    limpar_tela()
    print('Adicionando magia ao livro...\n')
    nova_magia = as_m.Magia
    nova_magia.definir_nome(nova_magia, nome_magia)
    nova_magia.definir_tipo(nova_magia, tipo_magia)
    nova_magia.definir_descricao(nova_magia, descricao_magia)
    nova_magia.definir_custo(nova_magia, custo_magia)
    nova_magia.definir_efeito(nova_magia, efeito_magia)
    criar_magia.salvar_magia(nova_magia)
    input('Magia adicionada ao livro!\nPressione Enter para continuar')
    limpar_tela()