import mysql.connector

def delete_book(book_id):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )

    cursorObject = dataBase.cursor()

    sql = "DELETE FROM book WHERE book_id = %s"
    val = (book_id,)  

    cursorObject.execute(sql, val)
    dataBase.commit()

    if cursorObject.rowcount > 0:
        print("Book removed from inventory....")
    else:
        print("enter valid book id.....")

    cursorObject.close()
    dataBase.close()


book_id = int(input("Enter book ID: "))
delete_book(book_id)
