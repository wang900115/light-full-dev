import sqlite3
import json

# 連結database
def connect_db():
    return sqlite3.connect('my.sqlite3')
 

def main():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')
    # 建立表格
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Event (
                Version TEXT,                                  -- 發行版本
                UID PRIMARY KEY,                               -- 唯一辨識碼
                title TEXT,                                    -- 活動名稱
                category TEXT,                                 -- 活動種類
                descriptionFilterHtml TEXT,                    -- 簡介說明
                discountInfo TEXT,                             -- 折扣資訊
                imageURL TEXT,                                 -- 圖片連結
                webSales TEXT,                                 -- 售票網址
                sourceWebPromote TEXT,                         -- 推廣網址
                sourceWebName TEXT,                            -- 來源網站名稱
                hitRate INTEGER,                               -- 點閱數 
                comment TEXT,                                  -- 備註
                editModifyDate TEXT,                           -- 編輯時間
                startDate TEXT,                                -- 活動起始時間
                endDate TEXT                                 -- 活動結束時間
            );
            """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Unit (
                
                unit_id INTEGER PRIMARY KEY AUTOINCREMENT,     -- 單位ID，自動生成
                event_uid TEXT,                                -- 活動唯一識別碼
                unit_type TEXT,                                -- 單位類型
                unit_name TEXT,                                 -- 單位名稱
                FOREIGN KEY (event_uid) REFERENCES Event (UID) -- 設置外鍵，保證單位與活動資料的關聯
            );
            """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS ShowInfo ( 
                show_id INTEGER PRIMARY KEY AUTOINCREMENT,     -- 場次ID
                event_uid TEXT ,                               -- 活動唯一識別碼                  
                time TEXT,                                 -- 單場演出時間
                onSales TEXT,                                  -- 是否售票
                Price TEXT,                                    -- 售票說明
                location TEXT,                                 -- 地址
                locationName TEXT,                             -- 場地名稱
                latitude REAL,                                 -- 緯度
                longitude REAL,                                -- 經度
                endTime TEXT,                              -- 單場結束時間
                FOREIGN KEY (event_uid) REFERENCES Event (UID) -- 設置外鍵，保證活動與場次資料的關聯
            );
            """)
    
    with open('SearchShowAction.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

     # 插入資料
    for event_data in data:
        # 插入 Event 資料
        cursor.execute("""
        INSERT INTO Event (Version, UID, title, category, descriptionFilterHtml, discountInfo, imageURL, webSales, 
        sourceWebPromote, sourceWebName, hitRate, comment, editModifyDate, startDate, endDate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            event_data["version"], event_data["UID"], event_data["title"], event_data["category"], 
            event_data["descriptionFilterHtml"], event_data["discountInfo"], event_data["imageUrl"], event_data["webSales"],
            event_data["sourceWebPromote"], event_data["sourceWebName"], event_data["hitRate"], event_data["comment"],
            event_data["editModifyDate"], event_data["startDate"], event_data["endDate"]
        ))

        # 插入 ShowInfo 資料
        for show in event_data["showInfo"]:
            cursor.execute("""
                INSERT INTO ShowInfo (event_uid, time, location, locationName, onSales, Price, latitude, longitude, endTime)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                event_data["UID"], show["time"], show["location"], show["locationName"], show["onSales"], 
                show["price"], show["latitude"], show["longitude"], show["endTime"]
            ))

        # 插入 Unit 資料
        for unit_type in ["masterUnit", "subUnit", "supportUnit", "otherUnit"]:
            for unit_name in event_data[unit_type]:
                cursor.execute("""
                    INSERT INTO Unit (event_uid, unit_type, unit_name)
                    VALUES (?, ?, ?)
                """, (event_data["UID"], unit_type, unit_name))

    # 提交變更並關閉連接
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
    
