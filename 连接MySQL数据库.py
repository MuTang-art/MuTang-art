import pymysql

conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='landscape', charset='utf8')
cursor = conn.cursor()

sql = 'select * from '

cursor.execute(sql)
# row = cursor.fetchall()
conn.commit()
cursor.close()
conn.close()







