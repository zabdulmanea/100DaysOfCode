# Python MySQL - PART 3
import mysql.connector

# Connecting to "mydatabase".
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234abcd1234",
    database="mydatabase"
)
mycursor = mydb.cursor()
print("'mydatabase' is connected!")
print("--------------------------")

# 1. Sort the Result:  ORDER BY
# Q: Sort the result alphabetically by name.
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("Customers ordered by name:")
for x in myresult:
    print(x)
print("--------------------------")

# Q: Sort the result reverse alphabetically by name.
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("Customers ordered desc by name:")
for x in myresult:
    print(x)
print("--------------------------")

# 2. Delete Record
sql = "DELETE FROM customers WHERE address = 'Blue Village'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted!")
print("--------------------------")

# 3. Delete a Table
# Q: Delete the table "customers".
sql = "DROP TABLE customers"
mycursor.execute(sql)
print("Customers table deleted!")
print("--------------------------")

# Q: Delete the table "customers" if it exists.
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
print("--------------------------")

mycursor.close()
mydb.close()
