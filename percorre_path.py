from os import listdir
from os.path import isfile, join, getsize
import json
import win32com.client as win32
from win32com.client import constants
import time
from datetime import datetime
import shutil

def ler_arquivo(path,file,word):

    name_file = path+"/"+file

    # Variável para armazenar o texto marcado com a tag <b>
    marked_text = ""

    if isfile(name_file):

        wb = word.Documents.Open(name_file)

        doc = word.ActiveDocument

        # Pega o texto do arquivo
        content = doc.Content

        # Iterando sobre cada parágrafo e trecho de texto do documento
        if len(content.Paragraphs) != 0:
            for paragraph in content.Paragraphs:

                # Verificar o alinhamento do parágrafo
                if paragraph.Alignment == constants.wdAlignParagraphCenter:
                    marked_text += "<p style='text-align:center'>"
                elif paragraph.Alignment == constants.wdAlignParagraphLeft:
                    marked_text += "<p>"
                elif paragraph.Alignment == constants.wdAlignParagraphRight:
                    marked_text += "<p  style='text-align:right'>"
                elif paragraph.Alignment == constants.wdAlignParagraphJustify:
                    marked_text += "<p  style='text-align:justify'>"
                else:
                    marked_text += "<p>"
                    
                # Verificar se o parágrafo tem bullet ou numbered point
                if paragraph.Range.ListFormat.ListType == constants.wdListBullet:
                    marked_text += "&emsp;&bull;&nbsp;"
                elif paragraph.Range.ListFormat.ListType == constants.wdListSimpleNumbering:
                    num = paragraph.Range.ListFormat.ListString
                    marked_text += "&emsp;"+num+"&nbsp;.&nbsp;"

                marked_text_paragraphs = ""
                for rng in paragraph.Range.Words:
                    if rng.Bold == -1:
                        # Adiciona a tag <b> ao texto em negrito
                        marked_text_paragraphs += "<b>" + rng.Text + "</b>"
                    else:
                        marked_text_paragraphs += rng.Text
                
                # Adicionar o texto do parágrafo ao HTML
                marked_text += marked_text_paragraphs
                # Fechar a tag p
                marked_text += "</p>"

            if (marked_text == "<p  style='text-align:justify'> </p>") or (marked_text == "<p  style='text-align:left'> </p>") or (marked_text == "<p  style='text-align:center'> </p>") or (marked_text == "<p  style='text-align:right'> </p>") or (marked_text == "<p> </p>"):
                marked_text = False

        else:
            marked_text = False

        # quit Word
        doc.Close(False)

        

    else:
            marked_text = False


    return marked_text


def gerar_json(path,files,limit = 1000000):
    array = []
    count = 0
    count2 = 14

    path_output = "dados_textos/"

    print("\n\nCarregando....\n\n")
    
    word =  win32.gencache.EnsureDispatch('Word.Application')

    word.Visible = False

    word.DisplayAlerts = False        

    for file in files:

        if count == limit:
            break

        if count == 2000:#40000:

            str_name = path_output + str(count2) + "_dados_html.json"

            count2 = count2 + 1

            with open(str_name, "w", encoding="utf-8") as arquivo:     
                json.dump(array, arquivo, indent=4,ensure_ascii=False)

            count = 0
            array = []

        #print(count," - Lendo File: ",file)
        conteudo = ler_arquivo(path,file,word)

        if conteudo != False:
            conteudo = str(conteudo)
            if conteudo != "\r":
                conteudo = conteudo.replace('\n', '<br>')
                conteudo = conteudo.replace('\t', '&emsp;')
                conteudo = conteudo.replace('\r', ' ')
                conteudo = conteudo.replace('"', "'")
                file2 = file.replace('.DOC', '')

                text_html = "<div style='padding:50px;'>"+conteudo+"</div>" 
                
                array.append({
                    "id": file2,
                    "conteudo": text_html
                })
                count = count + 1
        # Mover o arquivo para o novo destino
        caminho_destino = "C:/xampp/htdocs/api_com_robo/b/"+str(count2)+"/" +file
        shutil.move(path+"/"+file, caminho_destino)
    
    word.Quit()

    str_name = path_output + str(count2) + "_dados_html.json"

    with open(str_name, "w", encoding="utf-8") as arquivo:     
        json.dump(array, arquivo, indent=4,ensure_ascii=False)

    print("\n\nFianlizado !")


def get_files(path):
    files = []
    for file in listdir(path):
        if (isfile(join(path, file))) and (getsize(join(path, file)) > 0):
            files.append(file)
   # print(files)
    print("QTDE: " ,len(files))
    return files



inicio = time.time()

data_e_hora_atuais = datetime.now()

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_em_texto+"\n\n")

#Caminho Completo da Pasta dos ARQUIVOS - WENNYS

#print("Exemplo(C:/documentos/Padroes)\nPath completo da pasta que tem os arquivos:")

#imput_path = input()

path = "C:/xampp/htdocs/api_com_robo/Textos"

files = get_files(path)

gerar_json(path,files)

fim = time.time()

duration = fim - inicio

duration_in_minutes_and_seconds = str(duration).split('.')[0][2:]

print("\nTempo: ",duration_in_minutes_and_seconds) 

data_e_hora_atuais= datetime.now()

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print("\n\n"+data_e_hora_em_texto+"\n\n")