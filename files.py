from os import listdir
from os.path import isfile, join, getsize
import json
import win32com.client as win32
from win32com.client import constants
import time
from datetime import datetime
import shutil


def get_files(path):
    files = []
    for file in listdir(path):
        if (isfile(join(path, file))) and (getsize(join(path, file)) > 0):
            files.append(file)
   # print(files)
    print("QTDE: " ,len(files))
    return files


def gerar_json(files):
    
    array = []

    print("\n\nCarregando....\n\n")
          
    for file in files:

        file2 = file.replace('.DOC', '')
        array.append(file2)

    with open("array_dados.json", "w", encoding="utf-8") as arquivo:     
        json.dump(array, arquivo, indent=4,ensure_ascii=False)

    print("\n\nFianlizado !")


path = "C:/Users/anton/Downloads/Evolucao2"

files = get_files(path)

gerar_json(files)