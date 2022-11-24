def origem_destino_iguais(origem, destino, lista_erros):
    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_numero(campo, nome_campo, lista_erros):
    if any(char.isdigit() for char in campo):
        lista_erros[nome_campo] = 'Este campo não aceita números'
