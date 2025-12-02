import sqlite3
from datetime import datetime

# Opening the database
conn = sqlite3.connect('avionics.db')
cur = conn.cursor()

equipment_id = 10
new_limit = 126

# Retrieve old value
old_value = cur.execute("SELECT max_value FROM Limits WHERE ID = ?", (equipment_id,)).fetchone()[0]

# Modifying the value
cur.execute("UPDATE Limits SET max_value = ? WHERE ID = ?", (new_limit, equipment_id))

# Adding the data in the History table
cur.execute("INSERT OR IGNORE INTO History \
            (equipment_id, old_value, new_value, change_date) VALUES (?, ?, ?, ?)", \
            (equipment_id, old_value, new_limit, datetime.now().isoformat()))

conn.commit()
conn.close()
