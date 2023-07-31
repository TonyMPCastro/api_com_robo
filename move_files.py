import os
import shutil

# Especifique os caminhos das pastas origem e destino
pasta_origem = 'Laudos'
pasta_destino = 'a_laudos'

# Obtenha a lista de arquivos na pasta origem
arquivos = os.listdir(pasta_origem)

# Selecione os primeiros 200 arquivos (ou menos se houver menos de 200)
arquivos_selecionados = arquivos[:50000]

# Mova os arquivos para a pasta destino
for arquivo in arquivos_selecionados:
    caminho_origem = os.path.join(pasta_origem, arquivo)
    caminho_destino = os.path.join(pasta_destino, arquivo)
    shutil.move(caminho_origem, caminho_destino)
