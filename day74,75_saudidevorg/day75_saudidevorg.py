"""
Week 11 : Challenge 2 (MySQL database)
"""

import mysql.connector

# 1. Create a Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234abcd1234"
)
mycursor = mydb.cursor()

# 2. Create a Database named (MyEmployee)
mycursor.execute("CREATE DATABASE MyEmployee")
print("MyEmployee has been created!")
print("--------------------------------------------")
mycursor.close()
mydb.close()

# 3. Connect to the database "MyEmployee".
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234abcd1234",
    database="MyEmployee"
)
mycursor = mydb.cursor()
print("'MyEmployee' is connected!")
print("--------------------------------------------")

# 4. Create a table named "Employee"
mycursor.execute(
    "CREATE TABLE employee ( \
        id INT AUTO_INCREMENT PRIMARY KEY, \
        firstName VARCHAR(255), \
        lastName VARCHAR(255), \
        age INT, \
        gender VARCHAR(255), \
        salary INT)")
print("Table 'employee' has been created!")
print("--------------------------------------------")

# 5. Insert Into Table
sql = "INSERT INTO employee \
    (firstName, lastName, age, gender, salary) \
    VALUES (%s, %s, %s, %s, %s)"
val = [
    ('Ahmed', 'Ali', 30, 'Male', 10000),
    ('Khalid', 'Muhammad', 34, 'Male', 7000),
    ('Nora', 'Saleh', 29, 'Female', 7000)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted!")
print("--------------------------------------------")

# ---------- Answer 1 -----------------
# 6. Display the records of employee table
mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------------------------")

# ---------- Answer 2 -----------------
# 7. Display first name, gender and salary of employee table
mycursor.execute("SELECT firstName, gender, salary FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------------------------")

# ---------- Answer 3 -----------------
# 8. Display the records of employee table Descending
mycursor.execute("SELECT * FROM employee ORDER BY firstName DESC")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------------------------")

# ---------- Answer 4 -----------------
# 9. Delete the row contains age=34 then display the table
sql = "DELETE FROM employee WHERE age = 34"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted!")
print("--------------------------------------------")

mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------------------------")

mycursor.close()
mydb.close()
