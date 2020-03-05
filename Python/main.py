import pyodbc
server = 'tcp:sp2020.database.windows.net'
database = 'SP2020'
username = 'se2sql'
password = 'SoftwareEngineering2'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM dbo.cands")
# cursor.execute("SELECT Party, count(Party) AS CountOf FROM dbo.cands GROUP BY Party HAVING count(Party) >3")
# cursor.execute("SELECT count(Party) AS CountOf FROM dbo.cands GROUP BY Party HAVING count(Party) >3")
row = cursor.fetchone()
for row in cursor:
    print(row)