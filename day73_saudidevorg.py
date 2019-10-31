# Python MySQL - PART 4
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


# 1. Update Table
# Q: Overwrite the address column from "Central st 954" to "Canyoun 123"
sql = "UPDATE customers SET address = 'Canyoun 123' WHERE address = 'Central st 954'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) updated!")
print("--------------------------")

# 2. Limit the Result | LIMIT
# Q: Select the 5 first records in the "customers" table
mycursor.execute("SELECT * FROM customers LIMIT 5")
print("The first five customers are:")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------")

# 3. Start From Another Position | OFFSET
# Q: Start from position 3, and return 5 records
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
print("The five customers are:")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------")


# 4. Join Two or More Tables | JOIN or INNER JOIN
# Q: Join users and products to see the name of the users favorite product.
sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users INNER JOIN products \
    ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------")

# 5. LEFT JOIN
# Q: Select all users and their favorite product.
sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users LEFT JOIN products \
    ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------")

# 6. RIGHT JOIN
# Q: Select all products, and the user(s) who have them as their favourite.
sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users RIGHT JOIN products \
    ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("--------------------------")

mycursor.close()
mydb.close()
