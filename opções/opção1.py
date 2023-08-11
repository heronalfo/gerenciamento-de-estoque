def opção1():
    
    from datetime import datetime
    from os import system
    import sqlite3 as SQL
      
  
      
    with SQL.connect('date.db') as conexão:
    	c = conexão.cursor()
    	
    
    horario = datetime.now()
    	
    system('clear')
            
    print('','-'*30, '\n{:>21}\n'.format('CADASTRO DE PRODUTOS'), '-'*30)
        
        
    produto = str(input(' PRODUTO: '))
    
    if len(produto) < 1:
    	print('PRODUTO INVALIDO!')
    	opção1()
    		
            
    print('-'*30)
   
    preço = str(input(' PREÇO: ')).replace(',', '.')
       
    if len(preço) < 1:
    	system('clear')
    	print('PREÇO INVALIDO!')
    	opção1()
    	
            
    print('-'*30)
   
    	
    estoque = int(input(' ESTOQUE: '))
    
    if estoque < 1:
    	system('clear')
    	print('ESTOQUE INVALIDO!')
    	opção1()
    	
    
    print('-'*30)
        
    c.execute(f''' INSERT INTO produtos (produto, preço, estoque, data) VALUES ('{produto}','{float(preço)}', '{estoque}', '{horario.date()}')
    '''
    )
    
    conexão.commit()
    system('clear')
           
    print(' PRODUTO CADASTRADO')
   
if __name__ == '__main__':
	opção1()