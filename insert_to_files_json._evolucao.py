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

def check_codigo_exists(codigo,cursor):

    # Executar a consulta SELECT
    query = "SELECT codigo FROM evolucao WHERE codigo = %s"

    cursor.execute(query, (codigo))

    # Verificar se o código já existe
    exists = cursor.fetchone() is not None

    return exists

def insert(files,cursor,conexao,limit = 1000000):
    
    print("\n\nCarregando....\n\n")

    count = 0
    
    for file in files:

        print("\n\nFile: "+file)
        if count == limit:
            break
        
        with open("dados_evolucao/"+file, 'r', encoding="utf-8") as file2:
            data = json.load(file2)
            
        print("\n\nTotal Registros: ",len(data))

        count_reg_i = 0
        count_reg_u = 0

        for item in data:
            # Extrair os dados do item
            id = item["id"]
            conteudo = item["conteudo"]
            if not check_codigo_exists(id , cursor):
                # ... (continuar para cada campo)
                # Executar a consulta de inserção
                query = "INSERT INTO evolucao (codigo, conteudo) VALUES (%s, %s)"
                valores = (id, conteudo)
                cursor.execute(query, valores)
                count_reg_i = count_reg_i + 1

            else:
                query = "UPDATE evolucao SET conteudo = %s WHERE codigo = %s"
                valores = (conteudo , id)
                cursor.execute(query, valores)
                count_reg_u = count_reg_u + 1
            
        count = count + 1
        
        print("\n\nTotal Registros Inseridos: ",count_reg_i)

        print("\n\nTotal Registros Update: ",count_reg_u)

        caminho_destino = "C:/xampp/htdocs/api_com_robo/Evolucao/" +file
        shutil.move("C:/xampp/htdocs/api_com_robo/dados_evolucao/"+file, caminho_destino)
        conexao.commit()

    print("\n\nFianlizado !")

conexao = pymysql.connect(
    host='desenv.medzin.com.br',
    user='developer',
    password= 'i&R&u$P@FS4x',
    db='medzin2'
)

cursor = conexao.cursor()

path = "C:/xampp/htdocs/api_com_robo/dados_evolucao"

files = get_files(path)

insert(files,cursor,conexao)

conexao.commit()
conexao.close()
