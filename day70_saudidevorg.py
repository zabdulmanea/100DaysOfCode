# Python MySQL - PART 1

"""
MySQL Database:
1. Install MySQL Server: https://dev.mysql.com/downloads/mysql/
2. Install MySQL Workbench: https://dev.mysql.com/downloads/workbench/
MySQL Driver:
3. Install MySQL connector: pip install mysql-connector
                            pip install mysql-connector-python

"""

# 1. Test MySQL Connector
import mysql.connector

# 2. Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234abcd1234"
)
print(mydb)
print("----------------------------")

# 3. Creating a Database

# Q: create a database named "mydatabase".
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
print("mydatabase has been created!")
print("----------------------------")

# 4. Check if Database Exists

# Q: Return a list of your system's databases.
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
mydb.close()
print("----------------------------")

# Q: Try connecting to the database "mydatabase".
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234abcd1234",
    database="mydatabase"
)

# 5. Creating a Table

# Q: Create a table named "customers"
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
print("Table 'customers' has been created!")

# 6. Check if Table Exists

# Q: Return a list of your system's databases tables
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
print("----------------------------")

# 7. Primary Key

# Q: Create primary key when creating the table.
# mycursor.execute("CREATE TABLE customers 
# (id INT AUTO_INCREMENT PRIMARY KEY, 
# name VARCHAR(255), address VARCHAR(255))")
# print("Table 'customers' has been created!")

# Q: Create primary key on an existing table.
mycursor.execute(
    "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
print("'id' attribute has been added to table 'customers'")
print("----------------------------")
