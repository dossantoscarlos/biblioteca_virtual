from src.database import DatabaseConnection
from src.model import Livro
try : 
    con = DatabaseConnection().conexao()
    
    try : 
        livro = Livro('Dom Quixote', 'Miguel de Cervantes', '1605-04-16')
    except Exception as e:
        print(e)

    con.execute('''Create table if not exists Livro(
                    id integer primary key autoincrement,
                    titulo text,
                    autor text,
                    ano_publicacao text
                )''')

    con.commit()

    con.execute(
        '''Insert into Livro (titulo, autor, ano_publicacao) 
        values (:titulo, :autor, :ano_publicacao)''', 
        vars(livro)
    )

    con.commit()

    for row in con.execute('Select * from Livro'):    
        row = row[1:]
        livro = Livro(*row)
        print(vars(livro))

except Exception as e:
    print(e)

finally :
    con.close()