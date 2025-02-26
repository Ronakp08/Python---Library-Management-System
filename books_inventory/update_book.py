import mysql.connector

def update_book(book_name, author, availability_status, quantity, book_id):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )
    
    cursorObject = dataBase.cursor()
    
    sql = "UPDATE book SET book_name=%s, author=%s, availability_status=%s, quantity=%s WHERE book_id=%s"
    val = (book_name, author, availability_status, quantity, book_id) 
    
    cursorObject.execute(sql, val) 
    dataBase.commit()
    
    if cursorObject.rowcount > 0:
        print(f"Book with ID {book_id} updated successfully....")
    else:
        print(f"No book found enter correct id..")

    cursorObject.close()
    dataBase.close()
    
book_id = int(input("Enter Book ID: "))  
book_name = input("Enter Book Name: ")
author = input("Enter Author Name: ")
availability_status = int(input("Enter availability status (1 for Yes, 0 for No): ")) 
quantity = int(input("Enter Quantity: "))  

update_book(book_name, author, availability_status, quantity, book_id)
