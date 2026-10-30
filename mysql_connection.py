
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="manufacturing_analytics"
)

if connection.is_connected():
    print("MySQL Connected Successfully!")

connection.close()
