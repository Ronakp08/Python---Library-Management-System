import mysql.connector

def view_transaction():
    dataBase=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )
    
    cursorObject = dataBase.cursor()
    
    sql = "SELECT * FROM transaction"
    
    cursorObject.execute(sql)
    
    result = cursorObject.fetchall()
    
    if result:
        print("transaction found..")
        for row in result:
            print(row)
    else:
        print("No Record found....")
        
    cursorObject.close()
    dataBase.close()

view_transaction()