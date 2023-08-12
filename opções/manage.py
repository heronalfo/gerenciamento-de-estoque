import model

def PAINEL():
    from os import system 
    import opção1
    import opção2
    import opção3
    import opção4
        
    print(
'',
'-'*30,
'\n{:>21}\n'.format('PAINEL FORGES'),
'-'*30,
'\n [1] CADASTRAR PRODUTOS › \n','-'*30,
'\n [2] PRODUTOS › \n','-'*30,
'\n [3] CAIXA › \n', '-'*30,
'\n [4] EDITAR PRODUTO › \n','-'*30,
'\n [5] RELATORIO DE VENDAS › \n', '-'*30    )
    
    opção = int(input(' OPÇÃO >>> '))
    
    if opção == 1:
        opção1.opção1()
    
    if opção == 2:
        opção2.opção2()
      
            
    elif opção == 3:
         opção3.opção3()
        
    elif opção == 4:
        opção4.opção4()
        
    else:
        system('clear')
        print('\033[31m  Opçãoinvalida!\033[m')
        
        PAINEL()
        
        

if __name__ == '__main__':
	PAINEL()