import sqlite3
conexao = sqlite3.connect('agenda.db')

cursor = conexao.cursor()
cursor.execute('create table agenda (nome text, telefone text)')

cursor.execute('insert into agenda(Nome, telefone) values(?, ?), ("ranie", "95473-8290")')

conexao.commit()
cursor.close()
conexao.close()