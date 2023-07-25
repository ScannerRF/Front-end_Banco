#Importações do Banco 
import sqlite3 

#Cria o Banco em Si
conn = sqlite3.connect("Scanner.db")
cursor = conn.cursor()

#Cria a Tabela users ---> Para o acesso dos seguranças e do diretor ao sistema
cursor.execute("""
CREATE TABLE IF NOT EXISTS users( 
    Username TEXT NOT NULL, 
   Password TEXT NOT NULL

)""")

#Cria a tabela cadastroAlu ---> Para cadastrar os alunos
cursor.execute("""
CREATE TABLE IF NOT EXISTS cadastroAlu(
    Nome TEXT NOT NULL,
    RM INTEGER NOT NULL,
    Periodo TEXT NOT NULL, 
    Curso TEXT NOT NULL, 
    Turma TEXT NOT NULL, 
    FotoAlu BLOB NOT NULL
);
""")

#Insere os dados na tabela users 
#cursor.execute("""
#INSERT INTO users(Username, Password)
#VALUES('Diretor', '1234')
#""")

#cursor.execute("""
#INSERT INTO users(Username, Password)
#VALUES('Segurança1', 'SeguOne')
#""")

#cursor.execute("""
#INSERT INTO users(Username, Password)
#VALUES('Segurança2', 'SeguTwo')
#""")

#cursor.execute("""
#INSERT INTO users(Username, Password)
#VALUES('Segurança3', 'SeguThree')
#""")

#Atualiza no Banco 
conn.commit()

#Usar o SQLBrowser pro controle do Banco# 

