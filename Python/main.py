import pyodbc
import pandas as pd
server = 'tcp:sp2020.database.windows.net'
database = 'SP2020'
username = 'se2sql'
password = 'SoftwareEngineering2'

#Gets full rows of candidates
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM dbo.cands")

# cursor.execute("SELECT Party, count(Party) AS CountOf FROM dbo.cands GROUP BY Party HAVING count(Party) >3")

#Testing connecting twice to same server
cnxn2 = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor2 = cnxn2.cursor()
cursor2.execute("SELECT count(Party) AS CountOf FROM dbo.cands GROUP BY Party HAVING count(Party) >3")

row = cursor.fetchone()
row2 = cursor2.fetchone()
for row in cursor:
    print(row)

for row2 in cursor2:
    print(row2)