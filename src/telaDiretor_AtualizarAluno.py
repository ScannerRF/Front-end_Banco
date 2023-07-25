#importando as bibliotecas
import customtkinter as ctk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

#======================criando a janela======================
telaDir_AtualizarAluno = ctk.CTk(fg_color='#f1f1f1')

#======================configurando a janela principal======================
telaDir_AtualizarAluno.title('Diretor - Atualizar Aluno')
telaDir_AtualizarAluno.geometry('1260x960')
telaDir_AtualizarAluno.resizable(False, False)
telaDir_AtualizarAluno._set_appearance_mode('dark')

#======================funcao======================
#funcao para iniciar a janela centralizada
def centralizarTela(telaDir_AtualizarAluno):
    telaDir_AtualizarAluno.update_idletasks()
    width = telaDir_AtualizarAluno.winfo_width()
    height = telaDir_AtualizarAluno.winfo_height()
    screen_width = telaDir_AtualizarAluno.winfo_screenwidth()
    screen_height = telaDir_AtualizarAluno.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    telaDir_AtualizarAluno.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#funcao para centralizar a janela
centralizarTela(telaDir_AtualizarAluno)

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
lblPlanoDFundo = ctk.CTkLabel(telaDir_AtualizarAluno, image=imgPlanoDFundo, text='')
lblPlanoDFundo.place(x=0, y=0 )

#======================configurando frames======================
#======================configurando frame de fundo do menu======================
frmFundoMenu = ctk.CTkFrame(telaDir_AtualizarAluno, width=1260, height=120, corner_radius=0,
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
frmFundoMain = ctk.CTkFrame(telaDir_AtualizarAluno, width=1060, height=740, corner_radius=0,
    fg_color='white')
frmFundoMain.place(x=150, y=170)

#======================configurando widgets do frame fundo do main======================
#label titulo da pagina
lblTituloCadastro = ctk.CTkLabel(frmFundoMain, text='ATUALIZAR ALUNO', fg_color='white', font=("arial", 50),
    text_color='#1C1C1C')
lblTituloCadastro.place(x=300, y=100)#arrumar posicao

#label subtitulo da pagina
lblSubtituloCadastro = ctk.CTkLabel(frmFundoMain, text='Atualize as respectivas informações desejadas do aluno.', fg_color='white',
    font=("arial", 30), text_color='#1C1C1C')
lblSubtituloCadastro.place(x=158, y=160)#arrumar posicao

#label nome do aluno
lblNomeAluno= ctk.CTkLabel(frmFundoMain, text='Nome:', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 16))
lblNomeAluno.place(x=65, y=250)

#caixa de texto nome do aluno
etyNomeAluno = ctk.CTkEntry(frmFundoMain, width=300, height=30, placeholder_text='Insira o nome completo do aluno',
    font=('arial bold', 12), fg_color='#069E6E', text_color='white',placeholder_text_color='white')
etyNomeAluno.place(x=65, y=250+35)

#label rm do aluno
lblRmAluno= ctk.CTkLabel(frmFundoMain, text='RM:', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 16))
lblRmAluno.place(x=65, y=250+35+45)

#caixa de texto rm do aluno
etyRmAluno = ctk.CTkEntry(frmFundoMain, width=300, height=30, placeholder_text='Insira o RM do aluno',
    font=('arial bold', 12), fg_color='#069E6E', text_color='white',placeholder_text_color='white')
etyRmAluno.place(x=65, y=250+35+45+35)

#label sataus matricula do aluno
lblStatus= ctk.CTkLabel(frmFundoMain, text='Status de Matrícula:', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 16))
lblStatus.place(x=65, y=250+35+45+35+45)

estado_var = tk.IntVar()
estado_var.set(1)  # Define o estado inicial como ativado

rdoAtivado = ctk.CTkRadioButton(frmFundoMain, text="Ativado", variable=estado_var, 
    value=1, text_color='#1C1C1C', fg_color='#069E6E', hover_color="#047b55")
rdoAtivado.place(x=65, y=250+35+45+35+45+35)

rdoDesativado = ctk.CTkRadioButton(frmFundoMain, text="Desativado", variable=estado_var,
    value=2, text_color='#1C1C1C', fg_color='#069E6E', hover_color="#047b55")
rdoDesativado.place(x=270, y=250+35+45+35+45+35)

#label periodo
lblPeriodo= ctk.CTkLabel(frmFundoMain, text='Período:', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 16))
lblPeriodo.place(x=415, y=250)#35 ENTRE LBL  e entry e 45 outro

