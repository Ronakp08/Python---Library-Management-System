import mysql.connector

def delete_book(book_id):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )

    cursorObject = dataBase.cursor()

    sql = "DELETE FROM book WHERE book_id=%s"
    val = (book_id,)

    cursorObject.execute(sql, val)
    dataBase.commit()

    if cursorObject.rowcount > 0:
        print(f"Book deleted successfully.")
    else:
        print("No Book found with the given ID.")

    cursorObject.close()
    dataBase.close()


book_id = int(input("Enter Book ID to delete: "))

delete_book(book_id)
