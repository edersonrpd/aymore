import os

arquivos = os.listdir()
cotacoes = []

excecao = ['aymore.py', '.gitignore', '.git', 'resultados.txt', 'aymore.bat']

try:
    for exc in excecao:

        if exc in excecao:
            arquivos.remove(exc)
        else:
            None

except exc as error:
    print(f'Deu ruim {error}')


def aymore(file: str):
    horario = ''
    data = ''
    dia = ''
    mes = ''
    ano = ''
    hora = ''
    minuto = ''
    produtos = []
    pedido = ''
    qtde = ''
    qtde_produto = []
    cod_cli = ''
    pedido_consulta = ''
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
    print('-' * 50)
    for produto, qtde in zip(produtos, qtde_produto):
        print(f'ID: {produto} Qtd: {qtde}')
    
    return ''


for arquivo in arquivos:
    print(aymore(arquivo))


print(f'{len(arquivos)} arquivos')