import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Diamonds2',
    
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE 1projectdb")

print("ALL Done!")