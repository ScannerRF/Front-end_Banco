#importando as bibliotecas
import customtkinter as ctk
from tkinter import *
import tkinter as tk
from PIL import Image
from tkinter import messagebox

#======================criando a janela======================
telaDir_PesquisaVisualizar = ctk.CTk(fg_color='#f1f1f1')

#======================configurando a janela principal======================
telaDir_PesquisaVisualizar.title('Diretor - Pesquisar por Turma/RM')
telaDir_PesquisaVisualizar.geometry('1260x960')
telaDir_PesquisaVisualizar.resizable(False, False)
telaDir_PesquisaVisualizar._set_appearance_mode('dark')

#======================funcao======================
#funcao para iniciar a janela centralizada
def centralizarTela(telaDir_PesquisaVisualizar):
    telaDir_PesquisaVisualizar.update_idletasks()
    width = telaDir_PesquisaVisualizar.winfo_width()
    height = telaDir_PesquisaVisualizar.winfo_height()
    screen_width = telaDir_PesquisaVisualizar.winfo_screenwidth()
    screen_height = telaDir_PesquisaVisualizar.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    telaDir_PesquisaVisualizar.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#funcao para centralizar a janela
centralizarTela(telaDir_PesquisaVisualizar)

#======================configurando imagens======================
imgLogoMenu = ctk.CTkImage(light_image=Image.open('imagens/imgLogo.png'), dark_image=Image.open(
    'imagens/imgLogo.png'), size=(110, 105))

imgBtnAlunos = ctk.CTkImage(light_image=Image.open('imagens/imgBtnAluno.png'), dark_image=Image.open(
    'imagens/imgBtnAluno.png'), size=(36, 36))

imgBtnEntradas = ctk.CTkImage(light_image=Image.open('imagens/imgBtnEntrada.png'), dark_image=Image.open(
    'imagens/imgBtnEntrada.png'), size=(36, 36))

imgPlanoDFundo = ctk.CTkImage(light_image=Image.open('imagens/imgFundo.jpg'), dark_image=Image.open(
    'imagens/imgFundo.jpg'), size=(1260, 960))

imgMainAlunos = ctk.CTkImage(light_image=Image.open('imagens/imgAlunoVerde.png'), dark_image=Image.open(
    'imagens/imgAlunoVerde.png'), size=(20, 20))

imgBtnCadastrar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnCadastrar.png'), dark_image=Image.open(
    'imagens/imgBtnCadastrar.png'), size=(26, 26))

imgBtnBuscar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnVisualizar.png'), dark_image=Image.open(
    'imagens/imgBtnVisualizar.png'), size=(26, 26))

imgBtnDesconectar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnDesconectar.png'), dark_image=Image.open(
    'imagens/imgBtnDesconectar.png'), size=(36, 36))

imgBtnHome = ctk.CTkImage(light_image=Image.open('imagens/imgBtnHome.png'), dark_image=Image.open(
    'imagens/imgBtnHome.png'), size=(36, 36))

imgBtnVoltar = ctk.CTkImage(light_image=Image.open('imagens/imgBtnVoltar.png'), dark_image=Image.open(
    'imagens/imgBtnVoltar.png'), size=(36, 36))


#label com imagem do plano de fundo, primeiro item a executar para ser a ultima camada
lblPlanoDFundo = ctk.CTkLabel(telaDir_PesquisaVisualizar, image=imgPlanoDFundo, text='')
lblPlanoDFundo.place(x=0, y=0 )

#======================configurando frames======================
#======================configurando frame de fundo do menu======================
frmFundoMenu = ctk.CTkFrame(telaDir_PesquisaVisualizar, width=1260, height=120, corner_radius=0,
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
frmFundoMain = ctk.CTkFrame(telaDir_PesquisaVisualizar, width=1060, height=740, corner_radius=0,
    fg_color='white')
frmFundoMain.place(x=150, y=170)

#======================configurando widgets do frame do fundo main sistema======================
#label para representar listra divisoria no main
lblListraMain = ctk.CTkLabel(frmFundoMain, text='', fg_color='#1C1C1C', font=('arial bold', 2), width=3, height=740
                             )
lblListraMain.place(x=530, y=0)

#label titulo da pagina
lblTituloCadastro = ctk.CTkLabel(frmFundoMain, text='VISUALIZAR ALUNO', fg_color='white', font=("arial", 50),
    text_color='#1C1C1C')
lblTituloCadastro.place(x=370, y=65)#arrumar posicao

#label subtitulo da pagina
lblSubtituloCadastro = ctk.CTkLabel(frmFundoMain, text='Encontre o aluno desejado em sua turma ou busque-o pelo RM.', fg_color='white',
    font=("arial", 30), text_color='#1C1C1C')
lblSubtituloCadastro.place(x=140, y=150)#arrumar posicao

#label periodo
lblPeriodo= ctk.CTkLabel(frmFundoMain, text='Periodo:', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 16))
lblPeriodo.place(x=105, y=125+60)

