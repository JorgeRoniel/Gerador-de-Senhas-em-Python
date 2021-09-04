import random
from PySimpleGUI import PySimpleGUI as sg 
import os 

class gerador_sen:
    def __init__(self):
        sg.theme('Reddit')

        layout = [
            [sg.Text('Site/Software: ', size=(10, 1)), sg.Input(size=(20,1), key='site')],
            [sg.Text('Email/Usuário: ', size=(10, 1)), sg.Input(size=(20, 1), key='email')],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32,5))],
            [sg.Button('Gerar Senha!')]
        ]

        self.janela = sg.Window('Gerador de Senhas', layout)

    def Iniciar(self):
        while True:
            eventos, valores = self.janela.read()
            if eventos == sg.WINDOW_CLOSED:
                break
            if eventos == 'Gerar Senha!':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        char_list = 'ABDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"Site: {valores['site']}, Usuário: {valores['email']}, Nova Senha: {nova_senha}")

        print('Arquivo Salvo!')

ger = gerador_sen()
ger.Iniciar()