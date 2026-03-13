from database.db import get_connection

def search_notes(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Search dono note ke title aur note ke content se match hogi for better results
    cursor.execute("Select * from notes where title LIKE ? COLLATE NOCASE OR content LIKE ? COLLATE NOCASE",(f"%{keyword}%",f"%{keyword}%"))
    
    # COLLATE NOCASE se results case sensitive nahi honge, chahe 'PYTHON' ho ya 'python' dono result me ayega
    # Agar f"%{keyword}%" ki jagah "%{keyword}%" hota toh python isko as a normal string treat karta 
    # python ki batane ke liye ki {keyword} ko iski value se replace karna h isiliye f lagate h
    
    search_result = cursor.fetchall()
    
    conn.close()
    
    return search_result