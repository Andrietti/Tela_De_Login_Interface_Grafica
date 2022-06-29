from tkinter import font
from weakref import finalize
from xml.dom.minidom import Element
import PySimpleGUI as sg
import io, os
from PIL import Image
import requests

file_types = [('Imagens', '*.png *.jpg *.jpeg *.bmp'), ('Todos os arquivos', '*.*')]

lista_dia = []
lista_mes = ['jan.', 'fev.', 'mar.', 'abr.', 'maio', 'jun.' , 'jul.', 'ago.', 'set.', 'out.', 'nov.', 'dez.']
lista_ano = []
for i in range(1, 32):
    lista_dia.append(str(i))
for i in range(1940, 2023):
    lista_ano.append(str(i))

lista_usuarios = []
lista_senhas = []
nome = []
sg.theme('Reddit')

def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Push(), sg.Image(filename='entra.png'), sg.Push()],
        [sg.HSeparator(pad=((0,0),(0,0)))],
        [sg.Text('Email', font=("bold", 12))], 
        [sg.InputText(key='email', font=("bold", 15))],
        [sg.Text('Senha', font=("bold", 12))], 
        [sg.InputText(key='senha', password_char='*', font=("bold", 15))],
        [sg.Checkbox('Salvar Login?', key='lembrar', font=("bold", 15))],
        [sg.Button('Entrar', font=("bold", 15)), sg.Button('Cadastrar', font=("bold", 15))],
        [sg.Text('', size=(10, 1), key='mensagem')],
    ]

    return sg.Window('Iniciar sessão no entra21', layout=layout, finalize=True)

image = [
    [sg.Image(key="-IMAGE-")],
    ]

def janela_cadastro():
    sg.theme('Reddit')
    layout = [

        [sg.Push(), sg.Column(image), sg.Push()],
        [sg.FileBrowse('Procurar Img', file_types=file_types, key="-FILE-", size=(30, 1)),
            sg.Button("Load Image", size=(29, 1))],
        [sg.Text('Primeiro nome', font=("bold", 15))],
        [sg.Input(key='primeiro_nome', font=("bold", 15))],
        [sg.Text('Ultimo nome', font=("bold", 15))],
        [sg.Input(key='ultimo_nome', font=("bold", 15))],
        [sg.Text('Email', font=("bold", 15))],
        [sg.Input(key='email', font=("bold", 15))],
        [sg.Text('Exemplo: nome@exemplo.com', font=("bold", 15))],
        [sg.Text('Senha', font=("bold", 15))],
        [sg.Input(key='senha', font=("bold", 15))],
        [sg.Text('Confirmar senha', font=("bold", 15))],
        [sg.Input(key='confirmar', font=("bold", 15))],
        [sg.Button('Salvar', font=("bold", 15)), sg.Button('Voltar', font=("bold", 15))]
        
    ]

    return sg.Window('Cadastro', layout=layout, finalize=True)

end1 = [
    
    [sg.Text('CEP', font=("bold", 15)), sg.InputText(key='cep', size=(15, 1), font=("bold", 15)), sg.Button('Consultar', font=("bold", 15))],
    [sg.Text('Logradouro', font=("bold", 15)) ,sg.InputText(key='logradouro', size=(28, 1),font=("bold", 15)), sg.Text('Número', font=("bold", 15)), sg.InputText(key='numero', size=(8, 1), font=("bold", 15)), sg.Text('UF', font=("bold", 15)), sg.InputText(key='uf', size=(7, 1), font=("bold", 15))],
    [sg.Text('Bairro', font=("bold", 15)), sg.InputText(key='bairro', size=(23, 1), font=("bold", 15)), sg.Text('Cidade', font=("bold", 15)), sg.InputText(key='cidadee', size=(23, 1), font=("bold", 15))], 
    
    ]

def janela_3():
    sg.theme('Reddit')
    layout = [
        
        [sg.Push(),sg.Image(filename='aa.png'), sg.Push()],
        [sg.Push(), sg.Text('Seja Bem Vindo ao Entra21', font=("bold", 30), text_color='black'), sg.Push()],
        [sg.Push(), sg.Text('Diogo Jose Bento', font=("bold", 15), text_color='black'), sg.Push()],
        [sg.Text(key='nome')],

        [sg.Text('Data de Nasc.', font=("bold", 15)),
            sg.Combo(lista_dia, key='dia', font=("bold", 15), size=(5, 1)),
            sg.Text('/'),
            sg.Combo(lista_mes, key='mes', font=("bold", 15), size=(5, 1)),
            sg.Text('/'),
            sg.Combo(lista_ano, key='ano', font=("bold", 15), size=(5, 1)),
            sg.Text('Sexo', font=("bold", 15)),
            sg.Combo(('Masculino', 'Feminino'), key='sexo', size=(10, 1), font=("bold", 15))],

        [sg.Text('Telefone', font=("bold", 15)), sg.InputText(key='telefone', size=(21, 1), font=("bold", 15)),
            sg.Text('Celular', font=("bold", 15)), sg.InputText(key='celular', size=(22, 1), font=("bold", 15))],

        [sg.Column(end1, element_justification='center')],
        [sg.Button("Voltar", font=("bold", 15)), sg.Button("Salvar", font=("bold", 15))],
    ]

    return sg.Window("Seu perfil", layout=layout, finalize=True, element_justification='center')

janela1, janela2, janela3 = janela_login(), None, None

while True:
    window, event, values = sg.read_all_windows()
 
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    elif window == janela2 and event == sg.WIN_CLOSED:
        break
    elif window == janela3 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == 'Cadastrar':
        janela1.hide()
        janela2 = janela_cadastro()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1 = janela_login()

    if window == janela3 and event == "Voltar":
        janela3.hide()
        janela1 = janela_login()

    if event == "Load Image":
        filename = values["-FILE-"]
        if os.path.exists(filename):
            image = Image.open(values["-FILE-"])
            image.thumbnail((200, 200), Image.ANTIALIAS)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["-IMAGE-"].update(data=bio.getvalue())

    if window == janela2 and event == 'Salvar':
        if values["senha"] == values["confirmar"]:

            lista_usuarios.append(values['email'])
            lista_senhas.append(values['senha'])
            sg.popup("Cadastrado com sucesso", font=("bold", 15))
            janela2.hide()
            janela1 = janela_login()
        else:
            sg.popup("As senhas não coincidem", font=("bold", 15))

    if window == janela1 and event == 'Entrar':
        if values["email"] in lista_usuarios:
            try:
                if lista_usuarios.index(values["email"]) == lista_senhas.index(values["senha"]):
                    janela1.hide()
                    janela3 = janela_3()
                       
                elif lista_usuarios.index(values["email"]) != lista_senhas.index(values["senha"]):
                    sg.popup("Senha incorreta", font=("bold", 15))
                    
            except:
                pass
                
        else:
            sg.popup("Email não cadastrado", font=("bold", 15))

    if window == janela3 and event == 'Consultar':
        cep = values['cep']
        url = 'https://viacep.com.br/ws/%s/json/' % cep
        response = requests.get(url)
        response_json = response.json()
        janela3.Element('logradouro').Update(response_json['logradouro'])
        janela3.Element('bairro').Update(response_json['bairro'])
        janela3.Element('uf').Update(response_json['uf'])
        janela3.Element('cidadee').Update(response_json['localidade'])
