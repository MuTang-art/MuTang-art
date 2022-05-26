import psycopg2
import xlrd
import csv

conn = psycopg2.connect(database='odoo14', user='odoo', password='odoo!321', host='172.16.1.108', port=5432)
cur = conn.cursor()
# cur = conn.cursor()
# cur.execute('select * from prod_type')
# rows = cur.fetchall()


# python读取excel文件
data = xlrd.open_workbook(r'D:/1234312.xlsx')
table = data.sheets()[0]
num = 0
abc = []
# 从第二行开始读
for i in range(1, table.nrows):
    dic = {
        "type": table.cell_value(i, 0),
        "parent": table.cell_value(i, 1),
        'prod_name': table.cell_value(i, 2),
    }
    if dic["prod_name"]:
        sql = f''' '''
        cur.execute(sql)
        row = cur.fetchall()
        if len(row) == 0:
            # 写入csv文件
            with open('product.csv', 'a') as f:
                csv.writer(f).writerow(dic.values())
            num +=1
print(abc)
print(num)
