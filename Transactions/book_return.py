import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Library_system"
)

cursorObject = dataBase.cursor()

# Book return by user

update1 = "UPDATE transaction SET return_date = '2025-02-28' WHERE user_id = '1'"
cursorObject.execute(update1)

dataBase.commit()

print("Book Returned....")
dataBase.close()