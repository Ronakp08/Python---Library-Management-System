import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database="Library_System",
)

cursorObject = dataBase.cursor()



# Insert Data into User Table
user_data = [
    (1, "Amit Sharma", 9876543210, "amit@example.com", "Delhi, India", "Amit@123"),
    (2, "Riya Patel", 9876543211, "riya@example.com", "Mumbai, India", "Riya@123"),
    (3, "Sanjay Mehta", 9876543212, "sanjay@example.com", "Kolkata, India", "Sanjay@123"),
    (4, "Neha Verma", 9876543213, "neha@example.com", "Chennai, India", "Neha@123"),
    (5, "Rajesh Gupta", 9876543214, "rajesh@example.com", "Hyderabad, India", "Rajesh@123"),
    (6, "Pooja Iyer", 9876543215, "pooja@example.com", "Bangalore, India", "Pooja@123"),
    (7, "Vikram Singh", 9876543216, "vikram@example.com", "Jaipur, India", "Vikram@123"),
    (8, "Anjali Nair", 9876543217, "anjali@example.com", "Pune, India", "Anjali@123"),
    (9, "Arjun Reddy", 9876543218, "arjun@example.com", "Ahmedabad, India", "Arjun@123"),
    (10, "Kavita Das", 9876543219, "kavita@example.com", "Lucknow, India", "Kavita@123"),
]

cursorObject.executemany("INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s)", user_data)

# Insert Data into Book Table
book_data = [
    ("The White Tiger", "Aravind Adiga", True, 5),
    ("Midnight’s Children", "Salman Rushdie", True, 3),
    ("The Namesake", "Jhumpa Lahiri", True, 4),
    ("God of Small Things", "Arundhati Roy", False, 2),
    ("Train to Pakistan", "Khushwant Singh", True, 6),
    ("Interpreter of Maladies", "Jhumpa Lahiri", True, 4),
    ("The Palace of Illusions", "Chitra Banerjee Divakaruni", True, 3),
    ("Malgudi Days", "R.K. Narayan", True, 5),
    ("Gitanjali", "Rabindranath Tagore", True, 2),
    ("The Inheritance of Loss", "Kiran Desai", True, 3),
]

cursorObject.executemany("INSERT INTO book (book_name, author, availability_status, quantity) VALUES (%s, %s, %s, %s)", book_data)

# Insert Data into Admin Table
admin_data = ("AdminUser", "admin@example.com", "Admin@123")
cursorObject.execute("INSERT INTO admin (admin_name, admin_email, admin_password) VALUES (%s, %s, %s)", admin_data)

dataBase.commit()
cursorObject.close()

dataBase.close()

print("Data inserted successfully!")
