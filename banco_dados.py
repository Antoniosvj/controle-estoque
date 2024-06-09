import sqlite3 as conector

class AppBd:
    def __init__(self):
        self.connection = None
        self.cursor = None
        print('Metodo Construtor')
        
    def abrirConexao(self):
        try:
            self.connection = conector.connect('controle_estoque.db')
            self.cursor = self.connection.cursor()
            print('Banco de dados conectado com sucesso.')
        except(Exception, conector.Error) as error:
            print("Falha ao se conectar ao Banco de Dados.")
    
    def fecharConexao(self):   
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print('A conexão com Banco de Dados foi fechada.')
            
    def criarTabela(self):
        self.abrirConexao()
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS produtos (
                    codigo INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    precoCompra REAL NOT NULL,
                    precoVenda REAL NOT NULL
                );                    
            ''')
            self.connection.commit()
            print('Tabela de produtos criada com sucesso.')
        except Exception as error:
            print("Falha ao criar a tabela produtos", error)
        finally:
            self.fecharConexao()

    def selecionarProduto(self):
        registros = []      
        try:
            self.abrirConexao()
            selecionar = """SELECT * FROM produtos"""
            self.cursor.execute(selecionar)
            registros = self.cursor.fetchall()
            print(registros)
        except (Exception, conector.Error) as error:
            print('Erro ao conectar ao Banco de Dados.', error)
        finally:
            self.fecharConexao()
        return registros
    
    def inserirProduto(self, codigo, nome, quantidade, precoCompra, precoVenda):
        self.criarTabela()
        try:
            self.abrirConexao()
            sql_criar = """ INSERT INTO produtos (codigo, nome, quantidade, precoCompra, precoVenda)
                        VALUES (?, ?, ?, ?, ?);"""
            dados = (codigo, nome, quantidade, precoCompra, precoVenda)
            self.cursor.execute(sql_criar, dados)
            self.connection.commit()
            print("Produto inserido com sucesso.")
        except (Exception, conector.Error) as error:
            print('Falha ao conectar ao banco de dados', error)
        finally: self.fecharConexao()
         
    def excluirProduto(self, codigo):
        try:
            self.abrirConexao()
            comando = """DELETE FROM produtos WHERE codigo =?"""
            self.cursor.execute(comando, (codigo,))
            self.connection.commit()
            print('Dados excluidos com sucesso.')
        except (Exception, conector.Error) as error:
            print('Falha ao conectar ao Banco de Dados', error)
        finally:
            self.fecharConexao()

    def atualizarProduto(self):
        try:
            self.abrirConexao()
            comando = """UPDATE produtos SET nome = ?, quantidade = ?, precoCompra = ?, precoVenda = ? WHERE codigo = ?;"""
            self.cursor.execute(comando, ('lapis', 100, 0.75, 1.50, 1))
            self.connection.commit()
            print('Produto atualizado com sucesso.')
        except (Exception, conector.Error) as error:
            print('Falha ao conectar ao Banco de Dados')
        finally:
            self.fecharConexao()
           
#Testando a classe
app_bd = AppBd()
app_bd.selecionarProduto()