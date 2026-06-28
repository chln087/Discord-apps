import sqlite3

conn = sqlite3.connect("data/settings.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS guild_settings (
        guild_id INTEGER PRIMARY KEY,
        welcome_channel INTEGER,
        verify_role INTEGER
)
""")

conn.commit()
conn.close()