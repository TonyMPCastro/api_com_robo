import openai
import codecs



# Adicione sua chave de API aqui
openai.api_key = "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"

# Defina o modelo a ser usado
model_engine = "text-davinci-003"


def pergunta(prompt):
    prompt = prompt
    response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5)
    res = response['choices'][0]['text']
    return res

def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        texto = f.read()
    return texto

def salvar_em_txt(texto, nome_arquivo):
    with codecs.open(nome_arquivo, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(texto)


def analiza_arquivo(solicitacao,caminho_arquivo):
    texto_do_arquivo = ler_arquivo(caminho_arquivo)
    prompt = texto_do_arquivo + "\n" + solicitacao
    res = pergunta(prompt)
    texto = "Pergunta: "+solicitacao+"\nCaminho File:" +caminho_arquivo+"\nResposta:" + res
    nome_arquivo = "Resposta.txt"
    salvar_em_txt(texto, nome_arquivo)

def cria_arquivo(solicitacao,new_file = "file_teste.php"):
    prompt = solicitacao
    res = pergunta(prompt)
    texto = "Pergunta: "+solicitacao+"\nCaminho File:" +new_file+"\nResposta:" + res
    nome_arquivo = new_file
    salvar_em_txt(texto, nome_arquivo)   



solicitacao = "Refatore o Codigo acima para um mais rapido e eficiente e com php 8:"
path_file = "index.php"
#analiza_arquivo(solicitacao,path_file)


solicitacao = "Fazer uma class apiChatGpt com php 8, para realizar uma requisição para Api do ChatGpt fazer calculos das 4 operacoes"

path_file = "apiChatGpt.php"
cria_arquivo(solicitacao,path_file)