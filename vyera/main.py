from database.schema import create_tables
from services.note_service import create_note, get_notes, update_note, delete_note, get_notes_by_id, get_notes_by_folder
from services.folder_service import create_folder, get_folders, delete_folder, update_folder_name
from services.search_service import search_notes

def main():
    create_tables()
    
    run = True
    
    while run:

        print("\n===== Vyera Test Menu =====")
        print("1. Create Folder")
        print("2. Show Folders")
        print("3. Create Note")
        print("4. Show All Notes")
        print("5. Show Notes By Folder")
        print("6. Search Notes")
        print("7. Update Note")
        print("8. Delete Note")
        print("9. Delete Folder")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter folder name: ")
            folder_id = create_folder(name)
            print("Folder created with id:", folder_id)

        elif choice == "2":
            folders = get_folders()
            print("\nFolders:")
            for f in folders:
                print(f)

        elif choice == "3":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            folder_id = input("Enter folder id (or press enter for None): ")

            if folder_id == "":
                folder_id = None
            else:
                folder_id = int(folder_id)

            note_id = create_note(title, content, folder_id)
            print("Note created with id:", note_id)

        elif choice == "4":
            notes = get_notes()
            print("\nNotes:")
            for n in notes:
                print(n)

        elif choice == "5":
            folder_id = int(input("Enter folder id: "))
            notes = get_notes_by_folder(folder_id)

            print("\nNotes in folder:")
            for n in notes:
                print(n)

        elif choice == "6":
            keyword = input("Enter search keyword: ")
            results = search_notes(keyword)

            print("\nSearch results:")
            for r in results:
                print(r)

        elif choice == "7":
            note_id = int(input("Enter note id: "))
            title = input("New title (press enter to skip): ")
            content = input("New content (press enter to skip): ")

            title = None if title == "" else title
            content = None if content == "" else content

            print(update_note(note_id, title, content))

        elif choice == "8":
            note_id = int(input("Enter note id: "))
            print(delete_note(note_id))

        elif choice == "9":
            folder_id = int(input("Enter folder id: "))
            print(delete_folder(folder_id))

        elif choice == "0":
            run = False
            print("Exiting...")

        else:
            print("Invalid choice")
    
    
# Below code make sure karta h ki main function tabhi call ho jab iss file ko run kiya jaye
# Agar iss file ko import kiya kisi aur file me toh function automatically run ho jayega which is not good
# Jab ye file run hoti h toh ek variable banta h __name__ = "__main__" , so the condition becomes true
# Jab ye file import ki jati h kisi aur file me tab variable banta h __name__ = "main" , so condition becomes false
# This way jab ham iss file ke function ko particularly import karke call karenge tabhi kaam karega

if __name__ == "__main__":
    main()