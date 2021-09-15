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
        cursor.execute("Friends (name char(20), age int, DOB datetime)")
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    connection.close()