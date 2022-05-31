import os

diretorio = os.listdir()
arquivos = list()

for arquivo in diretorio:
    if arquivo.startswith('MILF'):
        arquivos.append(arquivo)


def aymore(file: str):

    produtos = []
    qtde_produto = []
    with open(file, mode='r', encoding='utf-8') as fp:
        linha = fp.readline()
        while linha:
            if linha.startswith('0001'):
                cod_cli = int(linha[6:19])
                data = str(linha[20:28])
                dia = data[:2]
                mes = data[2:4]
                ano = data[4:8]
                horario = str(linha[28:32])
                hora = horario[:2]
                minuto = horario[2:4]
                pedido = int(linha[32:38])
                pedido_consulta = int(linha[38:40])
                if pedido_consulta == 0:
                    pedido_consulta = 'Pedido'
                else:
                    pedido_consulta = 'Consulta'

                forma_pagamento = linha[39:44]

            if linha[4:6] == '02':
                posicao = linha[0:4]
                produto = int(linha[6:20])
                produtos.append(produto)
                qtde = int(linha[32:36])
                qtde_produto.append(qtde)
            linha = fp.readline()

    print('-' * 50)
    print(f'|Pedido: {pedido} | Arquivo: {file}|')
    print('-' * 50)
    print(f'Data: {dia}/{mes}/{ano} Hora: {hora}:{minuto}')
    print(f'Cliente: {cod_cli}')
    print(f'Pedido/Consulta: {pedido_consulta}')
    print(f'Forma de Pagamento: {forma_pagamento}')
    print('-' * 50)
    for produto, qtde in zip(produtos, qtde_produto):
        print(f'ID: {produto} Qtd: {qtde}')

    return ''


for arquivo in arquivos:
    aymore(arquivo)

print('-' * 50)
if len(arquivos) == 1:
    print(f'{len(arquivos)} arquivo.')
else:
    print(f'{len(arquivos)} arquivos.')
