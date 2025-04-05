import mysql.connector

def get_connector():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "sakila",
        port = 3306
    )
    return conn
