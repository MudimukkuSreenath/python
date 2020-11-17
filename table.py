import pyodbc
try:
    
    conn=pyodbc.connect('Driver={SQL server};Server=DESKTOP-T66VEKU\SREENATHSQL;Database=master;')
    cursor=conn.cursor()
    cursor.execute("create table book(bno smallint,bname varchar(20),bprice smallmoney)")
    print("table created successfully")
except pydobc.DatabaseError as e:
    if conn:
        conn.rollback()
        print("there is a problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        
                       
