import json
import pymysql
from os import listdir
from os.path import isfile, join, getsize
import shutil


def get_files(path):
    files = []
    for file in listdir(path):
        if (isfile(join(path, file))) and (getsize(join(path, file)) > 0):
            files.append(file)
    print(files)
    print("QTDE: " ,len(files))
    return files

def insert(files,cursor,conexao,limit = 1000000):
    
    print("\n\nCarregando....\n\n")

    count = 0
    
    for file in files:

        print("\n\nFile: "+file)

        if count == limit:
            break
        
        with open("dados_laudos/"+file, 'r', encoding="utf-8") as file2:
            data = json.load(file2)

        print("\n\nTotal Registros: ",len(data))
        
        count_reg = 0

        for item in data:
            # Extrair os dados do item
            id = item["id"]
            conteudo = item["conteudo"]
            
            # ... (continuar para cada campo)
            # Executar a consulta de inserção
            query = "INSERT INTO laudos_legado (codigo, conteudo) VALUES (%s, %s)"
            valores = (id, conteudo)
            cursor.execute(query, valores)
            count_reg = count_reg + 1

        print("\n\nTotal Registros inseridos: ",count_reg)
    
        count = count + 1
        caminho_destino = "C:/xampp/htdocs/api_com_robo/Laudos_/" +file
        shutil.move("C:/xampp/htdocs/api_com_robo/dados_laudos/"+file, caminho_destino)
        conexao.commit()

    print("\n\nFianlizado !")

conexao = pymysql.connect(
    host='desenv.medzin.com.br',
    user='developer',
    password= 'i&R&u$P@FS4x',
    db='medzin2'
)

cursor = conexao.cursor()

path = "C:/xampp/htdocs/api_com_robo/dados_laudos"

files = get_files(path)

insert(files,cursor,conexao)

conexao.commit()
conexao.close()
