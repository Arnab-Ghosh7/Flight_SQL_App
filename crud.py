import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Your Password',
        database = 'indigo'             # make sure this database exists
    )

    if conn.is_connected():
        print('Connection established')
        mycursor = conn.cursor()
        # You can now run your own SQL queries here

except Error as e:
    print(f'Connection error: {e}')

# create a database on the db server
# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()

# create a table
# airport -> airport_id | code | name | City
# mycursor.execute("""
#CREATE TABLE airport(
    #airport_id INTEGER PRIMARY KEY,
    #code VARCHAR(10) NOT NULL,
    #city VARCHAR(50) NOT NULL,
    #name VARCHAR(255) NOT NULL
#)
#""")
#conn.commit()

# Insert data to the table
#mycursor.execute("""
    #INSERT INTO airport VALUES
    #(1,'DEL','New Delhi','IGIA'),
    #(2,'CCU','Kolkata','NSCA'),
    #(3,'BOM','Mumbai','CSMA')
#""")
#conn.commit()

# Search/Retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

# Update
mycursor.execute("""
UPDATE airport
SET name = 'Bombay'
WHERE airport_id = 3
""")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

# DELETE
mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)


