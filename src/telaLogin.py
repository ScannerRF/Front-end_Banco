#importando as bibliotecas
import customtkinter as ctk
from tkinter import *
from PIL import Image
from subprocess import run
import DataBase
from tkinter import messagebox 

#======================criando a janela======================
telaLogin = ctk.CTk(fg_color='white')

#======================configurando a janela principal======================
telaLogin.title('Login')
telaLogin.geometry('700x400')
telaLogin.resizable(False, False)
telaLogin._set_appearance_mode('dark')

#======================funcao======================
#funcao para iniciar a janela centralizada
def centralizarTela(telaLogin):
    telaLogin.update_idletasks()
    width = telaLogin.winfo_width()
    height = telaLogin.winfo_height()
    screen_width = telaLogin.winfo_screenwidth()
    screen_height = telaLogin.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    telaLogin.geometry('{}x{}+{}+{}'.format(width, height+20, x, y-50))

#funcao para centralizar a janela
centralizarTela(telaLogin)

#======================configurando imagem======================
imgLogo = ctk.CTkImage(light_image=Image.open('imagens/imgLogo.png'), dark_image=Image.open('imagens/imgLogo.png'), size=(250, 280))

#======================configurando menu======================
#barra do menu de opçoes
barraDeMenus = Menu(telaLogin)

#elemento da barra de menu, dentro da barra
menuOpcoes = Menu(barraDeMenus, tearoff=0)

#menu dropdown com nome para identificar
barraDeMenus.add_cascade(label='Opções', menu=menuOpcoes)

#subitens do menu Opcoes
menuOpcoes.add_command(label='Sair')

#adicionando a barra
telaLogin.config(menu=barraDeMenus)

#label com imagem da logo
lblImgLogo = ctk.CTkLabel(telaLogin, image=imgLogo, text='')
lblImgLogo.place(x=45, y=55)

#======================configurando frame fundo do login======================
#frame de fundo do login
frmFundoLogin = ctk.CTkFrame(telaLogin, width=348, height=390, corner_radius=10, fg_color='#1C1C1C')
frmFundoLogin.place(x=345, y=5)

#======================configurando widgets do frame fundo do login======================
#titulo
ctk.CTkLabel(frmFundoLogin, text='Fazer login', fg_color='#1C1C1C', text_color='white',
    font=('arial bold', 26)).place(x=115, y=50)

#subtitulo
ctk.CTkLabel(frmFundoLogin, text='Faça o login para acessar o sistema.', fg_color='#1C1C1C', text_color='white',
    font=('arial bold', 12)).place(x=75, y=80)

#label Usuario
lblUsuario = ctk.CTkLabel(frmFundoLogin, text='Usuário:', fg_color='#1C1C1C', text_color='white',
    font=('arial bold', 16))
lblUsuario.place(x=25, y=125)

#caixa de texto Usuario
etyUsuario = ctk.CTkEntry(frmFundoLogin, width=298, height=30, placeholder_text='Insira o seu usuário',
    font=('arial bold', 12))
etyUsuario.place(x=25, y=160)

#label senha
lblSenha = ctk.CTkLabel(frmFundoLogin, text='Senha:', fg_color='#1C1C1C', text_color='white',
    font=('arial bold', 16))
lblSenha.place(x=25, y=205)

#caixa de texto senha
etySenha = ctk.CTkEntry(frmFundoLogin, width=298, height=30, placeholder_text='Insira a sua senha',
    font=('arial bold', 12), show='*')
etySenha.place(x=25, y=240)

#======================funcoes======================
#funcao de ver senha
def exibirSenha():
    #ao clicar na checkbox ira executar a estrutura de decisao
    #se a visibilidade dos dados do campo senha ja estiver setado com '*'
    if etySenha.cget('show') == '*':
        #setando para aparecer a senha
        etySenha.configure(show='')
    else:
        #setando para esconder a senha
        etySenha.configure(show='*')

#checkbox com opção de visualizar senha
chkboxExibirSenha = ctk.CTkCheckBox(frmFundoLogin, text='Exibir senha', checkbox_width=20, checkbox_height=20,
    fg_color='#069E6E', hover_color='#047b55', command=exibirSenha)
chkboxExibirSenha.place(x=25, y=285)
#setando como desabilitado a opção de ver senha, ira aparecer somente quando o campo senha receber algo
chkboxExibirSenha.configure(state=DISABLED)

#======================funcoes======================
#funcao do botao login

def Banco():
    Username = etyUsuario.get()
    Password = etySenha.get()
    DataBase.cursor.execute("""
    SELECT * FROM users 
    WHERE (Username = ? and Password = ?)
    """,(Username, Password))
    VerifyLogin = DataBase.cursor.fetchone()
    if Username == '':
        messagebox.showinfo(title='Campos não preenchidos!', message='Preencha o campo usuário!')
        #se o campo senha nao for preenchido...
    elif Password == '':
        messagebox.showinfo(title='Campos não preenchidos', message='Preencha o campo senha!')
    else:
        try:
            if (Username in VerifyLogin and Password in VerifyLogin):
                messagebox.showinfo(title="Login Info", message="Acesso confirmado!!")
        except:
            messagebox.showinfo(title="Login Info", message="Acesso negado. Dados incorretos!") 
    

#botão fazer login
btnLogin = ctk.CTkButton(frmFundoLogin, text='Login', width=298, height=30, fg_color='#069E6E',
                         hover_color='#047b55', text_color='white', command=Banco
                        )
btnLogin.place(x=25, y=320)

#======================funcoes======================
#funcao acionada quando o campo de senha recebe o foco
def habilitarExibirSenha(event):
    #se o campo senha receber algo, ira habilitar a opção ver senha
    if etySenha.get():
        chkboxExibirSenha.configure(state=NORMAL)
#associa o evento de foco a funcao
etySenha.bind("<FocusIn>", habilitarExibirSenha)

#funcao para verificar a entrada no campo de senha
def verificarEntradaSenha(event):
    #verifica se há algum valor no campo de senha
    if etySenha.get():
        #se houver valor habilita a caixa de seleção
        chkboxExibirSenha.configure(state=NORMAL)
    else:
        #caso contrário desabilita a caixa de seleção
        chkboxExibirSenha.configure(state=DISABLED)
#associa a funcao de verificação ao evento de tecla pressionada ("<Key>") do campo de senha
etySenha.bind("<Key>", verificarEntradaSenha)

#rodando a janela
telaLogin.mainloop()
