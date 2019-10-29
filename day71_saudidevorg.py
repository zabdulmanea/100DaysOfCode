# Python MySQL - PART 2
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

# 0. Delete table rows
# sql = "DELETE FROM customers"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record was deleted!")

# 1. Insert Into Table
# Q: Insert a record in the "customers" table.
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted!")
print("--------------------------")

# 2. Insert Multiple Rows
# Q: Fill the "customers" table with data.
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Sandy', 'Ocean blvd 21'),
    ('Susan', 'One way 98'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Vicky', 'Yellow Garden 2'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted!")
print("--------------------------")

# 3. Get Inserted ID
# Q: Insert one row, and return the ID.
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted, ID:", mycursor.lastrowid)
print("--------------------------")

# 4. Select From a Table
# Q: Select all records from the "customers" table,
# and display the result.
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------")

# 5. Selecting Columns
# Q: Select only the name and address columns.
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------")

# 6. Using the fetchone() Method
# Q: Fetch only the first row.
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)
mycursor.reset()
print("--------------------------")


# 7. Select With a Filter 'WHERE'
# Q: Select record(s) where the address is "Park Lane 38".
sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------")

# 8. Wildcard Characters '%'
# Q: Select records where the address contains the word "way".
sql = "SELECT * FROM customers WHERE address like '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------")

mycursor.close()
mydb.close()
