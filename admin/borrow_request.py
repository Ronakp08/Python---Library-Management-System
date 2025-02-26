import mysql.connector

def view_borrow_request():
    dataBase=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )
    
    cursorObject = dataBase.cursor()
    
    sql = "SELECT * FROM book_borrow_request WHERE req_status='0'"
    
    cursorObject.execute(sql)
    
    result = cursorObject.fetchall()
    
    if result:
        print("pending Requests..")
        for row in result:
            print(row)
    else:
        print("No Record found....")
        
    cursorObject.close()
    dataBase.close()

view_borrow_request()