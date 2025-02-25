import mysql.connector

def add_new_book(book_name, author, availability_status, quantity):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )

    cursorObject = dataBase.cursor()

    sql = """INSERT INTO book (book_name, author, availability_status, quantity) 
             VALUES (%s, %s, %s, %s)"""
    val = (book_name, author, availability_status, quantity)

    cursorObject.execute(sql, val)
    dataBase.commit()

    print(f"Book '{book_name}' by {author} added to inventory. Quantity: {quantity}")

    cursorObject.close()
    dataBase.close()

book_name = input("Enter book name: ")
author = input("Enter author name: ")
availability_status = input("Is available? (1 for Yes, 0 for No): ")
quantity = int(input("Enter book quantity: "))


availability_status = bool(int(availability_status))

add_new_book(book_name, author, availability_status, quantity)
