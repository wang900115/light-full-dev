import sqlite3

# 連接到 SQLite 資料庫
conn = sqlite3.connect('my.sqlite3')  # 替換為您的資料庫文件路徑

# 創建一個 cursor 物件來執行 SQL 查詢
cursor = conn.cursor()

cursor.execute("SELECT * FROM ShowInfo")

# 提取所有表格名稱
tables = cursor.fetchall()

# 輸出所有表格名稱
for table in tables:
    print(table)  # 輸出表格名稱
