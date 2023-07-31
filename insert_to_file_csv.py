import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Abrir o arquivo CSV para leitura

    with open(csv_file_path, 'r', encoding="utf-8") as csv_file:
        # Ler o conteúdo do arquivo CSV
        csv_data =  csv.DictReader(csv_file, delimiter=';')
        # Converter o conteúdo do CSV em uma lista de dicionários
        data_list = list(csv_data)
     
        
    # Obter a quantidade de linhas do array
    quantidade_linhas = len(data_list)

    # Mostrar a quantidade de linhas
    print("QTDE: ",quantidade_linhas)

    # Escrever os dados convertidos em um arquivo JSON
    with open(json_file_path, 'w', encoding="utf-8") as json_file:
        json.dump(data_list, json_file, indent=4,ensure_ascii=False)

# Caminho do arquivo CSV de entrada
csv_file_path = 'paciente.csv'

# Caminho do arquivo JSON de saída
json_file_path = 'Pacientes2.json'

# Chamar a função de conversão
csv_to_json(csv_file_path, json_file_path)

