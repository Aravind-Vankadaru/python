import mysql.connector
from mysql.connector import Error
import pandas as pd
try:
    connection = mysql.connector.connect(host='localhost',user='root',passwd='Aravind@018')
    print('successful')
except Error as err:
    print(f"Error: {err}")
cursor = connection.cursor()
cursor.execute("CREATE DATABASE videoes")
connection = mysql.connector.connect(host='localhost',user='root',passwd='Aravind@018',database="videoes")
cursor = connection.cursor()
data = """
insert into movie values
('inception','leanadro','angelia','christopher-nolan','2001-12-05'),
('bahubali','prabhas','anushka','rajamouli','2016-10-10'),
('bahubali2','prabhas','anushka','rajamouli','2018-05-05'),
('pushpa','aa','rashmika','sukumar','2020-11-07'),
('rrr','ram-ntr','aliabhatt','rajamouli','2022-08-15');
"""
cursor.execute(data)
connection.commit()
q = """Select * from movie;"""
cursor.execute(q)
result = cursor.fetchall()
print(result)
q2 = """select * from movie where actor='prabhas';"""
cursor.execute(q2)
result = cursor.fetchall()
print(result)
