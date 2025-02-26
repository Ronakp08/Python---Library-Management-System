import mysql.connector

def view_book():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )
    
    cursorObject = dataBase.cursor()
    
    sql = "SELECT * FROM book"
    cursorObject.execute(sql)
    
    results = cursorObject.fetchall()
    
    if results:
        print("Book Inventory..")
        for row in results:
            print(row)
    else:
        print("No Record found....")
        
    cursorObject.close()
    dataBase.close()
    
view_book()
