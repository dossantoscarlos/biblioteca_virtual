from sqlite3 import connect as conection

class DatabaseConnection : 
    def conexao(self): 
        connection = conection('livraria.db')
        return connection
        