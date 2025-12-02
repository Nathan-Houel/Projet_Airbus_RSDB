import json
import sqlite3
import logging
import sys

# Logging initialization
logging.basicConfig(filename='activity.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Opening the database
conn = sqlite3.connect('avionics.db')

# Cursor initialization
cur = conn.cursor()

# Reading and stocking raw data
try : 
    with open('massive_data.json', 'r') as f:
        data_brute = json.load(f)
except FileNotFoundError:
    logging.error("Critical error : data.json not found")
    sys.exit()

# Adding the data in our database
for elt in data_brute:
    system_name = elt['system']

    cur.execute("INSERT OR IGNORE INTO Subsystems (Name) VALUES (?)", (system_name,))
    cur.execute("SELECT ID FROM Subsystems WHERE Name = ?", (system_name,))
    system_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Equipments (Name_equipment, subsystem_id) VALUES (?, ?)", (elt['name'], system_id))
    cur.execute("SELECT ID FROM Equipments WHERE Name_equipment = ?", (elt['name'],))
    equipment_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Limits (equipment_id, measure_type, min_value, max_value) VALUES (?, ?, ?, ?)", 
                (equipment_id, elt["limits"]['type'], elt["limits"]['min'], elt["limits"]['max']))

conn.commit()
conn.close()