from os import listdir
from os.path import isfile, join, getsize
import json
import win32com.client
import time
from datetime import datetime


def ler_arquivo(path,file):
    a = "C:/xampp/htdocs/api_com_robo/"+path+"/"+file
    word = win32com.client.Dispatch("Word.Application")
    wb = word.Documents.Open(a)
    doc = word.ActiveDocument
    # Pega o texto do arquivo
    result = doc.Range().Text
    # quit Word
    doc.Close(False)
    word.Quit()

    return result


def gerar_json(path,files):
    array = []
    count = 0
    print("Carregando....")
    for file in files:
       
        conteudo = ler_arquivo(path,file)
        #print(count)
        conteudo = str(conteudo)
        if conteudo != "\r":
            conteudo = conteudo.replace('\n', '<br>')
            conteudo = conteudo.replace('\t', '&emsp;')
            conteudo = conteudo.replace('\r', '<br>')
            conteudo = conteudo.replace('"', "'")
            file = file.replace('.DOC', '')

            text_html = "<main style='width: 100%; height: 100%;'><div style='padding:50px;'><p>"+conteudo+"</p></div></main>" 
            
            array.append({
                "id": file,
                "conteudo": text_html
            })
            count = count + 1
        
    with open(path+"_html.json", "w", encoding="utf-8") as arquivo:     
        json.dump(array, arquivo, indent=4,ensure_ascii=False)
    print(count," QTD")
    print("Fianlizado !")



def get_files(path):
    files = []
    for file in listdir(path):
        if (isfile(join(path, file))) and (getsize(join(path, file)) > 0):
            files.append(file)
    print(files)
    return files



inicio = time.time()
data_e_hora_atuais = datetime.now()

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_em_texto)

path = 'Padroes'

files = get_files(path)

gerar_json(path,files)

fim = time.time()
duration = fim - inicio
duration_in_minutes_and_seconds = str(duration).split('.')[0][2:]

print("Tempo: ",duration_in_minutes_and_seconds) 

data_e_hora_atuais= datetime.now()

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_em_texto)

