import os

arquivos = os.listdir()
cotacoes = []

if arquivos


if ('sample_data') in arquivos:
  arquivos.remove('sample_data')
if ('.config') in arquivos:
  arquivos.remove('.config') 
if('./aymore.py'):
  arquivos.remove('aymore.py')
else:
  None
  

def aymore(file:str):
  data = ''
  hora = ''
  produtos = []
  pedido = ''
  qtde = ''
  qtde_produto = []
  pedido_consulta = ''
  with open(file, mode='r', encoding='utf-8') as fp:
    linha = fp.readline()
    while linha:
      if linha.startswith('0001'):
        data = str(linha[20:28])
        hora = str(linha[28:32])
        pedido = int(linha[32:38])
        pedido_consulta = int(linha[38:40])
        
      if linha[4:6] == '02':
        posicao = linha[0:4]
        produto = int(linha[6:20] )
        produtos.append(produto)
        qtde = int(linha[32:36])
        qtde_produto.append(qtde)
      linha = fp.readline()

  print(f'Pedido: {pedido}')
  print(f'Data: {data}')
  print(f'Hora: {hora}')
  print(f'Pedido consulta: {pedido_consulta}')
  print('-' * 32 )
  for produto, qtde in zip(produtos, qtde_produto):
    print(f'ID: {produto} Qtd: {qtde}')
  print('-' * 32 )
  return ''

def imprimir():
  for arquivo in arquivos:
    
    print(arquivo)
    print(aymore(arquivo))

imprimir()