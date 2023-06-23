# 用 connect() 函數建立跟資料庫檔案聯繫的 Connection 物件。
# 由 Connection 物件的 cursor() 方法建立 Cursor 物件。
# 利用 Cursor 物件的 execute() 方法進行資料庫操作。
# 利用 Connection 物件的 commit() 方法做資料庫檔案更新。
# 利用 Connection 物件的 close() 方法做關閉跟資料庫檔案的聯繫。
# 參考鏈接
# https://youtu.be/bgFuVih778w?t=132

import sqlite3
import os
path = os.path.split(os.path.realpath(__file__))[0]+'/'


# 創建table
def create_table(table_name):
    return cur.execute(
        f'''CREATE TABLE "{str(table_name)}" (
            "id"	INTEGER NOT NULL,
            "name"	TEXT,
            "dayman"	TEXT,
            PRIMARY KEY("id"));
            ''')


# 插入資料庫
def insert_data(cur, date, name):
    # 先查詢該表最大id 插入的下一個要+1
    res = cur.execute(
        'SELECT MAX(CAST("id" AS INTEGER)) FROM "main"."line_table";')
    for i in res.fetchall()[0]:
        id = i+1

    print(id)
    # 插入資料
    return cur.execute(f"INSERT INTO line_table VALUES ('{id}','{str(date)}','{str(name)}')")


# 資料庫連接
con = sqlite3.connect(path+"database.db")
# 建立 Cursor 物件
cur = con.cursor()
# 進行資料庫操作
# cur.execute("CREATE TABLE movie(title, year, score)")
# 創建table
# cur.execute("CREATE TABLE contacts (date text, name text, number text)")
# res = cur.execute("SELECT name FROM sqlite_master")
# 插入欄位
# cur.execute("INSERT INTO contacts VALUES ('2018-03-11','王小寶','222')")
# cur.execute("INSERT INTO contacts VALUES ('2018-03-12','吳有明','321')")
# cur.execute(f"INSERT INTO line_table VALUES ('{res}','2/30','派大興')")
insert_data(cur, 11/5, '小小')
# table_name = '天好運'
# create_table(table_name)
res = cur.execute('SELECT * FROM line_table;')
# for row in cur.execute('SELECT * FROM contacts ORDER BY name'):
#     print(row)
print(res.fetchall())
# con.commit()
# con.close()
