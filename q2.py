import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',password ='shanthan@123',database='inventory_management')
cur= mydb.cursor()
#Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
update='UPDATE MANUFACTURE SET NUMBER_ITEMS=10 WHERE PRODUCT_NAME="TOY CAR" AND COLOR="RED"';
cur.execute(update);
print("Updated ")
