'''import tkinter as tk
import customtkinter as ctk
from PIL import Image
def expandir_menu(event):
    sidebar.configure(width=350)  # Largura expandida do menu
    for button in botoes:
        button.configure(width=350, height=70, anchor=tk.CENTER)
        button.configure(text=button.nome)  # Exibir o texto do botão
        botao_separado1.configure(text='Voltar', width=350, height=5, anchor=tk.CENTER)
        botao_separado.configure(text='Desconectar', width=350, height=5, anchor=tk.CENTER)
    sidebar.bind("<Leave>", contrair_menu)

def contrair_menu(event):
    sidebar.configure(width=100)  # Largura contraída do menu
    for button in botoes:
        button.configure(width=100, height=70, anchor=tk.CENTER)
        button.configure(text="")  # Ocultar o texto do botão
        botao_separado1.configure(text='',width=100, height=50, anchor=tk.CENTER)
        botao_separado.configure(text='',width=100, height=50, anchor=tk.CENTER)

def fechar_janela():
    root.destroy()

def abrir_janela():
    nova_janela = tk.Toplevel(root)
    nova_janela.geometry("200x200")
    nova_janela.title("Nova Janela")
    label = tk.Label(nova_janela, text="Janela aberta!")
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root = ctk.CTk()
root.geometry("1200x960")

sidebar = tk.Frame(root, width=100, bg="#069E6E")
sidebar.place(x=0, y=0, relheight=1)

# Lista de dados dos botões
button_data = [
    {"nome": "Início", "icone": "imagens/imgBtnHome.png", "comando": fechar_janela},
    {"nome": "Alunos", "icone": "imagens/imgBtnAluno.png", "comando": abrir_janela},
    {"nome": "Entradas", "icone": "imagens/imgBtnEntrada.png", "comando": abrir_janela},
    # Adicione mais botões e ícones conforme necessário
]

botoes = []

y_offset = 0  # Deslocamento vertical inicial
#font=('arial', 30),
 #   width=350, height=70, corner_radius=0, fg_color='#069E6E', hover_color='#047b55'
for data in button_data:
    button = tk.Button(sidebar, compound=tk.LEFT, command=data["comando"])
    button.configure(width=100, height=70, bg='#069E6E',fg='white' ,font=('arial', 20) ,anchor=tk.CENTER)
    button.configure(text="")  # Exibir o texto do botão
    button.place(x=0, y=y_offset)

    # Configure o ícone do botão
    icon = tk.PhotoImage(file=data["icone"])
    button.config(image=icon)
    button.image = icon

    button.nome = data["nome"]  # Salvar o nome do botão

    # Configure os eventos de passagem do mouse
    button.bind("<Enter>", expandir_menu)

    botoes.append(button)

    y_offset += 77  # Incrementar o deslocamento vertical para o próximo botão

imgBtnVoltar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnVoltar.png'), dark_image=Image.open(
    'imagens/imgBtnVoltar.png'), size=(36, 36))
imgBtnDesconectar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnDesconectar.png'), dark_image=Image.open(
    'imagens/imgBtnDesconectar.png'), size=(36, 36))

# Botão separado na parte inferior do menu
botao_separado1 = ctk.CTkButton(sidebar, text="", corner_radius=0, fg_color="#069E6E", hover_color='#047b55', image=imgBtnVoltar)
botao_separado1.configure(width=100, height=50)
botao_separado1.place(x=0, y=860)

# Botão separado na parte inferior do menu
botao_separado = ctk.CTkButton(sidebar, text="", corner_radius=0, fg_color="#069E6E", hover_color='#047b55', image=imgBtnDesconectar)
botao_separado.configure(width=100, height=50)
botao_separado.place(x=0, y=912)

root.mainloop()

'''











from tkinter import Tk, Button, Label, PhotoImage
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

def carregar_imagem():
    # Abrir caixa de diálogo para selecionar a imagem
    filename = askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    
    # Verificar se um arquivo foi selecionado
    if filename:
        # Abrir a imagem usando a biblioteca PIL
        imagem = Image.open(filename)
        
        # Redimensionar a imagem para exibi-la na janela
        imagem = imagem.resize((200, 240), Image.LANCZOS)
        
        # Criar um objeto ImageTk para exibir a imagem no tkinter
        imagem_tk = ImageTk.PhotoImage(imagem)
        
        # Exibir a imagem na Label
        label_imagem.configure(image=imagem_tk)
        label_imagem.image = imagem_tk  # Manter uma referência à imagem

# Criar a janela principal
janela = Tk()

# Criar uma Label para exibir a imagem
label_imagem = Label(janela)
label_imagem.pack()

# Criar um botão para carregar a imagem
botao_carregar = Button(janela, text="Carregar Imagem", command=carregar_imagem)
botao_carregar.pack()

# Iniciar o loop do tkinter
janela.mainloop()


'''
#======================configurando frame de fundo do rodape======================
frmFundoRodape = ctk.CTkFrame(telaDir_Home, width=1260, height=120, corner_radius=0,
    fg_color='white')
frmFundoRodape.place(x=0, y=840)

#======================configurando widgets do frame de fundo do rodape======================
#label com imagem da logo no rodape
lblImgLogoRodape = ctk.CTkLabel(frmFundoRodape, image=imgLogoRodape, text='')
lblImgLogoRodape.place(x=10, y=-10)

#label rodape
lblRodape = ctk.CTkLabel(frmFundoRodape, text='Todos os direitos reservados - 2023 - ScannerRF', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 12))
lblRodape.place(x=200-285, y=28)

#label para representar listra divisoria no rodape
lblListraRodape = ctk.CTkLabel(frmFundoRodape, text='', fg_color='#1C1C1C', font=('arial bold', 2), width=200-20, height=1)
lblListraRodape.place(x=10, y=68)

#label rodape copyright
lblRodapeCopyright = ctk.CTkLabel(frmFundoRodape, text='© 2023 Copyright - ScannerRF',fg_color='white', text_color='#1C1C1C', font=('arial bold', 12))
lblRodapeCopyright.place(x=540, y=73)

'''