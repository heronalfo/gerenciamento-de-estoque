from os import system
from pandas import read_sql, DataFrame
from main import PAINEL
from datetime import datetime
import sqlite3 as SQL
import date
import re

horario = datetime.now()

with SQL.connect('date.db') as conexão:
	c = conexão.cursor()



def opção1():
    system('clear')
            
    print(
        '',
        '-'*30,
        '\n{:>21}\n'.format('CADASTRO DE PRODUTOS'),
        '-'*30)
        
        
    PRODUTO = str(input(' PRODUTO: '))
    
    if len(PRODUTO) < 1:
    	print('PRODUTO INVALIDO!')
    	opção1()
    	
    	
            
    print('-'*30)
    PREÇO = str(input(' PREÇO: ')).replace(',', '.')
    
    if len(PREÇO) < 1:
    	system('clear')
    	print('PREÇO INVALIDO!')
    	opção1()
    	
            
    print('-'*30)
   
    	
    ESTOQUE = int(input(' ESTOQUE: '))
    
    if ESTOQUE < 1:
    	system('clear')
    	print('ESTOQUE INVALIDO!')
    	opção1()
    	
    
    
    print('-'*30)
        
    c.execute(
        f'''
          INSERT INTO produtos
          (produto, preço, estoque, data)
          VALUES (
          
          '{PRODUTO}', 
          '{float(PREÇO)}',
          '{ESTOQUE}',
          '{horario.date()}'
          
          )
    '''
    )
    
    conexão.commit()
        
    system('clear')
            
    PAINEL()
    print(' PRODUTO CADASTRADO')
            


def opção2():
    
    	
    system('clear')
    
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
            
    PAINEL()




def opção3():
    system('clear')
    print(
        '',
        '-'*30,
        '\n{:>21}\n'.format('DELETAR ITEM'),
        '-'*30)
        
    ID = int(input('DIGITE O ID: '))
        
    c.execute(
        f'''
        DELETE  FROM produtos WHERE id = '{ID}'
        '''
            )
        
    conexão.commit()
        
    system('clear')
    PAINEL()
    
    print(' ITEM REMOVIDO COM SUCESSO!')
            
        




def opção4():
    system('clear')
        
    print(
        '',
        '-'*30,
        '\n{:>21}\n'.format('RETIRADA E VENDA'),
        '-'*30)
        
    PRODUTO = str(input(' DIGITE O ID DO PRODUTO: '))
    
    PRODUTO = int(PRODUTO)
    
    print('','-'*30)
            
    QUANTIDADE = int(input(' QUANTIDADE: ')
    )
    
    if QUANTIDADE < 1:
    	system('clear')
    	print('QUANTIDADE INVALIDA!')
    	opção4()
    
    	
    
    	
        
    c.execute(f'''UPDATE produtos SET estoque = estoque - {QUANTIDADE} WHERE id = {PRODUTO}''')
    
    
    
        
    
        
    valor = c.execute(f'''SELECT preço FROM produtos WHERE id = {PRODUTO}''')
    
    PREÇOS = valor.fetchone()
    PREÇO = PREÇOS[0]*QUANTIDADE
        
       
    c.execute(f'''UPDATE produtos SET faturamento = faturamento + {float(PREÇO)} WHERE id = {PRODUTO}''')
    
    print('','-'*30)
    
    
    
    
    
    print(f' Preço {PREÇO} R$')
    
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
    
    PAINEL()
            



def opção5():
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
        PAINEL()
            
        conexão.commit()          