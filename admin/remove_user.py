import mysql.connector

def delete_user(user_id):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )

    cursorObject = dataBase.cursor()

    sql = "DELETE FROM user WHERE user_id=%s"
    val = (user_id,)

    cursorObject.execute(sql, val)
    dataBase.commit()

    if cursorObject.rowcount > 0:
        print(f"User deleted successfully.")
    else:
        print("No user found with the given ID.")

    cursorObject.close()
    dataBase.close()


user_id = int(input("Enter User ID to delete: "))

delete_user(user_id)
