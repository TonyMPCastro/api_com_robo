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
        
        with open("dados_exames/"+file, 'r', encoding="utf-8") as file2:
            data = json.load(file2)

        for item in data:
    
            # Executar a consulta de inserção
            query = "INSERT INTO exames_legado(guia, nome_paciente, ano, paciente_id, requisicao, ordem, crm_realizante, nome_realizante, mnemonico, data_entrega, data_realizacao,  categoria_servico_id,created_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            valores = (item["guia"],item["nome_paciente"], item["ano"],item["paciente_id"], item["requisicao"],item["Ordem"],item["crm_realizante"],item["nome_realizante"],item["Mnemonico"],item["DataEntrega"],item["data_realizacao"],item["categria_servico_id"], '2023-05-25 17:28:00')
          
            cursor.execute(query, valores)
            
        count = count + 1
        caminho_destino = "C:/xampp/htdocs/api_com_robo/Exames/" +file
        shutil.move("C:/xampp/htdocs/api_com_robo/dados_exames/"+file, caminho_destino)
        conexao.commit()

    print("\n\nFianlizado !")

conexao = pymysql.connect(
 host='desenv.medzin.com.br',
    user='developer',
    password= 'i&R&u$P@FS4x',
    db='medzin2'
)

cursor = conexao.cursor()

path = "C:/xampp/htdocs/api_com_robo/dados_exames"

files = get_files(path)

insert(files,cursor,conexao)

conexao.commit()
conexao.close()