#option menu com opcoes dos periodos
optnPeriodo = ctk.CTkOptionMenu(frmFundoMain, values=['Manhã', 'Tarde', 'Noite' ], width=300, height=30,
    fg_color='#069E6E',text_color='white', button_color="#047b55",dropdown_fg_color="#069E6E",
    dropdown_hover_color="#047b55")
optnPeriodo.set('Qual o período do aluno?')
optnPeriodo.place(x=415, y=250+35)

#label curso
lblCurso= ctk.CTkLabel(frmFundoMain, text='Curso:', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 16))
lblCurso.place(x=415, y=250+35+45)

#option menu com opcoes dos periodos
optnCurso = ctk.CTkOptionMenu(frmFundoMain, values=['Administração', 'Desenvolvimento de Sistemas', 'Logística', 'Recursos Humanos'],
    width=300, height=30, fg_color='#069E6E', text_color='white', button_color="#047b55",
    dropdown_fg_color="#069E6E",dropdown_hover_color="#047b55")
optnCurso.set('Qual o curso do aluno?')
optnCurso.place(x=415, y=250+35+45+35)

#label turma
lblTurma= ctk.CTkLabel(frmFundoMain, text='Turma:', fg_color='white', text_color='#1C1C1C',
    font=('arial bold', 16))
lblTurma.place(x=415, y=250+35+45+35+45)
#option menu com opcoes das turmas
optnTurma = ctk.CTkOptionMenu(frmFundoMain, values=['1° Ano', '2° Ano', '3° Ano'], width=300, height=30, fg_color='#069E6E',
    text_color='white', button_color="#047b55",dropdown_fg_color="#069E6E", dropdown_hover_color="#047b55")
optnTurma.set('Qual a turma do aluno?')
optnTurma.place(x=415, y=250+35+45+35+45+35)


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
        lblImgAluno.configure(image=imagem_tk, text='', width=200, height=240)
        lblImgAluno.image = imagem_tk  # Manter uma referência à imagem


#label para exibir a imagem
lblImgAluno = ctk.CTkLabel(frmFundoMain, text='Foto do Aluno', bg_color='#f1f1f1', width=200, 
    height=240, text_color='#1C1C1C')
lblImgAluno.place(x=765, y=250)

#botão para carregar a imagem
btnCarregarFtAluno = ctk.CTkButton(frmFundoMain, text="Carregar foto do aluno", command=carregar_imagem,
    width=200, height=20, fg_color='#069E6E', font=("arial", 14), hover_color='#047b55', 
    text_color='white')
btnCarregarFtAluno.place(x=765, y=500)

#======================funcoes======================
#funcao do botao atualizarAluno aluno
def atualizarAluno():
    nomeAluno = etyNomeAluno.get()
    rmAluno = etyRmAluno.get()
    periodo = optnPeriodo.get()
    curso = optnCurso.get()
    turma = optnTurma.get()

    if nomeAluno == '':
        tk.messagebox.showwarning(title='Campos não preenchidos', message='Preencha o campo nome.')
    elif rmAluno == '':
        tk.messagebox.showwarning(title='Campos não preenchidos', message='Preencha o campo RM.')
    elif periodo == 'Qual o período do aluno?':
        tk.messagebox.showwarning(title='Campos não selecionados', message='Selecione alguma opção do campo período.')
    elif curso == 'Qual o curso do aluno?':
        tk.messagebox.showwarning(title='Campos não selecionados', message='Selecione alguma opção do campo curso.')
    elif turma == 'Qual a turma do aluno?':
        tk.messagebox.showwarning(title='Campos não selecionados', message='Selecione alguma opção do campo turma.')
    else:
        tk.messagebox.showinfo(title='Atualizar', message='Dados atualizados com sucesso')

#botao cadastrar aluno
btnAtualizar = ctk.CTkButton(frmFundoMain, text='Atualizar aluno', width=298, height=50,corner_radius=50,
    fg_color='#069E6E', font=("arial", 20), hover_color='#047b55', image=imgBtnAtualizar,
    text_color='white', command=atualizarAluno)
btnAtualizar.place(x=381,y=590)

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
frmFundoMenuLateral = tk.Frame(telaDir_AtualizarAluno, width=100, bg="#069E6E")
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
    telaDir_AtualizarAluno.destroy()

#botão desconectar separado na parte inferior do menu
btnDesconectarMenuLateral = ctk.CTkButton(frmFundoMenuLateral, text="", corner_radius=0, fg_color="#069E6E", 
    hover_color='#047b55', image=imgBtnDesconectar, command=desconectar)
btnDesconectarMenuLateral.configure(width=100, height=70)
btnDesconectarMenuLateral.place(x=0, y=862)

#rodando a janela
telaDir_AtualizarAluno.mainloop()

