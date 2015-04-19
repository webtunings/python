import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='pk', db='test')
cursor = conn.cursor()

cursor.execute("SHOW DATABASES")

print(cursor.description)

for row in cursor:
 print(row)

cursor.close()
conn.close()

