import mysql.connector

def return_book(trans_id, return_date):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )

    cursorObject = dataBase.cursor()

    sql_update = "UPDATE transaction SET return_date = %s WHERE trans_id = %s"
    cursorObject.execute(sql_update, (return_date, trans_id))

    dataBase.commit()
    
    if cursorObject.rowcount > 0:
        print("Book returned successfully")
    else:
        print("No transactions found for the given User ID.")

    cursorObject.close()
    dataBase.close()


trans_id = input("Enter User ID: ")
return_date = input("Enter Return Date (YYYY-MM-DD): ")

return_book(trans_id, return_date)
