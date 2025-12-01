import json
import sqlite3

# Ouverture de la base de données
conn = sqlite3.connect('avionics.db')

# Initialisation du curseur
cur = conn.cursor()

# Lecture et stockage des données brutees
with open('data.json', 'r') as f:
    data_brute = json.load(f)

# Ajout des données dans notre base de données
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