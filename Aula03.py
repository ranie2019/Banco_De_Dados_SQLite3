import sqlite3

dados = [('ana', '93750-3847'), ('maria', '9385-7134'), ('joao', '9501-6748')]

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.executemany('insert into agenda(Nome, Telefone) values(?, ?)',dados)

conexao.commit()
cursor.close()
conexao.close()