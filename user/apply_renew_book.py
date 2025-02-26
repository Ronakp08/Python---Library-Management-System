import mysql.connector
from datetime import datetime, timedelta

def renew_book(trans_id, book_id):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )
    
    cursorObject = dataBase.cursor()

    sql_fetch = "SELECT return_date FROM transaction WHERE trans_id = %s AND book_id = %s"
    cursorObject.execute(sql_fetch, (trans_id, book_id))
    result = cursorObject.fetchone()

    if result and result[0]:
        current_return_date = result[0]
        if isinstance(current_return_date, str):
            current_return_date = datetime.strptime(current_return_date, "%Y-%m-%d")

        new_return_date = (current_return_date + timedelta(days=15)).strftime("%Y-%m-%d")

        sql_update = "UPDATE transaction SET return_date=%s WHERE trans_id=%s AND book_id=%s"
        cursorObject.execute(sql_update, (new_return_date, trans_id, book_id))
        dataBase.commit()

        print(f"Book renewed successfully! New return date: {new_return_date}")
    else:
        print("No transaction found or return date is NULL.")

    cursorObject.close()
    dataBase.close()


trans_id = int(input("Enter Transaction ID: "))
book_id = int(input("Enter Book ID: "))
renew_book(trans_id, book_id)
