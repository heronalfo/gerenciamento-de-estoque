def opção2():
     
    from pandas import read_sql
    from os import system
    import sqlite3 as SQL
    import manage
    
    
    
    system('clear')
    
    
    
    with SQL.connect('date.db') as conn:
    	c = conn.cursor()
    	
    
    #try:
    print('{:>37}'.format('PAINEL FORGES'))
    print('-'*70)	
    relatorio = read_sql('SELECT * FROM produtos', conn)
    	
    print(relatorio, '\n')
    	
    	
    mDP = int(relatorio['preço'].sum() / len(relatorio['preço']))
    		
    qDE = relatorio['estoque'].sum()	
    	
    F = relatorio['faturamento'].sum()
        
    opção = int(input('         | [1] PESQUISAR | [2] REMOVER | [3] SAIR |'))
    
    if  opção == 1:
        print('-'*70)
        pesquisar = str(input('NOME DO PRODUTO: '))
        
        resposta =  read_sql(f'''SELECT * FROM produtos WHERE produto = "{pesquisar}" ''', conn)
        
        system('clear')
        
        print(resposta)
        
        print('-'*70)
        input('\n\n[ENTER]')
        system('clear')
        
    elif opção == 2:
        
        print('-'*70)
        itemApagar = str(input('ID DO PRODUTO: '))
        
        c.execute(f'''DELETE  FROM produtos WHERE id = {itemApagar} ''')
        
        conn.commit()
        
        system('clear')
        
        
        opção2()
    
    elif opção == 3:
        system('clear')
        
    
    
    
    
    
    manage.PAINEL()

if __name__ == '__main__':
	opção2()