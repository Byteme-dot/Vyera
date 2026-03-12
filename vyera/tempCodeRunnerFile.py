from database.schema import create_tables
from services.note_service import create_note, get_notes

def main():
    create_tables()

    create_note("First Note","Hiii this is my first testing note", None)
    notes = get_notes()
    print(notes)
    
if __name__ == "__main__":
    main()