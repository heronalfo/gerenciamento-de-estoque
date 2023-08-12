import sqlite3 as SQL
from pandas import read_sql

conexão = SQL.connection('datebase.db')
c = conexão.cursor()

class dbaseModel():

    def pegar(consulta: str):
       
        response = read_sql(consulta)

    def adiconar(consulta: str):

         c.execute(consulta)
    
    
    