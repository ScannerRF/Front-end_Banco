#importando as bibliotecas
import customtkinter as ctk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

#======================criando a janela======================
telaDir_VisualizarAluno = ctk.CTk(fg_color='#f1f1f1')

#======================configurando a janela principal======================
telaDir_VisualizarAluno.title('Diretor - Visualizar Turma')
telaDir_VisualizarAluno.geometry('1260x960')
telaDir_VisualizarAluno.resizable(False, False)
telaDir_VisualizarAluno._set_appearance_mode('dark')

#======================funcao======================
#funcao para iniciar a janela centralizada
def centralizarTela(telaDir_VisualizarAluno):
    telaDir_VisualizarAluno.update_idletasks()
    width = telaDir_VisualizarAluno.winfo_width()
    height = telaDir_VisualizarAluno.winfo_height()
    screen_width = telaDir_VisualizarAluno.winfo_screenwidth()
    screen_height = telaDir_VisualizarAluno.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    telaDir_VisualizarAluno.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#funcao para centralizar a janela
centralizarTela(telaDir_VisualizarAluno)

#======================configurando imagens======================
imgLogoMenu = ctk.CTkImage(light_image=Image.open('imagens/imgLogo.png'), dark_image=Image.open(
    'imagens/imgLogo.png'), size=(110, 105))

imgBtnAlunos = ctk.CTkImage(light_image=Image.open('imagens/imgBtnAluno.png'), dark_image=Image.open(
    'imagens/imgBtnAluno.png'), size=(36, 36))

imgBtnEntradas = ctk.CTkImage(light_image=Image.open('imagens/imgBtnEntrada.png'), dark_image=Image.open(
    'imagens/imgBtnEntrada.png'), size=(36, 36))

imgLogoRodape = ctk.CTkImage(light_image=Image.open('imagens/imgNomeLogo.png'), dark_image=Image.open(
    'imagens/imgNomeLogo.png'), size=(300, 92))

imgPlanoDFundo = ctk.CTkImage(light_image=Image.open('imagens/imgFundo.jpg'), dark_image=Image.open(
    'imagens/imgFundo.jpg'), size=(1260, 960))

imgMainAlunos = ctk.CTkImage(light_image=Image.open('imagens/imgAlunoVerde.png'), dark_image=Image.open(
    'imagens/imgAlunoVerde.png'), size=(200, 240))

imgBtnCadastrar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnCadastrar.png'), dark_image=Image.open(
    'imagens/imgBtnCadastrar.png'), size=(36, 36))

imgBtnDesconectar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnDesconectar.png'), dark_image=Image.open(
    'imagens/imgBtnDesconectar.png'), size=(36, 36))

imgBtnHome = ctk.CTkImage(light_image=Image.open('imagens/imgBtnHome.png'), dark_image=Image.open(
    'imagens/imgBtnHome.png'), size=(36, 36))

imgBtnVoltar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnVoltar.png'), dark_image=Image.open(
    'imagens/imgBtnVoltar.png'), size=(36, 36))

imgBtnAtualizar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnAtualizar.png'), dark_image=Image.open(
    'imagens/imgBtnAtualizar.png'), size=(36, 36))

#label com imagem do plano de fundo, primeiro item a executar para ser a ultima camada
lblPlanoDFundo = ctk.CTkLabel(telaDir_VisualizarAluno, image=imgPlanoDFundo, text='')
lblPlanoDFundo.place(x=0, y=0 )

#======================configurando frames======================
#======================configurando frame de fundo do menu======================
frmFundoMenu = ctk.CTkFrame(telaDir_VisualizarAluno, width=1260, height=120, corner_radius=0,
    fg_color='white')
frmFundoMenu.place(x=0, y=0)

