#This program demonstrate the databse connectivity.

import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="root", passwd="sa1234",database="demo")
mycur=mydb.cursor()
#mycur.execute('show databases')
#mycur.execute('select * from student')
mycur.execute('select * from student')
#result=mycur.fetchall()
result=mycur.fetchone()
for i in result:
    print(i)