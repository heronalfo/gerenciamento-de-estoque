import sqlite3

conexão = sqlite3.connect('datebase.db')
c = conexão.cursor()
        

      
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
        
c.execute(
    	
    '''
    
    CREATE TABLE IF NOT EXISTS vendas(

      id_venda INTEGER PRIMARY KEY AUTOINCREMENT,        
      id_produto, 
      quantidade INT,
      preço FLOAT,
      horario VARCHAR
      
    )
        
        
    '''
)


conexão.commit()