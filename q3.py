import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',password ='shanthan@123',database='inventory_management')
cur= mydb.cursor()
--Display all the “wooden chair” items that were manufactured before the 1st May 2023.
display='SELECT * FROM MANUFACTURE WHERE PRODUCT_NAME="WOODEN CHAIR" AND MANUFACTURE_DATE < "2023-05-01"';
cur.execute(display);
display1=cur.fetchall()
for i in display1:
    print(i)
