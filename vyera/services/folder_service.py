from database.db import get_connection


def create_folder(folder_name):
     conn = get_connection()
     cursor = conn.cursor()
     
     cursor.execute("Insert into folders (name) values (?)",(folder_name,))
     
     conn.commit()
     conn.close()
     folder_id = cursor.lastrowid
     return folder_id
     
def update_folder_name(folder_name, folder_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("update folders set name = ? where id = ?",(folder_name,folder_id))
    conn.commit()
    conn.close()
    return "Folder name updated successfully"
     
def get_folders():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("Select * from folders")
    
    folders = cursor.fetchall()
    conn.close()
    return folders

def get_folder_by_id(folder_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("Select * from folders where id = ?",(folder_id,))
    
    folder = cursor.fetchone()
    conn.close()
    return folder

def delete_folder(folder_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("delete from folders where id = ?",(folder_id,))
    conn.commit()
    conn.close()
    return "Folder deleted successfully"
