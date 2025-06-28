# init_db.py
from db import create_user_table

if __name__ == "__main__":
    create_user_table()
    print("✅ data.db created and user table initialized.")
