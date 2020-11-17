import pyodbc
con = pyodbc.connect('Driver={SQL server};Server=DESKTOP-T66VEKU\SREENATHSQL;Database=sreenath;')
cursor = con.cursor()
cursor.execute("select * from EMP")
for row in cursor:
    print(row)




