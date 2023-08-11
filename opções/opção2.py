def opção2():
     
    from pandas import read_sql
    from os import system
    import sqlite3 as SQL
    import manage
    
    
    
    system('clear')
    
    
    
    with SQL.connect('date.db') as conexão:
    	c = conexão.cursor()
    	
    
    try:
    	
    	relatorio = read_sql('SELECT * FROM produtos', conexão)
    	
    	print(relatorio, '\n')
    	
    	
    	mDP = int(relatorio['preço'].sum() / len(relatorio['preço']))
    		
    	qDE = relatorio['estoque'].sum()	
    	
    	F = relatorio['faturamento'].sum()
    	
    	
    	print('-'*30)
    	
    	rel = {'Média de preço:': mDP, 'Quantidade em estoque:': qDE, 'Faturamento total:': F}
    	
    	#print(rel)
        	
    except:
    		
    	print('Nenhum produto cadastrado. \n')
    	
    finally:
    	
    	input('\n\n[PRESS ENTER]')
    	system('clear')
    
    manage.PAINEL()

if __name__ == '__main__':
	opção2()