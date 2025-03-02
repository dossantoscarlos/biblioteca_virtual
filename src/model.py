from datetime import datetime

class Livro : 
    def __init__(self, titulo, autor, ano_publicacao_str) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = self.__ano_publicacao_str(ano_publicacao_str)
    
    def __ano_publicacao_str(self, ano_publicacao) -> str :
        ano_publicacao =ano_publicacao.replace('/', '-')

        date_split = ano_publicacao.split('-')
        
        if len(date_split) != 3:
            raise Exception('Ano de publicação inválido')
        
        if not date_split[0].isnumeric() or not date_split[1].isnumeric() or not date_split[2].isnumeric():
            raise Exception('Data formatada errada.')
        
        if len(date_split[0]) < 4 and len(date_split[2]) < 4:
            raise Exception('Data formatada errada.')
        
        if len(date_split[0]) > 2 :
            ano_publicacao = f'{date_split[2]}-{date_split[1]}-{date_split[0]}'
        elif len(date_split[2]) > 2 :
            ano_publicacao = f'{date_split[0]}-{date_split[1]}-{date_split[2]}'
            
        publicacao = datetime.strptime(ano_publicacao, '%d-%m-%Y')
        
        return publicacao.strftime('%d/%m/%Y')
    