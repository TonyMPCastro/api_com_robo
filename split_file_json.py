
import json

def separar_arquivos_json(json_data, quantidade_arquivos):
    # Dividir os dados do JSON em partes iguais
    tamanho_parte = len(json_data) // quantidade_arquivos

    for i in range(quantidade_arquivos):
        # Calcular os índices de início e fim para cada parte
        inicio = i * tamanho_parte
        fim = (i + 1) * tamanho_parte

        # Se for a última parte, incluir o restante dos dados
        if i == quantidade_arquivos - 1:
            parte = json_data[inicio:]
        else:
            parte = json_data[inicio:fim]

        # Salvar a parte em um arquivo JSON separado
        nome_arquivo = f"dados_padores_parte_{i+1}.json"
        with open(nome_arquivo,  'w',encoding="utf-8") as json_file:
            json.dump(parte, json_file, indent=4,ensure_ascii=False)
            
                
# Caminho do dados JSON
json_file_path = f"dados_impot_medzin/Padores/dados_padores_html.json"

# Abrir o dados JSON
with open(json_file_path, 'r', encoding="utf-8") as json_file:
    # Carregar o conteúdo do dados JSON
    dados_json = json.load(json_file)
    
# Quantidade de arquivos desejada
quantidade_arquivos_saida = 3

# Chamar a função para separar os arquivos JSON
separar_arquivos_json(dados_json, quantidade_arquivos_saida)

