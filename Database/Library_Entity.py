import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database="Library_System",
)

cursorObject = dataBase.cursor()

# # User Table

userTable = """CREATE TABLE user(user_id INT PRIMARY KEY,
user_name VARCHAR(50) NOT NULL,
user_mobile INTEGER(15) NOT NULL,
user_email VARCHAR(30) NOT NULL,
user_address VARCHAR(50) NOT NULL,
user_password VARCHAR(50) NOT NULL)"""

cursorObject.execute(userTable)

# # Book Table

bookTable = """CREATE TABLE book(book_id INT PRIMARY KEY AUTO_INCREMENT,
book_name VARCHAR(50) NOT NULL,
author VARCHAR(30) NOT NULL,
availability_status BOOLEAN NOT NULL,
quantity INT NOT NULL)"""

cursorObject.execute(bookTable)

# Transaction Table

transTbl = """CREATE TABLE transaction(trans_id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
book_id INT,
issue_date DATE NOT NULL,
return_date DATE NOT NULL,
FOREIGN KEY (user_id) REFERENCES user(user_id),
FOREIGN KEY (book_id) REFERENCES book(book_id))"""

cursorObject.execute(transTbl)

# Admin Table

adminTable = """CREATE TABLE admin(admin_id INT PRIMARY KEY AUTO_INCREMENT,
admin_name VARCHAR(40),
admin_email VARCHAR(30),
admin_password VARCHAR(40))"""

cursorObject.execute(adminTable)


book_borrow_request = """create table book_borrow_request(req_id INT NOT NULL AUTO_INCREMENT,user_id INT NOT NULL,book_id INT NOT NULL,req_status BOOLEAN,
FOREIGN KEY (user_id) REFERENCES user(user_id),
FOREIGN KEY (book_id) REFERENCES book(book_id)) """

cursorObject.execute(book_borrow_request)

print("Table created successfully")
dataBase.close()