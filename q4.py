import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',password ='shanthan@123',database='inventory_management')
cur= mydb.cursor()
--Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.
stat='SELECT S.PROFIT_MARGIN FROM MANUFACTURE M,SALE S WHERE M.MANUFACTURE_COMPANY="SS EXPORT" AND M.PRODUCT_NAME="WOODEN TABLE" AND S.STORE_NAME="MY CARE"';
stat=cur.execute(stat);
each=cur.fetchall()
print("values are:");
for k in each:
    print(k);
