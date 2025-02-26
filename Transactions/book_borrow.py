import mysql.connector
from datetime import datetime, timedelta

def book_borrow(user_id, book_id, issue_date):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )
    
    cursorObject = dataBase.cursor()
    return_date = (datetime.strptime(issue_date, "%Y-%m-%d") + timedelta(days=15)).strftime("%Y-%m-%d")

    sql = """INSERT INTO transaction(user_id, book_id, issue_date, return_date) 
             VALUES (%s, %s, %s, %s)"""
    val = (user_id, book_id, issue_date, return_date)

    cursorObject.execute(sql, val)
    dataBase.commit()

    print("Book issued to user....")

    cursorObject.close()
    dataBase.close()


user_id = int(input("Enter user ID: "))
book_id = int(input("Enter book ID: "))
issue_date = input("Enter issue date (YYYY-MM-DD): ") 

book_borrow(user_id, book_id, issue_date)
