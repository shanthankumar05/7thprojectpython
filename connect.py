--create database
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="shanthan@123")
cur = mydb.cursor()
cur.execute("create database inventory_management")
