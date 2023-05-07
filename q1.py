import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',password ='shanthan@123',database='inventory_management')
cur= mydb.cursor()
--Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-04-23’.
delete='DELETE FROM MANUFACTURE WHERE DEFECTIVE=1';
cur.execute(delete);
print("Deleted Done")
