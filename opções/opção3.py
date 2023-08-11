def opção3():
    
    from os import system
    import sqlite3 as SQL
    import manage
    
    
    
    with SQL.connect('date.db') as conexão:
    	c = conexão.cursor() 	
    	
    system('clear')
    
    print('', '-'*30, '\n{:>21}\n'.format('DELETAR ITEM'), '-'*30)
        
    ID = int(input('DIGITE O ID: '))
    
    if ID == 00:
        system('clear')
        manage.PAINEL()
        
    c.execute(f'''DELETE  FROM produtos WHERE id = '{ID}' ''')
        
    conexão.commit()
        
    system('clear')
    
    print(' ITEM REMOVIDO COM SUCESSO!')
    
    manage.PAINEL()

if __name__ == '__main__':
	opção3()  