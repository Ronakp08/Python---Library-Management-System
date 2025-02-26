import mysql.connector

def approve_borrow(req_id):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )

    cursorObject = dataBase.cursor()

    sql = "UPDATE book_borrow_request SET req_status = 1 WHERE req_id = %s"
    val = (req_id,)

    cursorObject.execute(sql, val)
    dataBase.commit()

    if cursorObject.rowcount > 0:
        print(f"Borrow request approved successfully.")
    else:
        print("No request found. Please enter a valid request ID.")

    cursorObject.close()
    dataBase.close()

req_id = int(input("Enter request ID: "))


approve_borrow(req_id)
