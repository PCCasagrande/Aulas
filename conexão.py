import firebirdsql 
import pandas as pd
con = firebirdsql.connect(user="SYSDBA",password="masterkey",database= "C:/puma/dados/puma.fdb", host= "192.168.1.99", charset="ANSI")
cur=con.cursor()
tabela = pd.read_sql("select * from GFILIAL",con)
print(tabela)

#cur.execute("select * from gfilial")
#for c in cur.fetchall():
    #print(c)
#con.close
    
 