import mysql.connector
dataBase = mysql.connector.connect(
    host= 'localhost',
    user='root',
    passwd='qwe12rty'

)

cursorObject = dataBase.cursor()


cursorObject.execute('CREATE DATABASE IF NOT EXISTS ritikdb')
print("All Done")