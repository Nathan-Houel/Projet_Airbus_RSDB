import subprocess
import os
import time
import sqlite3
from update_limits import update_spec


# ---- Initialize the database ----

# Create a new DB if not existing
if not os.path.exists('avionics.db'):
    # Connecting to the new database
    conn = sqlite3.connect('avionics.db')

    # Reading the SQL architecture
    with open('schema.sql','r') as f:
        sql_script = f.read()

    # Create the tables in the database and close it
    conn.executescript(sql_script)
    conn.close()
    print("New DataBase create !")


# ---- Data Generation ----

# Generating and loading the data
subprocess.run(["python", "generator.py"])
subprocess.run(["python", "main.py"])


# ---- Quality Gate ----

# Test the coherence of the data
try :
    subprocess.run(["pytest"], check=True)
except subprocess.CalledProcessError:
    print("Tests failed !")
    exit()


# ---- Interaction ----

# Modify a limit if wanted
user = input("Do you want to modify a limit ? (y/n) ")
if user == "y":
    id = input('What is the equipment ID ? ')
    val = input("What is the new value ? ")
    update_spec(int(id), float(val))
    print(f"Value modified on the equipment {id}.")


# ---- Visualizing ----

# Launch the dashboard and sent a goodbye msg after Ctrl + C
try :
    subprocess.run(["streamlit", "run", "dashboard.py"])
except KeyboardInterrupt:
    print("Dashboard stop ! See you soon ;)")