import sqlite3 as SQL

with SQL.connect('date.db') as conexão:
    c = conexão.cursor()
        

      
class produtos:
    def __init__(self):
        c.execute(
    '''
    	  
    CREATE TABLE IF NOT EXISTS produtos(
    
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      produto VARCHAR, 
      preço FLOAT, 
      estoque INT,
      faturamento FLOAT default 0,
      data VARCHAR,
      edição VARCHAR
    
   )
   
   '''
    
      )
        
class vendas:
    def __init__(self):
    	c.execute(
    	
    '''
    
    CREATE TABLE IF NOT EXISTS vendas(

      id_venda INTEGER PRIMARY KEY AUTOINCREMENT,        id_produto, 
      quantidade INT,
      preço FLOAT,
      horario VARCHAR
      
    )
        
        
    '''
        )


conexão.commit()