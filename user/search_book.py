import mysql.connector

def search_book(book_name):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )
    
    cursorObject = dataBase.cursor()
    
    sql = "SELECT * FROM book WHERE book_name LIKE %s"
    val = (f"%{book_name}%",)
    cursorObject.execute(sql, val)
    
    results = cursorObject.fetchall()
    
    if results:
        print("Search results.....")
        for row in results:
            print(row)
    else:
        print("Book is not found....")
        
    cursorObject.close()
    dataBase.close()
    
book_name = input("Enter book name: ")
search_book(book_name)
