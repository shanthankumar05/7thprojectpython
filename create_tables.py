# create tables

# goods
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',password ='shanthan@123',database='inventory_management')
cur= mydb.cursor()cur = mydb.cursor()
cd= 'CREATE TABLE GOODS(GOODS_ID INT NOT NULL, NUMBER_ITEMS INT NOT NULL, MANUFACTURE_DATE DATE NOT NULL, PRODUCT_NAME VARCHAR(20) NOT NULL,COLOR VARCHAR(20) NOT NULL, PRIMARY KEY(PRODUCT_NAME, COLOR), FOREIGN KEY(MANUFACTURE_DATE) REFERENCES MANUFACTURE(MANUFACTURE_DATE) ON DELETE CASCADE)'
cur.execute(cd)


# manufacture

import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',password ='shanthan@123',database='inventory_management')
cur= mydb.cursor()
ct = 'CREATE TABLE MANUFACTURE(MANUFACTURE_ID INT NOT NULL,MANUFACTURE_COMPANY VARCHAR(20),DEFECTIVE BIT NOT NULL,NUMBER_ITEMS INT NOT NULL,MANUFACTURE_DATE DATE PRIMARY KEY NOT NULL,PRODUCT_NAME VARCHAR(20) NOT NULL,COLOR VARCHAR(10) NOT NULL)'
cur.execute(ct)

# purchase

import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',password ='shanthan@123',database='inventory_management')
cur= mydb.cursor()
d1 = 'CREATE TABLE PURCHASE(PURCHASE_ID INT PRIMARY KEY NOT NULL,STORE_MODE VARCHAR(40) NOT NULL,PRODUCT_NAME VARCHAR(20) NOT NULL,COLOR VARCHAR(10) NOT NULL,NUMBER_ITEMS INT NOT NULL,PURCHASE_DATE DATE NOT NULL,PURCHASE_AMOUNT FLOAT NOT NULL);'
cur.execute(d1)

# sales

import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',password ='shanthan@123',database='inventory_management')
cur= mydb.cursor()
st = 'CREATE TABLE SALE(SALE_ID INT PRIMARY KEY NOT NULL,STORE_NAME VARCHAR(40) NOT NULL,SALE_DATE DATE NOT NULL,COLOR VARCHAR(10) NOT NULL,NUMBER_ITEMS INT NOT NULL,PRODUCT_NAME VARCHAR(20) NOT NULL,SALE_AMOUNT FLOAT NOT NULL,PROFIT_MARGIN FLOAT,FOREIGN KEY(PRODUCT_NAME, COLOR) REFERENCES GOODS(PRODUCT_NAME, COLOR) ON DELETE CASCADE)'
cur.execute(st)
