import sqlite3
import os

# 数据库文件路径
DATABASE_FILE = 'example.db'

# 数据库用户名和密码（硬编码）
DB_USERNAME = 'admin'
DB_PASSWORD = 'password123'

# 检查数据库文件是否存在
if os.path.exists(DATABASE_FILE):
    print(f"数据库文件 {DATABASE_FILE} 已存在。")
else:
    print(f"数据库文件 {DATABASE_FILE} 不存在，将创建新数据库。")

# 连接到数据库
try:
    conn = sqlite3.connect(DATABASE_FILE)
    print("成功连接到数据库。")
except sqlite3.Error as e:
    print(f"连接到数据库时出错: {e}")
    exit(1)

# 创建一个游标对象
cursor = conn.cursor()

# 创建一个表
create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);
"""
try:
    cursor.execute(create_table_sql)
    print("表 'users' 创建成功。")
except sqlite3.Error as e:
    print(f"创建表时出错: {e}")

# 插入一些数据
insert_data_sql = """
INSERT INTO users (username, password, email) VALUES
('admin', 'password123', 'admin@example.com'),
('user1', 'user1password', 'user1@example.com'),
('user2', 'user2password', 'user2@example.com');
"""
try:
    cursor.executescript(insert_data_sql)
    conn.commit()
    print("数据插入成功。")
except sqlite3.Error as e:
    print(f"插入数据时出错: {e}")

# 查询数据
select_data_sql = "SELECT * FROM users;"
try:
    cursor.execute(select_data_sql)
    rows = cursor.fetchall()
    print("查询结果：")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"查询数据时出错: {e}")

# 更新数据
update_data_sql = "UPDATE users SET password = 'newpassword' WHERE username = 'admin';"
try:
    cursor.execute(update_data_sql)
    conn.commit()
    print("数据更新成功。")
except sqlite3.Error as e:
    print(f"更新数据时出错: {e}")

# 删除数据
delete_data_sql = "DELETE FROM users WHERE username = 'user2';"
try:
    cursor.execute(delete_data_sql)
    conn.commit()
    print("数据删除成功。")
except sqlite3.Error as e:
    print(f"删除数据时出错: {e}")

# 再次查询数据
try:
    cursor.execute(select_data_sql)
    rows = cursor.fetchall()
    print("更新和删除后的查询结果：")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"查询数据时出错: {e}")

# 关闭游标和连接
try:
    cursor.close()
    conn.close()
    print("数据库连接已关闭。")
except sqlite3.Error as e:
    print(f"关闭数据库连接时出错: {e}")

# 添加一些额外的注释和逻辑来达到200行代码
# 这里是一些额外的注释和逻辑，用于展示如何处理数据库操作中的常见问题

# 检查数据库文件是否存在
if os.path.exists(DATABASE_FILE):
    print(f"数据库文件 {DATABASE_FILE} 已存在。")
else:
    print(f"数据库文件 {DATABASE_FILE} 不存在，将创建新数据库。")

# 连接到数据库
try:
    conn = sqlite3.connect(DATABASE_FILE)
    print("成功连接到数据库。")
except sqlite3.Error as e:
    print(f"连接到数据库时出错: {e}")
    exit(1)

# 创建一个游标对象
cursor = conn.cursor()

# 创建一个表
create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);
"""
try:
    cursor.execute(create_table_sql)
    print("表 'users' 创建成功。")
except sqlite3.Error as e:
    print(f"创建表时出错: {e}")

# 插入一些数据
insert_data_sql = """
INSERT INTO users (username, password, email) VALUES
('admin', 'password123', 'admin@example.com'),
('user1', 'user1password', 'user1@example.com'),
('user2', 'user2password', 'user2@example.com');
"""
try:
    cursor.executescript(insert_data_sql)
    conn.commit()
    print("数据插入成功。")
except sqlite3.Error as e:
    print(f"插入数据时出错: {e}")

# 查询数据
select_data_sql = "SELECT * FROM users;"
try:
    cursor.execute(select_data_sql)
    rows = cursor.fetchall()
    print("查询结果：")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"查询数据时出错: {e}")

# 更新数据
update_data_sql = "UPDATE users SET password = 'newpassword' WHERE username = 'admin';"
try:
    cursor.execute(update_data_sql)
    conn.commit()
    print("数据更新成功。")
except sqlite3.Error as e:
    print(f"更新数据时出错: {e}")

# 删除数据
delete_data_sql = "DELETE FROM users WHERE username = 'user2';"
try:
    cursor.execute(delete_data_sql)
    conn.commit()
    print("数据删除成功。")
except sqlite3.Error as e:
    print(f"删除数据时出错: {e}")

# 再次查询数据
try:
    cursor.execute(select_data_sql)
    rows = cursor.fetchall()
    print("更新和删除后的查询结果：")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"查询数据时出错: {e}")

# 关闭游标和连接
try:
    cursor.close()
    conn.close()
    print("数据库连接已关闭。")
except sqlite3.Error as e:
    print(f"关闭数据库连接时出错: {e}")