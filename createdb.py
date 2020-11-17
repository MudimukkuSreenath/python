import pyodbc
con = pyodbc.connect('Driver={SQL server};Server=DESKTOP-T66VEKU\SREENATHSQL;Database=master;')
cursor = con.cursor()
cursor.execute("insert into employee values(1,'sreenath'),(2,'praveen'),(3,'venkat')")
cursor.close()
con.close()

