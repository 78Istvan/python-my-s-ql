import os
import datetime
import pymysql

username = os.getenv('C9_USER')
connection = pymysql.connect(host='localhost',
                           user = username,
                           password= '',
                           db = 'Chinook')
try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    connection.close()


try:
    with connection.cursor() as cursor:
        cursor.execute("""Create table if not exists
                            Friends(name char(20), age int, DOB datetime);""")
finally:
    connection.close()