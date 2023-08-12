from pandas import read_sql
from os import system
import sqlite3 as SQL
import manage
import re

def opção2():
    system('clear')

    with SQL.connect('datebase.db') as conn:
        c = conn.cursor()

    try:
        print('{:>37}'.format('PAINEL FORGES'))
        print('-'*70)
        relatorio = read_sql('SELECT * FROM produtos', conn)
        
        mDP = int(relatorio['preço'].sum() / len(relatorio['preço']))
        qDE = relatorio['estoque'].sum()
        F = relatorio['faturamento'].sum()
        
        print(relatorio, '\n')
        
        opção = int(input('         | [1] PESQUISAR | [2] REMOVER | [3] SAIR |'))
        
        if opção == 1:
            print('-'*70)
            pesquisar = str(input('NOME DO PRODUTO: '))
            resposta =  read_sql(f'''SELECT * FROM produtos WHERE produto LIKE "{pesquisar}%" ''', conn)
            print(resposta)
            
        elif opção == 2:
            print('-'*70)
            
            itemApagar = int(input('ID DO PRODUTO: '))

            consulta =  c.execute('SELECT id FROM produtos')

            if itemApagar in consulta.fetchone():
                system('clear')
                
                print('-'*70)
                print(read_sql(f'SELECT * FROM produtos WHERE id = {itemApagar}', conn))
                
                print('-'*70)
                apagar = str(input(f'DESEJA REALMENTE APAGAR O ID {itemApagar} [S/N]? '))
                
                if apagar == 'S':
                
                    c.execute(f'''DELETE  FROM produtos WHERE id = {itemApagar} ''')
                              
                    conn.commit()
                 
                    system('clear')
                         
                    opção2()
                
                else:
                    
                    opção2()
                    manage.PAINEL()
            else:
                
                system('clear')
                print('-'*70)
                print('{:>40}'.format('ID NÃO EXISTENTE'))
            
        elif opção == 3:
            system('clear')
            manage.PAINEL()
        
        
        
        print('-'*70)
        input('\n\n[ENTER]')
        system('clear')
        opção2()
    
    except:
        print('{:>42}'.format('Nenhum produto cadastrado.'))
        input('\n\n[PRESS ENTER]')
        system('clear')

    conn.commit()
    manage.PAINEL()

if __name__ == '__main__':
    opção2()