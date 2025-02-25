import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Library_system"
)

cursorObject = dataBase.cursor()

# Book Borrow by user

val = [(2,4,'2025-02-15'),
       (3,1,'2005-05-25'),
       (5,6,'2024-02-14'),
       (6,8,'2023-10-31')]

cursorObject.executemany("INSERT INTO transaction (user_id, book_id, issue_date) VALUES (%s, %s, %s)",val)
dataBase.commit()

print("Book assigned to user....")
dataBase.close()