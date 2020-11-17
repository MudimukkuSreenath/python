import pyodbc
con=pyodbc.connect('Driver={SQL server};Server=DESKTOP-T66VEKU\SREENATHSQL;Database=master;')
cursor=con.cursor()
cursor.execute("insert into employee values(3,'sm'),(4,'hj')")
print("table  succesfully")

