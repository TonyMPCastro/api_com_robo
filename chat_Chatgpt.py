import openai
import PySimpleGUI as sg
import pyperclip

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
    temperature=0.5
    )
    res = response['choices'][0]['text']
    return res

def chat():
    sg.theme("Dark Blue")

    layout = [
              [sg.Text('Resposta do Chat GPT:', text_color='red', background_color='white')],
              [sg.Output(size=(100,20), key='Output', text_color='white')],
              [sg.Button('Copiar'), sg.Button('Limpar'), sg.Button('Salvar conversa em .txt')],
              [sg.Text('Digite sua mensagem:',key='input')],
              [sg.Input(key='prompt', text_color='white'), sg.Button('Enviar')],
             ]

    return sg.Window('Chat', layout, finalize=True, resizable=True)
    
window = chat()

while True:

    event, values = window.read()

    if event == sg.WINDOW_CLOSED:

        break

    elif event == 'Enviar':

        # Chame a API e armazene a resposta em uma variável
        prompt = values['prompt']

        print(f'\nUser: {prompt}\n')

        window['input'].update('')

        res = pergunta(prompt)

        print(f'GPT-3: {res}')

    elif event == 'Limpar':

        window.close()
        window = chat()

    elif event == 'Copiar':

        output_value = window.Element('Output').get()
        # copy the output value to clipboard
        pyperclip.copy(output_value)

    elif event == 'Salvar conversa em .txt':

        # get the output value
        output_value = window.Element('Output').get()
        # Open a file save dialog
        file_path = sg.PopupGetFile('Salvar arquivo', save_as=True, file_types=(("Text files", "*.txt"),))
        # write the output value to the selected file
        with open(file_path, "w") as file:
            file.write(output_value)
            sg.popup("Arquivo salvo com sucesso!")