import sqlite3
from pathlib import Path
#Creating notes.db where all data will be stored inside
#Creating this file so we don't have to write connection code everytime

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "workspace" / "notes.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Path agar normal + use karke concatenate karte toh issues aate 
# / lagane se python Path class se Path.joinpath() ko call karta h so we don't have issues

# BASE_DIR consists the current absolute directory of this file
# parents=True : Creates directory if not exist
# exist_ok=True : Does nothing if directory already exists

def get_connection():
    return sqlite3.connect(DB_PATH)

# Creating this function so we can directly call it in any code and make connection
# When function is called in other file like : conn = sqllite3.connect(DB_PATH)
# SQLite opens/creates that file, loads tables and get ready to take inputs 