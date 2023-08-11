def opção5():
    
    from os import system
    import manage
    
    system('clear')
            
    print(
        '',
        '-'*30,
        '\n{:>21}\n'.format('EDITAR PRODUTO'),
        '-'*30)
        
    ID = str(input(' DIGITE O ID DO PRODUTO: ')
    )
            
    print('','-'*30)
            
    prg1 = input(' DESEJA ALTERAR O NOME? [S/N]')
            
    if prg1 == 'S':
        print('','-'*30)
                
        NOVO_NOME = str(input(' NOVO NOME: '))
        
        if len(NOVO_NOME) < 1:
        	system('clear')
        	print('NOME INVALIDO!')
        	opção5()
        	
                
        c.execute(
                f'''
                UPDATE produtos SET produto = '{NOVO_NOME}' WHERE id = {ID}
                
                ''')
                
    print('','-'*30)
            
            
    prg2 = input(' DESEJA ALTERAR O PREÇO?  [S/N]')
    if prg2 == 'S':
        print('-'*30)
        
        NOVO_VALOR = str(input(' DIGITE O NOVO PREÇO: ')).replace(',', '.')
                
        VALOR_INT = float(NOVO_VALOR)
        
        if VALOR_INT < 1:
        	system('clear')
        	print('VALOR INVALIDO!')
        	opção5()
        	
                
        c.execute(
                f'''
                
                UPDATE produtos SET preço = {VALOR_INT} WHERE id = {ID}
                
                '''
                
                
        )
                
        print('-'*30)
            
        prg3 = input(' DESEJA ALTERAR O ESTOQUE? [S/N]')
            
        if prg3 == 'S':
                
            print('','-'*30)
            NOVO_ESTOQUE = int(input(' NOVO ESTOQUE: '))
            
            if NOVO_ESTOQUE < 1:
            	system('clear')
            	print('ESTOQUE INVALIDO!')
            	opção1()
            
            c.execute(
                f'''
               UPDATE produtos SET estoque = {NOVO_ESTOQUE} WHERE id = {ID}
                
                ''')       
           
        prg4 = input(' DESEJA ALTERAR A DATA DE CADASTRO DO PRODUTO? [S/N] ')
         
        if prg4 == 'S':
         	print('','-'*30)
         	
         	
         	padrao = re.compile('\d{2}/\d{2}/\d{4}')
         	
         	DATA = str(input(' NOVA DATA: '))
         	
         	if re.match(padrao, DATA):
         		
         		c.execute(f''' UPDATE produtos SET data = {DATA} WHERE id = {ID}''')
    	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
        	
            	
                
            
        system('clear')       
        manage.PAINEL()
            
        conexão.commit()        