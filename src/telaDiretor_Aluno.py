#importando as bibliotecas
import customtkinter as ctk
from tkinter import *
import tkinter as tk
from PIL import Image

#======================criando a janela======================
telaDir_Aluno = ctk.CTk(fg_color='#f1f1f1')

#======================configurando a janela principal======================
telaDir_Aluno.title('Diretor - Aluno')
telaDir_Aluno.geometry('1260x960')
telaDir_Aluno.resizable(False, False)
telaDir_Aluno._set_appearance_mode('dark')

#======================funcao======================
#funcao para iniciar a janela centralizada
def centralizarTela(telaDir_Aluno):
    telaDir_Aluno.update_idletasks()
    width = telaDir_Aluno.winfo_width()
    height = telaDir_Aluno.winfo_height()
    screen_width = telaDir_Aluno.winfo_screenwidth()
    screen_height = telaDir_Aluno.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    telaDir_Aluno.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#funcao para centralizar a janela
centralizarTela(telaDir_Aluno)

#======================configurando imagens======================
imgLogoMenu = ctk.CTkImage(light_image=Image.open('imagens/imgLogo.png'), dark_image=Image.open(
    'imagens/imgLogo.png'), size=(110, 105))

imgBtnAlunos = ctk.CTkImage(light_image=Image.open('imagens/imgBtnAluno.png'), dark_image=Image.open(
    'imagens/imgBtnAluno.png'), size=(36, 36))

imgMainAlunos = ctk.CTkImage(light_image=Image.open('imagens/imgAlunoVerde.png'), dark_image=Image.open(
    'imagens/imgAlunoVerde.png'), size=(260, 260))

imgBtnEntradas = ctk.CTkImage(light_image=Image.open('imagens/imgBtnEntrada.png'), dark_image=Image.open(
    'imagens/imgBtnEntrada.png'), size=(36, 36))

imgBtnCadastrar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnCadastrar.png'), dark_image=Image.open(
    'imagens/imgBtnCadastrar.png'), size=(46, 46))

imgBtnVisualizar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnVisualizar.png'), dark_image=Image.open(
    'imagens/imgBtnVisualizar.png'), size=(36, 36))

imgPlanoDFundo = ctk.CTkImage(light_image=Image.open('imagens/imgFundo.jpg'), dark_image=Image.open(
    'imagens/imgFundo.jpg'), size=(1260, 960))

imgBtnDesconectar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnDesconectar.png'), dark_image=Image.open(
    'imagens/imgBtnDesconectar.png'), size=(36, 36))

imgBtnHome = ctk.CTkImage(light_image=Image.open('imagens/imgBtnHome.png'), dark_image=Image.open(
    'imagens/imgBtnHome.png'), size=(36, 36))

imgBtnVoltar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnVoltar.png'), dark_image=Image.open(
    'imagens/imgBtnVoltar.png'), size=(36, 36))

    
#label com imagem do plano de fundo, primeiro item a executar para ser a ultima camada
lblPlanoDFundo = ctk.CTkLabel(telaDir_Aluno, image=imgPlanoDFundo, text='')
lblPlanoDFundo.place(x=0, y=0 )

#======================configurando frames======================
#======================configurando frame de fundo do menu======================
frmFundoMenu = ctk.CTkFrame(telaDir_Aluno, width=1260, height=120, corner_radius=0,
    fg_color='white')
frmFundoMenu.place(x=0, y=0)

#======================configurando widgets do frame de fundo do menu======================
#botão alunos
btnAluno = ctk.CTkButton(frmFundoMenu, text='Alunos', width=300, height=70,corner_radius=0,
    fg_color='#069E6E', font=("arial", 30), hover_color='#047b55', image=imgBtnAlunos, text_color='white')
btnAluno.place(x=200, y=25)

#label com imagem da logo no menu
lblImgLogoMenu = ctk.CTkLabel(frmFundoMenu, image=imgLogoMenu, text='')
lblImgLogoMenu.place(x=625, y=10)

#botão entradas
btnEntrada = ctk.CTkButton(frmFundoMenu, text='Entradas', width=300, height=70,corner_radius=0,
    fg_color='#069E6E', font=("arial", 30), hover_color='#047b55', image=imgBtnEntradas, text_color='white')
btnEntrada.place(x=860, y=25)



#======================main do sistema, parte do centro do sistema======================
#======================configurando frame de fundo do main======================
frmFundoMain = ctk.CTkFrame(telaDir_Aluno, width=960, height=500, corner_radius=0,
    fg_color='white')
frmFundoMain.place(x=200, y=290)

#======================configurando widgets do frame fundo do main======================
#label com a imagem(icone) do aluno
lblImgAluno = ctk.CTkLabel(frmFundoMain, image=imgMainAlunos, text='', bg_color='white')
lblImgAluno.place(x=350, y=120)

#label rotulo explicativo da pagina
lblRotuloImgAluno = ctk.CTkLabel(frmFundoMain, text='ALUNOS', fg_color='#069E6E', font=("arial", 30),
    text_color='white', corner_radius=10, bg_color='white', width=150, height=40)
