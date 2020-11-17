import pyodbc
conn=pyodbc.connect('Driver={SQL server};Server=DESKTOP-T66VEKU\SREENATHSQL;Database=master;')
cursor=conn.cursor()
cursor.execute("select * from dbo.emp")
while 1:
    row=cursor.fetchone()
    if not row:
        break
    print(row .ename)
cursor.execute("select * from dbo.emp")
for row in cursor:

    print('row=%r' %(row,))
cursor.execute("update emp SET ename='NTR' WHERE ename='praveen'")
conn.commit()
conn.close()
