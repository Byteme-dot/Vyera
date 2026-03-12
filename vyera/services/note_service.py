# This file contains all code related to CRUD operations related to notes
from database.db import get_connection

def create_note(title, content, folder_id=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("Insert into notes (title, content, folder_id) values (?,?,?)",(title, content, folder_id))
    
    conn.commit()
    conn.close()
    note_id = cursor.lastrowid
    return note_id
    
def get_notes():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("Select * from notes")
    
    notes = cursor.fetchall()
    conn.close()
    
    return notes

def get_note_by_id(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("Select * from notes where id = ?",(note_id,))
    
    note = cursor.fetchone()
    
    conn.close()
    return note

def update_note(note_id, new_title=None, new_content=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    if new_content is not None and new_title is None:
        cursor.execute("update notes set content = ? where id = ?",(new_content,note_id))
        conn.commit()
        conn.close()
        return "Note Updated Successfully"
    elif new_content is None and new_title is not None:
        cursor.execute("update notes set title = ? where id = ?",(new_title,note_id))
        conn.commit()
        conn.close()
        return "Title Updated Successfully"
    elif new_content is not None and new_title is not None:
        cursor.execute("update notes set title = ? , content = ? where id = ?",(new_title,new_content,note_id))
        conn.commit()
        conn.close()
        return "Title and note Updated Successfully"
    else:
        conn.close()
        return "Nothing to update"
    
    

def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("delete from notes where id = ?",(note_id,))
    
    conn.commit()
    conn.close()
    return "Note deleted successfully"
    
    