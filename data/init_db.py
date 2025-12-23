import os
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

conn : Connection | None = None #đại diện cho connection
curs : Cursor | None = None #đại diện cho con trỏ query

def get_db(name: str | None = None, reset: bool = False):
    global conn, curs #khai báo rằng khi dùng sẽ thay đổi giá trị như biến global
    
    if conn: #nếu đã có db  
        if not reset: #kiểm tra điều kiện có reset không nếu có thì sẽ đi tiếp không thì sẽ dừng luôn
            return
        conn = None #hủy kết nối database 
        
    if not name: #nếu không truyền tên database
        name = os.getenv("SCRYPTID_SQLITE_DB") 
        top_dir = Path(__file__).resolve().parents[1] #trong thư mục hiện tại tìm list các thư mục cha (parents) và chọn cấp 2 ==> src
        print(top_dir)#repo top
        db_dir = top_dir / "db"
        db_name = "cyptid.db"
        db_path = str(db_dir / db_name)
        name = os.getenv("SCRYPTID_SQLITE_DB",db_path)
        
    conn = connect(name, check_same_thread= False)
    curs = conn.cursor()

get_db()