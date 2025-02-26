import mysql.connector

def view_transaction(user_id):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )
    
    cursorObject = dataBase.cursor()

    sql = """SELECT b.book_name, t.issue_date, t.return_date, t.penalty_amount
             FROM transaction t 
             JOIN book b ON t.book_id = b.book_id
             WHERE t.user_id = %s;
          """
    
    val = (user_id,)  

    cursorObject.execute(sql, val)
    result = cursorObject.fetchall()

    if result:
        print("Here are your transactions:")
        for row in result:
            print(f"Book: {row[0]}, Issue Date: {row[1]}, Return Date: {row[2]}, Penalty: {row[3]}")
    else:
        print("No transactions found.")

    cursorObject.close()
    dataBase.close()


user_id = int(input("Enter User ID: "))
view_transaction(user_id)
