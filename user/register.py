import mysql.connector

def user_register(user_name,user_mobile,user_email,user_address,user_password):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Library_system"
    )
    
    cursorObject = dataBase.cursor()
    
    sql = """INSERT INTO user(user_name,user_mobile,user_email,user_address,user_password)
             VALUES(%s,%s,%s,%s,%s)"""
    val = (user_name,user_mobile,user_email,user_address,user_password)
    
    cursorObject.execute(sql,val)
    dataBase.commit()
    
    if cursorObject.rowcount > 0:
        print("Registration successfully....")
    else:
        print("Registration failed...")
    
    cursorObject.close()
    dataBase.close()
    
user_name = input("Enter your name: ")
user_mobile = int(input("Enter mobile number: "))
user_email = input("Enter email id: ")
user_address = input("Enter your address")
user_password = input("Enter password")

user_register(user_name,user_mobile,user_email,user_address,user_password)