lblRotuloImgAluno.place(x=395, y=350)

#botão cadastrar aluno
btnCadastrarAluno = ctk.CTkButton(frmFundoMain, text='Cadastrar\n Aluno', width=298, height=70, corner_radius=50,
    fg_color='#069E6E', font=("arial", 25), hover_color='#047b55', image=imgBtnCadastrar, text_color='white')
btnCadastrarAluno.place(x=30, y=215)

#botão visualizar aluno
btnVisualizarAluno = ctk.CTkButton(frmFundoMain, text='Visualizar\n Aluno', width=298, height=70, corner_radius=50,
    fg_color='#069E6E', font=("arial", 25), hover_color='#047b55', image=imgBtnVisualizar, text_color='white')
btnVisualizarAluno.place(x=632, y=215)


#======================funcoes======================
#funcao que ira definir como o menu ira exibir de forma expandida, quando o mouse passar por cima
def expandir_menu(event):
    # Largura expandida do menu
    frmFundoMenuLateral.configure(width=350)  
    for btnMenuLateral in botoes:
        btnMenuLateral.configure(width=350, height=69, anchor=tk.CENTER)
        btnMenuLateral.configure(text=btnMenuLateral.nome)  # Exibir o texto do botão
        btnVoltarMenuLateral.configure(text='Voltar', width=350, height=70, anchor=tk.CENTER)
        btnDesconectarMenuLateral.configure(text='Desconectar', width=350, height=70, anchor=tk.CENTER)
    frmFundoMenuLateral.bind("<Leave>", contrair_menu)

#funcao que ira definir como o menu ira exibir de forma contraida, quando o mouse sair de cima
def contrair_menu(event):
    # Largura contraída do menu
    frmFundoMenuLateral.configure(width=100)  
    for btnMenuLateral in botoes:
        btnMenuLateral.configure(width=100, height=70, anchor=tk.CENTER)
        btnMenuLateral.configure(text="")  # Ocultar o texto do botão
        btnVoltarMenuLateral.configure(text='',width=100, height=70, anchor=tk.CENTER)
        btnDesconectarMenuLateral.configure(text='',width=100, height=70, anchor=tk.CENTER)



#======================configurando frame de fundo do menu lateral======================
frmFundoMenuLateral = tk.Frame(telaDir_Aluno, width=100, bg="#069E6E")
frmFundoMenuLateral.place(x=0, y=0, relheight=1)

#======================configurando widgets do frame de fundo do menu lateral======================
# Lista de dados dos botões, 
botoes_menu = [
    #texto do btn         |       icone do btn          | comando do btn
    {"nome": "Início", "icone": "imagens/imgBtnHome.png", "comando": ''},
    {"nome": "Alunos", "icone": "imagens/imgBtnAluno.png", "comando":'' },
    {"nome": "Entradas", "icone": "imagens/imgBtnEntrada.png", "comando": ''}
]

botoes = []

y_offset = 0  # Deslocamento vertical inicial

for data in botoes_menu:
    btnMenuLateral = tk.Button(frmFundoMenuLateral, compound=tk.LEFT, command=data["comando"])
    btnMenuLateral.configure(width=100, height=70, bg='#069E6E',fg='white' ,font=('arial', 20) ,anchor=tk.CENTER)
    btnMenuLateral.configure(text="")  # Exibir o texto do botão
    btnMenuLateral.place(x=0, y=y_offset)

    # Configure o ícone do botão
    icon = tk.PhotoImage(file=data["icone"])
    btnMenuLateral.config(image=icon)
    btnMenuLateral.image = icon

    btnMenuLateral.nome = data["nome"]  # Salvar o nome do botão

    # Configure os eventos de passagem do mouse
    btnMenuLateral.bind("<Enter>", expandir_menu)

    botoes.append(btnMenuLateral)

    y_offset += 77  # Incrementar o deslocamento vertical para o próximo botão


#botão voltar separado na parte inferior do menu
btnVoltarMenuLateral = ctk.CTkButton(frmFundoMenuLateral, text="", corner_radius=0, fg_color="#069E6E", hover_color='#047b55',
    image=imgBtnVoltar)
btnVoltarMenuLateral.configure(width=100, height=70)
btnVoltarMenuLateral.place(x=0, y=790)


#======================funcoes======================
#funcao do botao desconectar
def desconectar():
    telaDir_Aluno.destroy()

#botão desconectar separado na parte inferior do menu
btnDesconectarMenuLateral = ctk.CTkButton(frmFundoMenuLateral, text="", corner_radius=0, fg_color="#069E6E", 
    hover_color='#047b55', image=imgBtnDesconectar, command=desconectar)
btnDesconectarMenuLateral.configure(width=100, height=70)
btnDesconectarMenuLateral.place(x=0, y=862)

#rodando a janela
telaDir_Aluno.mainloop()