#option menu com opcoes dos periodos
optnPeriodo = ctk.CTkOptionMenu(frmFundoMain, values=['Manhã', 'Tarde', 'Noite' ], width=300, height=30, fg_color='#069E6E',
    text_color='white', button_color="#047b55",dropdown_fg_color="#069E6E", dropdown_hover_color="#047b55")
optnPeriodo.set('Qual o período do aluno?')
optnPeriodo.place(x=105, y=160+60)

#label curso
lblCurso= ctk.CTkLabel(frmFundoMain, text='Curso:', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 16))
lblCurso.place(x=105, y=205+60)

#option menu com opcoes dos periodos
optnCurso = ctk.CTkOptionMenu(frmFundoMain, values=['Administração', 'Desenvolvimento de Sistemas', 'Logística', 'Recursos Humanos'],
    width=300, height=30, fg_color='#069E6E', text_color='white', button_color="#047b55",dropdown_fg_color="#069E6E",
    dropdown_hover_color="#047b55")
optnCurso.set('Qual o curso do aluno?')
optnCurso.place(x=105, y=240+60)

#label turma
lblTurma= ctk.CTkLabel(frmFundoMain, text='Turma:', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 16))
lblTurma.place(x=105, y=285+60)

#option menu com opcoes das turmas
optnTurma = ctk.CTkOptionMenu(frmFundoMain, values=['1° Ano', '2° Ano', '3° Ano'], width=300, height=30, fg_color='#069E6E',
    text_color='white', button_color="#047b55",dropdown_fg_color="#069E6E", dropdown_hover_color="#047b55")
optnTurma.set('Qual a turma do aluno?')
optnTurma.place(x=105, y=320+60)

#======================funcoes======================
#funcao do botao buscar turma
def buscarTurma():
    periodo = optnPeriodo.get()
    curso = optnCurso.get()
    turma = optnTurma.get()
    
    if periodo == 'Qual o período do aluno?':
        messagebox.showinfo(title='Campos não selecionados', message='Selecione alguma opção do campo período.')
    elif curso == 'Qual o curso do aluno?':
        messagebox.showinfo(title='Campos não selecionados', message='Selecione alguma opção do campo curso.')
    elif turma == 'Qual a turma do aluno?':
        messagebox.showinfo(title='Campos não selecionados', message='Selecione alguma opção do campo turma.')
    else:
        messagebox.showinfo(title='Busca por turma', message='Busca realizada com sucesso')
        
#botao cadastrar aluno
btnBuscarTurma = ctk.CTkButton(frmFundoMain, text='Buscar na turma', width=200, height=20,corner_radius=50,
    fg_color='#069E6E', font=("arial", 18), hover_color='#047b55', image=imgBtnBuscar, text_color='white',
    command=buscarTurma)
btnBuscarTurma.place(x=155,y=400+60)


#label pesquisar RM
lblRM= ctk.CTkLabel(frmFundoMain, text='Pesquisar por RM:', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 16))
lblRM.place(x=600, y=205+60)

lblImgAluno = ctk.CTkButton(frmFundoMain, width=60, height=30, image=imgMainAlunos, text='',fg_color='#069E6E',
    hover_color='#069E6E', corner_radius=20)
lblImgAluno.place(x=630, y=240+60)

#entry pesquisar rm
etyPesquisarRM = ctk.CTkEntry(frmFundoMain, width=300, height=30, fg_color='#069E6E', text_color='white')
etyPesquisarRM.place(x=600, y=240+60)

#botao pessquisar rm
btnBuscarRM = ctk.CTkButton(frmFundoMain, text='Buscar por RM', width=260, height=20,corner_radius=50,
    fg_color='#069E6E', font=("arial", 20), hover_color='#047b55', image=imgBtnBuscar, text_color='white')
btnBuscarRM.place(x=600,y=285+60)



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
frmFundoMenuLateral = tk.Frame(telaDir_PesquisaVisualizar, width=100, bg="#069E6E")
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
    telaDir_PesquisaVisualizar.destroy()

#botão desconectar separado na parte inferior do menu
btnDesconectarMenuLateral = ctk.CTkButton(frmFundoMenuLateral, text="", corner_radius=0, fg_color="#069E6E", 
    hover_color='#047b55', image=imgBtnDesconectar, command=desconectar)
btnDesconectarMenuLateral.configure(width=100, height=70)
btnDesconectarMenuLateral.place(x=0, y=862)

#rodando a janela
telaDir_PesquisaVisualizar.mainloop()

