import mysql.connector
connection = mysql.connector.connect(host='remotemysql.com',
                                         database='3sRxPqRiLy',
                                         user='3sRxPqRiLy',
                                         password='dhpwyt9ufA', port=3306)
insertQuery="INSERT INTO informations (name,surname1,surname2,dni)"
for index,row in df.iterrows():
            insertQuery1=insertQuery+"VALUES('{0}','{1}','{2}','{3}')".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]))
            cursor = connection.cursor()
            result = cursor.execute(insertQuery1)
            connection.commit()