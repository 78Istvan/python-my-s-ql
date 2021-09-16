import os
import datetime
import pymysql

username = os.getenv('C9_USER')
connection = pymysql.connect(host='localhost',
                           user = username,
                           password = '',
                           db = 'Chinook')


try:
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s where name = %s;",
                        rows)
                            
        connection.commit()
finally:
    connection.close()