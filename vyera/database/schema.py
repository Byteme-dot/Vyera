from .db import get_connection

def create_tables():
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS folders (id Integer Primary Key AUTOINCREMENT,name TEXT NOT NULL)")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, folder_id INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ) ")
    
    conn.commit()
    conn.close()

