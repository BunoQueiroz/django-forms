def origem_destino_iguais(origem, destino, lista_erros):
    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_numero(campo, nome_campo, lista_erros):
    if any(char.isdigit() for char in campo):
        lista_erros[nome_campo] = 'Este campo não aceita números'

def data_ida_maior_data_volta(data_ida, data_volta, lista_erros):
    if data_ida > data_volta:
        lista_erros['data_volta'] = 'Você não pode voltar antes de ir'

def data_ida_menor_hoje(data_ida, data_atual, lista_erros):
    if data_ida < data_atual:
        lista_erros['data_ida'] = 'Você não pode ir antes que hoje'
