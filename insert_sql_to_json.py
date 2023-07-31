import json
import pymysql
from os import listdir
from os.path import isfile, join, getsize
from datetime import datetime


def insert_evolucao_prontuario(file,cursor,conexao):
    
    print("\n\nCarregando....\n\n")

    with open(file, 'r', encoding="utf-8") as file2:
        data = json.load(file2)
    count = 0   
    for item in data:
        # Extrair os dados do item
        cod = item["Prontuario"]
        data_p = datetime.strptime(item["Data"], '%Y-%m-%d')
        hist = item["Historico"]
        num = int(item["Numero"])
        tipo = int(item["Tipo"])
        cab = item["Cabecalho"]
        rod = item["Rodape"]
        tim = item["Timbrado"]
        
        # Obtendo a data e hora atual
        agora = datetime.now()
        # Obtendo a data e hora formatadas
        data_hora_formatada = agora.strftime('%Y-%m-%d %H:%M:%S')
        
        dt = data_hora_formatada
        # ... (continuar para cada campo)
        # Executar a consulta de inserção
        query = "INSERT INTO evolucao_prontuario (prontuario, data_prontuario, historico, numero, tipo, cabecalho, rodape, timbrado, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (cod, data_p,hist,num,tipo,cab,rod,tim,dt)
        cursor.execute(query, valores)
        count = count + 1
        if count == 500:
            conexao.commit()
            count = 0
        

    print("\n\nFianlizado !")
    
    
    
    

conexao = pymysql.connect(
    host='143.198.174.64',
    user='dev',
    password='123456',
    db='medzin2'
)

cursor = conexao.cursor()

file = "evolucao.json"

insert_evolucao_prontuario(file,cursor,conexao)

conexao.commit()
conexao.close()
