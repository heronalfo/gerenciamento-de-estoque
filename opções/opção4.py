def opção4():
    
    from datetime import datetime
    from os import system
    import sqlite3 as SQL
    import manage
    
    
    
    with SQL.connect('date.db') as conexão:
    	c = conexão.cursor() 
    
    horario = datetime.now()
    
    system('clear')
        
    print('', '-'*30, '\n{:>21}\n'.format('RETIRADA E VENDA'), '-'*30)
        
    PRODUTO = str(input(' DIGITE O ID DO PRODUTO: '))
    
    PRODUTO = int(PRODUTO)
    
    print('','-'*30)
            
    QUANTIDADE = int(input(' QUANTIDADE: ')
    )
    
    if QUANTIDADE < 1:
    	system('clear')
    	print('QUANTIDADE INVALIDA!')
    	opção4()
        
    
    valor = c.execute(f'''SELECT preço FROM produtos WHERE id = {PRODUTO}''')
      
    
    PREÇOS = valor.fetchone()
    PREÇO = PREÇOS[0]*QUANTIDADE
        
       
    c.execute(f'''UPDATE produtos SET faturamento = faturamento + {float(PREÇO)} WHERE id = {PRODUTO}''')
    
    print('','-'*30)
    
    
    
    
    
    print(f' Preço {PREÇO} R$')
    
    c.execute(f'''UPDATE produtos SET estoque = estoque - {QUANTIDADE} WHERE id = {PRODUTO}''')
    
    
    c.execute(
    f'''
    
    INSERT INTO vendas (
    
    id_produto,
    quantidade,
    preço,
    horario
    )
    
    VALUES (
    '{PRODUTO}',
    '{QUANTIDADE}',
    '{PREÇO}',
    '{horario}'
    
    
    
    )
    
    '''
    )
    
    
    conexão.commit()
    
    input('\n [PRESS ENTER]')
    
    system('clear')
    
    manage.PAINEL()
    
if __name__ == "__main__":
	opção4()