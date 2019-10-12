#Set-up
import mysql.connector

#Connection
connection = mysql.connector.connect(host='remotemysql.com',
                                         database='3sRxPqRiLy',
                                         user='3sRxPqRiLy',
                                         password='dhpwyt9ufA', port=3306)
insertquery="INSERT INTO test2 (Name,Age) VALUES('Abraham',12)"
cursor = connection.cursor()
result = cursor.execute(insertquery)
connection.commit()

