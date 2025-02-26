import mysql.connector

def user_book_borrow(user_id,book_id):
    dataBase=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )
    
    cursorObject = dataBase.cursor()
    
    sql = """INSERT INTO book_borrow_request(user_id,book_id) VALUES(%s,%s)"""
    val = (user_id,book_id)
    
    cursorObject.execute(sql,val)
    dataBase.commit()
    
    print("Borrow request sent to librarian..")
    
    cursorObject.close()
    dataBase.close()
    
user_id = input("Enter user id: ")
book_id = input("Enter book id: ")

user_book_borrow(user_id,book_id)