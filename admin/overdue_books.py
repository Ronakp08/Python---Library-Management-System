import mysql.connector
from datetime import date

def view_overdue():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )

    cursorObject = dataBase.cursor()

    sql = """
        SELECT t.trans_id, u.user_name, b.book_name, t.issue_date, t.return_date, t.penalty_amount
        FROM transaction t
        JOIN user u ON t.user_id = u.user_id
        JOIN book b ON t.book_id = b.book_id
        WHERE t.return_date < CURDATE()
    """

    cursorObject.execute(sql)
    result = cursorObject.fetchall()

    if result:
        print("Overdue transactions found:")
        for row in result:
            print(row)
    else:
        print("No overdue transactions found.")


    cursorObject.close()
    dataBase.close()

view_overdue()