#======================configurando widgets do frame de fundo do menu======================
#botão alunos
btnAluno = ctk.CTkButton(frmFundoMenu, text='Alunos', width=300, height=70,corner_radius=0,
    fg_color='#069E6E', font=("arial", 30), hover_color='#047b55', image=imgBtnAlunos, text_color='white')
btnAluno.place(x=150, y=25)

#label com imagem da logo no menu
lblImgLogoMenu = ctk.CTkLabel(frmFundoMenu, image=imgLogoMenu, text='')
lblImgLogoMenu.place(x=625, y=10)

#botão entradas
btnEntrada = ctk.CTkButton(frmFundoMenu, text='Entradas', width=300, height=70,corner_radius=0,
    fg_color='#069E6E', font=("arial", 30), hover_color='#047b55', image=imgBtnEntradas, text_color='white')
btnEntrada.place(x=910, y=25)



#======================main do sistema, parte do centro do sistema======================
#======================configurando frame de fundo do main======================
frmFundoMain = ctk.CTkFrame(telaDir_VisualizarAluno, width=1060, height=740, corner_radius=0,
    fg_color='white')
frmFundoMain.place(x=150, y=170)

#======================configurando widgets do frame fundo do main======================
#label titulo da pagina
lblTituloCadastro = ctk.CTkLabel(frmFundoMain, text='ALUNO', fg_color='white', font=("arial", 50),
    text_color='#1C1C1C')
lblTituloCadastro.place(x=440, y=100)

#label turma pesquisada
lblNomeAluno = ctk.CTkLabel(frmFundoMain, text='Nome:', fg_color='white', font=("arial", 20),
    text_color='#1C1C1C')
lblNomeAluno.place(x=100, y=180)

#label curso pesquisado
lblRmAluno = ctk.CTkLabel(frmFundoMain, text='RM:', fg_color='white', font=("arial", 20),
    text_color='#1C1C1C')
lblRmAluno.place(x=100, y=220)

#label periodo pesquisado
lblPeriodoAluno= ctk.CTkLabel(frmFundoMain, text='Período:', fg_color='white', font=("arial", 20),
    text_color='#1C1C1C')
lblPeriodoAluno.place(x=100, y=250)

#label serie pesquisada
lblCursoAluno = ctk.CTkLabel(frmFundoMain, text='Curso:', fg_color='white', font=("arial", 20),
    text_color='#1C1C1C')
lblCursoAluno.place(x=100, y=280)

#label quantidade de alunos na turma
lblSerieAluno = ctk.CTkLabel(frmFundoMain, text='Série:', fg_color='white', font=("arial", 20),
    text_color='#1C1C1C')
lblSerieAluno.place(x=100, y=310)

#label com a imagem do aluno
lblImgAluno = ctk.CTkLabel(frmFundoMain, text='Foto do Aluno', bg_color='#f1f1f1', width=200, 
    height=240, text_color='#1C1C1C')
lblImgAluno.place(x=430, y=330)
print(860/2)

#botão atualizar aluno, vai p/ a pag atualizar
btnAtualizarAluno = ctk.CTkButton(frmFundoMain, text='Atualizar aluno', width=298, height=50,corner_radius=50,
    fg_color='#069E6E', font=("arial", 20), hover_color='#047b55', image=imgBtnAtualizar,
    text_color='white')
btnAtualizarAluno.place(x=381, y=590)

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
frmFundoMenuLateral = tk.Frame(telaDir_VisualizarAluno, width=100, bg="#069E6E")
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
    telaDir_VisualizarAluno.destroy()

#botão desconectar separado na parte inferior do menu
btnDesconectarMenuLateral = ctk.CTkButton(frmFundoMenuLateral, text="", corner_radius=0, fg_color="#069E6E", 
    hover_color='#047b55', image=imgBtnDesconectar, command=desconectar)
btnDesconectarMenuLateral.configure(width=100, height=70)
btnDesconectarMenuLateral.place(x=0, y=862)

#rodando a janela
telaDir_VisualizarAluno.mainloop()

